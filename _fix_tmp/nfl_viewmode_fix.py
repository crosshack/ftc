# -*- coding: utf-8 -*-
import sys, glob, os

REPO = sys.argv[1]

OLD = 'data-viewmode="total">総数</button>'
NEW = 'data-viewmode="total">合計</button>'

files = sorted(glob.glob(f"{REPO}/nfl-db/*.html"))
assert len(files) == 33, f"expected 33 files, found {len(files)}"

results = []
for path in files:
    with open(path, encoding="utf-8") as f:
        html = f.read()
    orig = html
    n = html.count(OLD)
    assert n == 8, f"{os.path.basename(path)}: expected 8 occurrences of OLD, found {n}"
    html = html.replace(OLD, NEW)
    assert html.count(NEW) == 8
    assert OLD not in html
    assert html != orig
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    results.append(os.path.basename(path))

print(f"OK: {len(results)} files updated (総数 -> 合計, 8 occurrences each)")
