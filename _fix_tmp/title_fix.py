# -*- coding: utf-8 -*-
import sys

REPO = sys.argv[1]

OLD = "なぜNFLでゾーンカバレッジがここまで拡大したのか"
NEW = "なぜゾーンカバレッジがここまで拡大したのか"

targets = [
    (f"{REPO}/topics/zone-coverage-1.html", 4),
    (f"{REPO}/topics/zone-coverage-2.html", 1),
    (f"{REPO}/assets/js/topics-data.js", 1),
]

for path, expected_n in targets:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    orig = content
    n = content.count(OLD)
    assert n == expected_n, f"{path}: expected {expected_n} occurrences, found {n}"
    content = content.replace(OLD, NEW)
    assert OLD not in content
    assert content != orig
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {path} ({expected_n} occurrences replaced)")

print("ALL FILES UPDATED")
