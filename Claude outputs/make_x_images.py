#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_x_images.py ― 記事内のSVG図を、X（Twitter）向けの1200×675 PNGに書き出す。

考え方:
  自前でCSSを再現せず、Playwrightで「実際の記事ページ」をfile://で開き、
  そのページの中に1200×675の額縁（オーバーレイ）を作って、図のSVGを複製して流し込む。
  こうすることで、フォント・色・線の太さがサイト本番と完全に一致する。

使い方:
  # リポジトリのルートで実行する
  python3 _setup/scripts/make_x_images.py --list topics/real-play-explained-001.html
  python3 _setup/scripts/make_x_images.py topics/real-play-explained-001.html
  python3 _setup/scripts/make_x_images.py topics/real-play-explained-001.html --fig 2
  python3 _setup/scripts/make_x_images.py --all
  python3 _setup/scripts/make_x_images.py --all --no-label

出力:
  Tmp/x-images/<記事ファイル名>-fig<N>.png （Tmp/ はgitignore対象）

オプション:
  --list           図の一覧（番号・figcaption）だけ表示して終了
  --fig N          N番目の図だけ書き出す（1始まり、複数指定可）
  --all            topics/ 配下の全記事を対象にする
  --caption        figcaption を画像下部に焼き込む（既定: 焼き込まない）
  --no-label       左上のテーマラベルを出さない（既定: 出す）
  --no-credit      右下の footballtactics.club を出さない（既定: 出す）
  --size W H       出力サイズ（既定: 1200 675）
  --out DIR        出力先（既定: Tmp/x-images）
  --scale N        レンダリング倍率（既定: 2。2で描いてから縮小するので文字が締まる）
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("playwright が見つかりません。 pip install playwright && playwright install chromium")

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# ---------------------------------------------------------------- 額縁の組み立て
# ページ内で実行するJS。図を1つ選び、1200×675の額縁に入れて、その要素を返す。
BUILD_FRAME_JS = r"""
(opts) => {
  const { index, width, height, label, credit, caption } = opts;

  // 既存の額縁が残っていれば消す
  const old = document.getElementById('__x_frame__');
  if (old) old.remove();

  // 対象の図を拾う。figure > svg を基本とし、無ければ本文中の svg を拾う
  let svgs = Array.from(document.querySelectorAll('.article-body figure svg, article figure svg, figure svg'));
  if (!svgs.length) {
    svgs = Array.from(document.querySelectorAll('.article-body svg, article svg'))
      .filter(s => (s.viewBox && s.viewBox.baseVal && s.viewBox.baseVal.width > 120));
  }
  const svg = svgs[index];
  if (!svg) return null;

  // ページの地の色・文字色をそのまま使う（サイト側のCSSが唯一の正）
  const bodyCS = getComputedStyle(document.body);
  const bg = bodyCS.backgroundColor && bodyCS.backgroundColor !== 'rgba(0, 0, 0, 0)'
        ? bodyCS.backgroundColor : '#ffffff';
  const fg = bodyCS.color || '#111111';
  const fontFamily = bodyCS.fontFamily;

  const frame = document.createElement('div');
  frame.id = '__x_frame__';
  Object.assign(frame.style, {
    position: 'fixed', left: '0px', top: '0px', zIndex: '2147483647',
    width: width + 'px', height: height + 'px',
    background: bg, color: fg, fontFamily: fontFamily,
    boxSizing: 'border-box', padding: '40px 56px',
    display: 'flex', flexDirection: 'column', overflow: 'hidden',
  });

  // --- 上段: テーマラベル
  const head = document.createElement('div');
  Object.assign(head.style, {
    flex: '0 0 auto', display: 'flex', alignItems: 'baseline', gap: '10px',
    fontSize: '19px', letterSpacing: '.04em', opacity: label ? '.72' : '0',
    minHeight: '26px',
  });
  if (label) {
    const tagEl = document.querySelector('.theme-tag, .page-head .theme-tag, .meta .theme-tag');
    const h1 = document.querySelector('.article-body h1, article h1, h1');
    const themeTxt = tagEl ? tagEl.textContent.trim().replace(/\s+/g, ' ') : '';
    const titleTxt = h1 ? h1.childNodes[0].textContent.trim().replace(/\s+/g, ' ') : '';
    head.textContent = themeTxt || titleTxt || '';
  }
  frame.appendChild(head);

  // --- 中段: 図
  const stage = document.createElement('div');
  Object.assign(stage.style, {
    flex: '1 1 auto', display: 'flex', alignItems: 'center', justifyContent: 'center',
    minHeight: '0', padding: '10px 0',
  });
  const clone = svg.cloneNode(true);
  clone.removeAttribute('width');
  clone.removeAttribute('height');
  clone.style.width = 'auto';
  clone.style.height = 'auto';
  clone.style.maxWidth = '100%';
  clone.style.maxHeight = '100%';
  stage.appendChild(clone);
  frame.appendChild(stage);

  // --- 下段: キャプション ／ クレジット
  const foot = document.createElement('div');
  Object.assign(foot.style, {
    flex: '0 0 auto', display: 'flex', alignItems: 'flex-end', gap: '24px',
    justifyContent: 'space-between', minHeight: '26px',
  });

  const capEl = document.createElement('div');
  Object.assign(capEl.style, {
    fontSize: '18px', lineHeight: '1.6', opacity: '.78',
    maxWidth: '72%', overflow: 'hidden',
    display: '-webkit-box', WebkitLineClamp: '2', WebkitBoxOrient: 'vertical',
  });
  if (caption) {
    const fig = svg.closest('figure');
    const cap = fig ? fig.querySelector('figcaption') : null;
    capEl.textContent = cap ? cap.textContent.trim().replace(/\s+/g, ' ').replace(/^図[:：]\s*/, '') : '';
  }
  foot.appendChild(capEl);

  const credEl = document.createElement('div');
  Object.assign(credEl.style, {
    fontSize: '18px', letterSpacing: '.06em', opacity: credit ? '.55' : '0',
    whiteSpace: 'nowrap', flex: '0 0 auto',
  });
  credEl.textContent = 'footballtactics.club';
  foot.appendChild(credEl);

  frame.appendChild(foot);
  document.body.appendChild(frame);
  return true;
}
"""

COUNT_FIGURES_JS = r"""
() => {
  let svgs = Array.from(document.querySelectorAll('.article-body figure svg, article figure svg, figure svg'));
  if (!svgs.length) {
    svgs = Array.from(document.querySelectorAll('.article-body svg, article svg'))
      .filter(s => (s.viewBox && s.viewBox.baseVal && s.viewBox.baseVal.width > 120));
  }
  return svgs.map((s, i) => {
    const fig = s.closest('figure');
    const cap = fig ? fig.querySelector('figcaption') : null;
    const vb = s.getAttribute('viewBox') || '';
    return {
      n: i + 1,
      viewBox: vb,
      caption: cap ? cap.textContent.trim().replace(/\s+/g, ' ') : '(figcaptionなし)',
    };
  });
}
"""


def render_article(page, html_path: Path, out_dir: Path, args):
    """1記事ぶんの図をPNGに書き出す。書き出したファイルのリストを返す。"""
    page.goto(html_path.resolve().as_uri(), wait_until="load")
    # Webフォント・遅延スクリプトの落ち着きを待つ
    page.evaluate("document.fonts ? document.fonts.ready : null")
    page.wait_for_timeout(400)

    figs = page.evaluate(COUNT_FIGURES_JS)
    if not figs:
        print(f"  図なし: {html_path}")
        return []

    if args.list:
        print(f"\n{html_path}")
        for f in figs:
            print(f"  図{f['n']}  viewBox={f['viewBox']}")
            print(f"        {f['caption'][:90]}")
        return []

    targets = args.fig if args.fig else [f["n"] for f in figs]
    written = []
    w, h = args.size
    scale = args.scale

    for n in targets:
        if n < 1 or n > len(figs):
            print(f"  図{n} は存在しません（この記事の図は{len(figs)}枚）")
            continue
        ok = page.evaluate(BUILD_FRAME_JS, {
            "index": n - 1, "width": w, "height": h,
            "label": not args.no_label,
            "credit": not args.no_credit,
            "caption": args.caption,
        })
        if not ok:
            print(f"  図{n} の取得に失敗しました")
            continue

        el = page.query_selector("#__x_frame__")
        out = out_dir / f"{html_path.stem}-fig{n}.png"
        el.screenshot(path=str(out))

        # scale倍で描いてから指定サイズへ縮小（文字のアンチエイリアスが締まる）
        if scale > 1 and HAS_PIL:
            img = Image.open(out)
            if img.size != (w, h):
                img.resize((w, h), Image.LANCZOS).save(out, optimize=True)
        elif scale > 1 and not HAS_PIL:
            print("  （Pillow未導入のため縮小せず、そのままのサイズで書き出しました）")

        size = Image.open(out).size if HAS_PIL else "?"
        print(f"  ✅ {out}  {size}")
        written.append(out)

    page.evaluate("() => { const e = document.getElementById('__x_frame__'); if (e) e.remove(); }")
    return written


def main():
    ap = argparse.ArgumentParser(description="記事内のSVG図をX向けPNGに書き出す")
    ap.add_argument("articles", nargs="*", help="記事のHTMLパス（リポジトリルートからの相対）")
    ap.add_argument("--all", action="store_true", help="topics/ 配下の全記事を対象にする")
    ap.add_argument("--list", action="store_true", help="図の一覧だけ表示する")
    ap.add_argument("--fig", type=int, action="append", help="書き出す図の番号（1始まり、複数指定可）")
    ap.add_argument("--caption", action="store_true", help="figcaptionを画像に焼き込む")
    ap.add_argument("--no-label", action="store_true", help="左上のテーマラベルを出さない")
    ap.add_argument("--no-credit", action="store_true", help="右下のクレジットを出さない")
    ap.add_argument("--size", nargs=2, type=int, default=[1200, 675], metavar=("W", "H"))
    ap.add_argument("--out", default="Tmp/x-images", help="出力先ディレクトリ")
    ap.add_argument("--scale", type=int, default=2, help="レンダリング倍率（既定2）")
    args = ap.parse_args()

    root = Path.cwd()
    if not (root / "topics").is_dir():
        sys.exit("リポジトリのルート（topics/ がある階層）で実行してください。")

    if args.all:
        paths = sorted(p for p in (root / "topics").glob("*.html") if "draft" not in p.name)
    elif args.articles:
        paths = [Path(a) for a in args.articles]
    else:
        sys.exit("記事を指定するか --all を付けてください。")

    missing = [p for p in paths if not p.is_file()]
    if missing:
        sys.exit("見つかりません: " + ", ".join(str(m) for m in missing))

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    w, h = args.size
    total = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(
            viewport={"width": max(w + 80, 1400), "height": max(h + 80, 900)},
            device_scale_factor=args.scale,
        )
        for p in paths:
            print(f"\n▶ {p}")
            total += render_article(page, p, out_dir, args)
        browser.close()

    if not args.list:
        print(f"\n合計 {len(total)} 枚を {out_dir}/ に書き出しました。")


if __name__ == "__main__":
    main()
