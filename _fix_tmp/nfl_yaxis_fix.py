# -*- coding: utf-8 -*-
import sys, glob, os

REPO = sys.argv[1]

OLD = "(state.viewMode === 'avg' ? '試合平均' : '総数')"
NEW = "(state.viewMode === 'avg' ? '試合平均' : '合計')"

files = sorted(glob.glob(f"{REPO}/nfl-db/*.html"))
assert len(files) == 33, f"expected 33 files, found {len(files)}"

for path in files:
    with open(path, encoding="utf-8") as f:
        html = f.read()
    orig = html
    n = html.count(OLD)
    assert n == 1, f"{os.path.basename(path)}: expected 1 occurrence of OLD, found {n}"
    html = html.replace(OLD, NEW)
    assert OLD not in html
    assert html != orig
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print(f"OK: {len(files)} files updated (yMainTitle: 総数 -> 合計)")
