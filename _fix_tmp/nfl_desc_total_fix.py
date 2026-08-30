# -*- coding: utf-8 -*-
import sys, glob, os

REPO = sys.argv[1]

FULLWIDTH_OLD = '（試合平均/総数）'
FULLWIDTH_NEW = '（試合平均/合計）'
HALFWIDTH_OLD = '(試合平均/総数)'
HALFWIDTH_NEW = '(試合平均/合計)'

files = sorted(glob.glob(f"{REPO}/nfl-db/*.html"))
assert len(files) == 33, f"expected 33 files, found {len(files)}"

FULLWIDTH_ONLY = {"new-england-patriots.html", "nfl.html"}

results = []
for path in files:
    base = os.path.basename(path)
    with open(path, encoding="utf-8") as f:
        html = f.read()
    orig = html

    n_full = html.count(FULLWIDTH_OLD)
    n_half = html.count(HALFWIDTH_OLD)

    if base in FULLWIDTH_ONLY:
        assert n_full == 8, f"{base}: expected 8 full-width, found {n_full}"
        assert n_half == 0, f"{base}: expected 0 half-width, found {n_half}"
    else:
        assert n_full == 4, f"{base}: expected 4 full-width, found {n_full}"
        assert n_half == 4, f"{base}: expected 4 half-width, found {n_half}"

    html = html.replace(FULLWIDTH_OLD, FULLWIDTH_NEW)
    html = html.replace(HALFWIDTH_OLD, HALFWIDTH_NEW)

    assert FULLWIDTH_OLD not in html
    assert HALFWIDTH_OLD not in html
    assert html != orig

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    results.append((base, n_full, n_half))

print(f"OK: {len(results)} files updated (chart-desc: 総数 -> 合計)")
for base, nf, nh in results:
    if nf == 8:
        print(f"  {base}: full-width x8")
print("(remaining 31 files: full-width x4 + half-width x4 each)")
