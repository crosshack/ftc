#!/usr/bin/env python3
"""
note 見出し画像ジェネレーター（FOOTBALLTACTICS.CLUB / 実戦プレー解説 速報版）

  1280x670 のPNGを書き出す。デザイン仕様はC-5改（2026-09-08 FIX）。
  レイアウト・配色の根拠は note-eyecatch-spec.md を参照。

使い方:
  python3 make_note_eyecatch.py --away NE --home SEA \
      --week "2026 WEEK 1" \
      --line1 "開幕戦を決めた、" --line2 "カバー0ブリッツの1プレー" \
      --out eyecatch.png

必要なもの:
  - playwright（chromium）
  - _setup/fonts/ の woff2（Oswald 500/600/700, NotoSansJP jp/latin 500/700）
  - assets/img/logo-combined.svg
"""
import argparse, base64, pathlib, sys
from playwright.sync_api import sync_playwright

# =============================================================================
# チームカラー（assets/js/nfl-db-data.js のサムネイルSVGから抽出）
#   (表示名, primary=アイコン背景, bar=アイコン下部バー, stroke=アイコン枠線)
# =============================================================================
TEAMS = {
"BUF":("BILLS","#00338D","#C60C30","#0C2E82"), "MIA":("DOLPHINS","#008E97","#F58220","#005778"),
"NE":("PATRIOTS","#002244","#C60C30","#B0B7BC"), "NYJ":("JETS","#003F2D","#000000","#A5ACAF"),
"BAL":("RAVENS","#241773","#9E7C0C","#9E7C0C"), "CIN":("BENGALS","#FB4F14","#000000","#000000"),
"CLE":("BROWNS","#FF3C00","#311D00","#A5ACAF"), "PIT":("STEELERS","#000000","#FFB612","#C60C30"),
"HOU":("TEXANS","#03202F","#A71930","#00071C"), "IND":("COLTS","#002C5F","#A5ACAF","#013369"),
"JAX":("JAGUARS","#006778","#000000","#9F792C"), "TEN":("TITANS","#4495D2","#D50A0A","#A5ACAF"),
"DEN":("BRONCOS","#002244","#FB4F14","#00234C"), "KC":("CHIEFS","#E31837","#FFB612","#000000"),
"LAC":("CHARGERS","#007BC7","#FFC20E","#FFB612"), "LV":("RAIDERS","#000000","#A5ACAF","#A6AEB0"),
"DAL":("COWBOYS","#002244","#B0B7BC","#ACC0C6"), "NYG":("GIANTS","#0B2265","#A71930","#A5ACAF"),
"PHI":("EAGLES","#004C54","#A5ACAF","#ACC0C6"), "WAS":("COMMANDERS","#5A1414","#FFB612","#000000"),
"CHI":("BEARS","#0B162A","#E64100","#0B162A"), "DET":("LIONS","#0076B6","#B0B7BC","#000000"),
"GB":("PACKERS","#203731","#FFB612","#1C2D25"), "MIN":("VIKINGS","#4F2683","#FFC62F","#E9BF9B"),
"ATL":("FALCONS","#A71930","#000000","#A5ACAF"), "CAR":("PANTHERS","#0085CA","#000000","#BFC0BF"),
"NO":("SAINTS","#D3BC8D","#000000","#9F8958"), "TB":("BUCCANEERS","#A71930","#322F2B","#000000"),
"ARI":("CARDINALS","#97233F","#000000","#FFB612"), "LAR":("RAMS","#003594","#FFD100","#001532"),
"SEA":("SEAHAWKS","#002244","#69BE28","#A5ACAF"), "SF":("49ERS","#AA0000","#B3995D","#000000"),
}

# =============================================================================
# レイアウト定数（2026-09-08 FIX）
# =============================================================================
W, H         = 1280, 670   # noteの見出し画像の推奨サイズ
BAND_H       = 300         # 上部帯の高さ
ICON_SIZE    = 104         # チームアイコンの一辺
NAME_GAP     = 22          # アイコンとチーム名の間隔
CENTER_GAP   = 118         # 中心からアイコン内側までの距離（アイコン間 = 236px）
NAME_SIZE    = 54          # チーム名。最長名(COMMANDERS/BUCCANEERS)で左端82pxに収まる上限
SEP_SIZE     = 50          # 区切り記号。小文字のため実高は30px（チーム名の実高69pxに対し43%）
TITLE_SIZE   = 52
PAD_X        = 80
BG           = "#141713"   # --bg-alt（Xヘッダー・noteヘッダー画像と同一）
BAND_BG      = "#0c0e0c"   # --bg
TEXT         = "#eceee9"   # --text
TEXT_DIM     = "#a8afa2"   # --text-dim
WEEK_COLOR   = "#8b938a"   # ブランド緑を避けてニュートラルに（チームカラーと競合させない）
VS_COLOR     = "#5c635a"
LINE         = "#2a2e28"   # --line
SERIES_LABEL = "実戦プレー解説"

def _p(root, *parts):
    return pathlib.Path(root).joinpath(*parts)

def font_faces(font_dir):
    spec = [("Oswald",500,"Oswald-500.woff2"), ("Oswald",600,"Oswald-600.woff2"),
            ("Oswald",700,"Oswald-700.woff2"),
            ("NotoJP",500,"NotoSansJP-jp-500.woff2"), ("NotoJP",700,"NotoSansJP-jp-700.woff2"),
            ("NotoJP",500,"NotoSansJP-latin-500.woff2"), ("NotoJP",700,"NotoSansJP-latin-700.woff2")]
    out = []
    for fam, wt, fn in spec:
        f = _p(font_dir, fn)
        if not f.exists():
            sys.exit(f"フォントが見つかりません: {f}")
        b64 = base64.b64encode(f.read_bytes()).decode()
        out.append(f'@font-face{{font-family:"{fam}";font-style:normal;font-weight:{wt};'
                   f'font-display:block;src:url(data:font/woff2;base64,{b64}) format("woff2");}}')
    return "".join(out)

def icon_svg(abbr, size=ICON_SIZE):
    """NFL.DBのチームサムネイルと同一構造のアイコン。"""
    _, prim, bar, stroke = TEAMS[abbr]
    fs = 26 if len(abbr) <= 2 else 19
    return (f'<svg viewBox="0 0 70 70" width="{size}" height="{size}" '
            f'xmlns="http://www.w3.org/2000/svg" style="display:block;flex:0 0 auto;">'
            f'<rect x="4" y="4" width="62" height="62" rx="10" fill="{prim}"/>'
            f'<rect x="4" y="4" width="62" height="62" rx="10" fill="none" stroke="{stroke}" '
            f'stroke-width="1.5" opacity="0.5"/>'
            f'<text x="35" y="41" text-anchor="middle" font-family="Oswald, sans-serif" '
            f'font-weight="700" font-size="{fs}" fill="#ffffff" letter-spacing="1">{abbr}</text>'
            f'<rect x="16" y="50" width="38" height="5" rx="2.5" fill="{bar}"/></svg>')

def build_html(away, home, week, line1, line2, sep, faces, logo_uri):
    css = f"""{faces}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:{W}px;height:{H}px;overflow:hidden;}}
.c{{width:{W}px;height:{H}px;display:flex;flex-direction:column;background:{BG};
   font-family:"NotoJP",sans-serif;-webkit-font-smoothing:antialiased;}}
.osw{{font-family:"Oswald","NotoJP",sans-serif;}}
.band{{flex:0 0 {BAND_H}px;background:{BAND_BG};position:relative;}}
.wkwrap{{position:absolute;top:30px;left:0;right:0;text-align:center;}}
.wk{{color:{WEEK_COLOR};font-weight:600;font-size:23px;letter-spacing:.24em;}}
.sep{{position:absolute;left:50%;top:calc(50% + 8px);transform:translate(-50%,-50%);
     color:{VS_COLOR};font-weight:500;font-size:{SEP_SIZE}px;}}
.side{{position:absolute;top:calc(50% + 8px);transform:translateY(-50%);
      display:flex;align-items:center;gap:{NAME_GAP}px;}}
.tname{{color:{TEXT};font-weight:700;font-size:{NAME_SIZE}px;line-height:1;white-space:nowrap;}}
.body{{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 {PAD_X}px;}}
.title{{color:{TEXT};font-weight:700;font-size:{TITLE_SIZE}px;line-height:1.36;}}
.foot{{flex:0 0 84px;border-top:1px solid {LINE};display:flex;align-items:center;
      justify-content:space-between;padding:0 {PAD_X}px;}}
.foot .s{{color:{TEXT_DIM};font-size:20px;font-weight:500;letter-spacing:.08em;}}
.foot img{{width:210px;display:block;}}
"""
    body = f"""<div class="c">
  <div class="band">
    <div class="wkwrap"><span class="osw wk">{week}</span></div>
    <div class="side" style="right:calc(50% + {CENTER_GAP}px);">
      <div class="osw tname">{TEAMS[away][0]}</div>{icon_svg(away)}</div>
    <div class="osw sep">{sep}</div>
    <div class="side" style="left:calc(50% + {CENTER_GAP}px);">
      {icon_svg(home)}<div class="osw tname">{TEAMS[home][0]}</div></div>
  </div>
  <div class="body"><div class="title">{line1}<br>{line2}</div></div>
  <div class="foot"><div class="s">{SERIES_LABEL}</div><img src="{logo_uri}"></div>
</div>"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--away", required=True, help="アウェイチームの略称（左側）例: NE")
    ap.add_argument("--home", required=True, help="ホームチームの略称（右側）例: SEA")
    ap.add_argument("--week", required=True, help='例: "2026 WEEK 1"')
    ap.add_argument("--line1", required=True, help="タイトル1行目")
    ap.add_argument("--line2", required=True, help="タイトル2行目")
    ap.add_argument("--sep", default="vs", choices=["vs", "@"], help="区切り記号（既定: vs）")
    ap.add_argument("--out", default="note-eyecatch.png")
    ap.add_argument("--font-dir", default="_setup/fonts")
    ap.add_argument("--logo", default="assets/img/logo-combined.svg")
    a = ap.parse_args()

    for t in (a.away, a.home):
        if t not in TEAMS:
            sys.exit(f"未知のチーム略称: {t}\n使える略称: {', '.join(sorted(TEAMS))}")

    logo = pathlib.Path(a.logo)
    if not logo.exists():
        sys.exit(f"ロゴが見つかりません: {logo}")
    logo_uri = "data:image/svg+xml;base64," + base64.b64encode(logo.read_bytes()).decode()

    html = build_html(a.away, a.home, a.week, a.line1, a.line2, a.sep,
                      font_faces(a.font_dir), logo_uri)
    tmp = pathlib.Path(a.out).with_suffix(".tmp.html")
    tmp.write_text(html, encoding="utf-8")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
            pg.goto(tmp.resolve().as_uri())
            pg.wait_for_timeout(500)
            pg.screenshot(path=a.out, clip={"x":0,"y":0,"width":W,"height":H})
            b.close()
    finally:
        tmp.unlink(missing_ok=True)
    print(f"書き出しました: {a.out}  ({TEAMS[a.away][0]} {a.sep} {TEAMS[a.home][0]})")

if __name__ == "__main__":
    main()
