# -*- coding: utf-8 -*-
import re, sys, os

REPO = sys.argv[1]

TOPICS_JS = f"{REPO}/assets/js/topics-data.js"
GLOSSARY_DIR = f"{REPO}/glossary"

with open(TOPICS_JS, encoding="utf-8") as f:
    content = f.read()

def extract_entry(slug):
    idx = content.find(f'slug: "{slug}"')
    start = content.rfind('{', 0, idx)
    depth = 0
    i = start
    while True:
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                break
        i += 1
    obj_text = content[start:i+1]
    def field(name, text=obj_text):
        m = re.search(name + r':\s*"((?:[^"\\]|\\.)*)"', text)
        return m.group(1) if m else None
    title = field('title')
    excerpt = field('excerpt')
    date = field('date')
    readMin = re.search(r'readMin:\s*(\d+)', obj_text).group(1)
    theme_name = re.search(r'theme:\s*\{[^}]*name:\s*"([^"]+)"', obj_text).group(1)
    theme_part = re.search(r'theme:\s*\{[^}]*part:\s*"([^"]+)"', obj_text).group(1)
    thumb_m = re.search(r"thumb:\s*'((?:[^'\\]|\\.)*)'", obj_text)
    thumb = thumb_m.group(1)
    tags_start = obj_text.find('tags:')
    tags_arr_start = obj_text.find('[', tags_start)
    depth = 0
    j = tags_arr_start
    while True:
        if obj_text[j] == '[':
            depth += 1
        elif obj_text[j] == ']':
            depth -= 1
            if depth == 0:
                break
        j += 1
    tags_block = obj_text[tags_arr_start:j+1]
    tag_slugs = re.findall(r'slug:\s*"([^"]+)"', tags_block)
    tag_names = re.findall(r'name:\s*"([^"]+)"', tags_block)
    return {
        'slug': slug, 'title': title, 'excerpt': excerpt, 'date': date, 'readMin': readMin,
        'theme_name': theme_name, 'theme_part': theme_part, 'thumb': thumb,
        'tags': list(zip(tag_slugs, tag_names))
    }

ART1 = extract_entry('zone-coverage-1')
ART2 = extract_entry('zone-coverage-2')

def build_card(article):
    date_fmt = article['date'].replace('-', '.')
    tags_html = ' '.join(f'<a href="{s}.html">#{n}</a>' for s, n in article['tags'])
    return (
        '<article class="card">'
        '<svg class="thumb" viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">'
        f'{article["thumb"]}</svg>'
        '<div>'
        f'<span class="theme-badge">{article["theme_name"]} ・ {article["theme_part"]}</span>'
        f'<h3><a href="../topics/{article["slug"]}.html">{article["title"]}'
        '<svg class="chev" viewBox="0 0 9 14" aria-hidden="true">'
        '<path d="M0,0 L5,7 L0,14" fill="none" stroke="#3ecf6e" stroke-width="1.6" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg></a></h3>'
        f'<p>{article["excerpt"]}</p>'
        f'<div class="meta">{date_fmt} ・ 読了目安 {article["readMin"]}分</div>'
        f'<div class="topic-tags">{tags_html}</div>'
        '</div></article>'
    )

CARD1 = build_card(ART1)
CARD2 = build_card(ART2)

TOPICS_ICON = ('<svg class="section-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
               'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
               '<polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/>'
               '<line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>')

# slug -> which articles need cards ("1", "2", or "12")
TARGETS = {
    'base-4-3': '2',
    'blitz': '2',
    'box': '2',
    'cover-3': '2',
    'cover-4': '2',
    'coverage': '12',
    'defense': '12',
    'defensive-coordinator': '2',
    'dime-package': '1',
    'front': '2',
    'linebacker': '1',
    'man-to-man-coverage': '1',
    'nickel-package': '1',
    'personnel': '1',
    'quarterback': '1',
    'route': '2',
    'safety': '1',
    'single-high': '2',
    'tight-end': '1',
    'wide-receiver': '1',
    'zone': '12',
    'zone-coverage': '12',
}

NO_SECTION_EXPECTED = {'base-4-3', 'cover-4', 'dime-package', 'man-to-man-coverage', 'single-high', 'zone-coverage'}

results = []

for slug, need in TARGETS.items():
    path = f"{GLOSSARY_DIR}/{slug}.html"
    with open(path, encoding='utf-8') as f:
        html = f.read()
    orig = html

    cards = []
    if '1' in need:
        cards.append(CARD1)
    if '2' in need:
        cards.append(CARD2)
    cards_joined = '\n    '.join(cards)

    has_section = '関連するトピックス' in html
    assert has_section == (slug not in NO_SECTION_EXPECTED), f"{slug}: section presence mismatch (expected no-section={slug in NO_SECTION_EXPECTED}, found has_section={has_section})"

    if has_section:
        # locate the card-list div belonging to the 関連するトピックス section
        h2_idx = html.find('関連するトピックス')
        divstart = html.find('<div class="card-list">', h2_idx)
        assert divstart != -1, f"{slug}: card-list div not found after 関連するトピックス"
        content_start = divstart + len('<div class="card-list">')
        depth = 1
        i = content_start
        while depth > 0:
            nd = html.find('<div', i)
            nc = html.find('</div>', i)
            if nc == -1:
                raise AssertionError(f"{slug}: unbalanced div while scanning card-list")
            if nd != -1 and nd < nc:
                depth += 1
                i = nd + 4
            else:
                depth -= 1
                i = nc + 6
        close_div_start = i - 6  # position of '</div>' start
        before = html[content_start:close_div_start]
        assert before.rstrip().endswith('</article>'), f"{slug}: card-list does not end with </article> as expected: ...{before[-50:]!r}"
        # insert new cards right after the last </article>, preserving existing trailing whitespace style
        trailing_ws_len = len(before) - len(before.rstrip())
        trailing_ws = before[len(before.rstrip()):]
        new_before = before.rstrip() + '\n    ' + cards_joined + trailing_ws
        html = html[:content_start] + new_before + html[close_div_start:]
        assert html != orig, f"{slug}: no change applied (existing section path)"
    else:
        idx2 = html.find('関連する用語')
        assert idx2 != -1, f"{slug}: 関連する用語 anchor not found"
        h2start = html.rfind('<h2', 0, idx2)
        prev_div_end = html.rfind('</div>', 0, h2start) + len('</div>')
        new_section = (
            f'<h2>{TOPICS_ICON}関連するトピックス</h2>\n'
            f'  <div class="card-list">\n'
            f'    {cards_joined}\n'
            f'  </div>'
        )
        html = html[:prev_div_end] + '\n\n  ' + new_section + '\n\n  ' + html[h2start:]
        assert html != orig, f"{slug}: no change applied (new-section path)"

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    results.append((slug, need, has_section))

print(f"OK: {len(results)} glossary pages updated")
for slug, need, has_section in results:
    print(f"  {slug}: need={need} had_section={has_section}")
