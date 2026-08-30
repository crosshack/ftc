# -*- coding: utf-8 -*-
import sys

REPO = sys.argv[1]

SLUGS = [
    "arizona-cardinals", "atlanta-falcons", "baltimore-ravens", "buffalo-bills",
    "carolina-panthers", "chicago-bears", "cincinnati-bengals", "cleveland-browns",
    "dallas-cowboys", "denver-broncos", "detroit-lions", "green-bay-packers",
    "houston-texans", "indianapolis-colts", "jacksonville-jaguars", "kansas-city-chiefs",
    "las-vegas-raiders", "los-angeles-chargers", "los-angeles-rams", "miami-dolphins",
    "minnesota-vikings", "new-orleans-saints", "new-york-giants", "new-york-jets",
    "philadelphia-eagles", "pittsburgh-steelers", "san-francisco-49ers", "seattle-seahawks",
    "tampa-bay-buccaneers", "tennessee-titans", "washington-commanders",
]
# NOTE: new-england-patriots and nfl.html intentionally excluded (NE already done; nfl.html has its own script).

OLD_TOC = '''      <li><span class="index">06</span><a href="#chart-defense-formation">ディフェンス編成別プレー回数</a></li>
    </ol>'''
NEW_TOC = '''      <li><span class="index">06</span><a href="#chart-defense-formation">ディフェンス編成別プレー回数</a></li>
      <li><span class="index">07</span><a href="#chart-play-type">プレータイプ別プレー回数</a></li>
      <li><span class="index">08</span><a href="#chart-coverage-type">カバレッジタイプ別プレー回数</a></li>
    </ol>'''

OLD_SECTION_END = '''      <p class="nfldb-legend-note">出典: nflverse(nfl_data_py)のPlay-by-Playデータを集計(集計対象: レギュラーシーズンのみ。パーソネルデータの提供開始年である2016年シーズン以降のみ集計可能)。</p>
    </div>
  </section>
</div>'''

NEW_SECTIONS = '''      <p class="nfldb-legend-note">出典: nflverse(nfl_data_py)のPlay-by-Playデータを集計(集計対象: レギュラーシーズンのみ。パーソネルデータの提供開始年である2016年シーズン以降のみ集計可能)。</p>
    </div>
  </section>

  <section class="nfldb-chart-section" id="chart-play-type">
    <h2><span class="index">07</span> プレータイプ別プレー回数</h2>
    <p class="nfldb-chart-desc">オフェンスの各プレーのプレータイプ(ラン/パス)ごとのプレー回数(試合平均/総数)のチャート。</p>

    <div class="nfldb-controls">
      <div class="nfldb-pill-group" data-role="granularity-group">
        <button type="button" class="nfldb-pill active" data-granularity="season">シーズン別</button>
        <button type="button" class="nfldb-pill" data-granularity="week">ウィーク別</button>
        <button type="button" class="nfldb-pill" data-granularity="quarter">クォーター別</button>
      </div>
      <div class="nfldb-pill-group" data-role="viewmode-group">
        <button type="button" class="nfldb-pill active" data-viewmode="avg">試合平均</button>
        <button type="button" class="nfldb-pill" data-viewmode="total">総数</button>
      </div>
      <div class="nfldb-year-range" data-role="year-range-group">
        <select class="nfldb-season-select nfldb-year-select" data-role="year-start-select" aria-label="表示開始年を選択"></select>
        <span class="nfldb-year-range-sep">〜</span>
        <select class="nfldb-season-select nfldb-year-select" data-role="year-end-select" aria-label="表示終了年を選択"></select>
      </div>
      <select class="nfldb-season-select" data-role="season-select" aria-label="シーズンを選択"></select>
    </div>

    <div class="nfldb-chart-box">
      <div class="nfldb-chart-canvas-wrap">
        <canvas id="chart-play-type-canvas" role="img" aria-label="プレータイプ別プレー回数のクロス集計チャート"></canvas>
      </div>
      <p class="nfldb-legend-note">出典: nflverse(nfl_data_py)のPlay-by-Playデータを集計(集計対象: レギュラーシーズンのみ)。</p>
    </div>
  </section>

  <section class="nfldb-chart-section" id="chart-coverage-type">
    <h2><span class="index">08</span> カバレッジタイプ別プレー回数</h2>
    <p class="nfldb-chart-desc">ディフェンスの各プレーのカバレッジタイプ(マンツーマン/ゾーン)ごとのプレー回数(試合平均/総数)のチャート。</p>

    <div class="nfldb-controls">
      <div class="nfldb-pill-group" data-role="granularity-group">
        <button type="button" class="nfldb-pill active" data-granularity="season">シーズン別</button>
        <button type="button" class="nfldb-pill" data-granularity="week">ウィーク別</button>
        <button type="button" class="nfldb-pill" data-granularity="quarter">クォーター別</button>
      </div>
      <div class="nfldb-pill-group" data-role="viewmode-group">
        <button type="button" class="nfldb-pill active" data-viewmode="avg">試合平均</button>
        <button type="button" class="nfldb-pill" data-viewmode="total">総数</button>
      </div>
      <div class="nfldb-year-range" data-role="year-range-group">
        <select class="nfldb-season-select nfldb-year-select" data-role="year-start-select" aria-label="表示開始年を選択"></select>
        <span class="nfldb-year-range-sep">〜</span>
        <select class="nfldb-season-select nfldb-year-select" data-role="year-end-select" aria-label="表示終了年を選択"></select>
      </div>
      <select class="nfldb-season-select" data-role="season-select" aria-label="シーズンを選択"></select>
    </div>

    <div class="nfldb-chart-box">
      <div class="nfldb-chart-canvas-wrap">
        <canvas id="chart-coverage-type-canvas" role="img" aria-label="カバレッジタイプ別プレー回数のクロス集計チャート"></canvas>
      </div>
      <p class="nfldb-legend-note">出典: nflverse(nfl_data_py)のPlay-by-Playデータを集計(集計対象: レギュラーシーズンのみ。カバレッジタイプデータの提供開始年である2018年シーズン以降のみ集計可能)。</p>
    </div>
  </section>
</div>'''

OLD_METRICS_TAIL = '''      unitLabel: 'プレー回数',
      ratioAxisLabel: '合計プレー回数に対する比率'
    }
  ];'''

NEW_METRICS_TAIL = '''      unitLabel: 'プレー回数',
      ratioAxisLabel: '合計プレー回数に対する比率'
    },
    {
      metricKey: 'play_type',
      sectionId: 'chart-play-type',
      canvasId: 'chart-play-type-canvas',
      categories: ['run', 'pass'],
      labels: { run: 'ラン', pass: 'パス' },
      barColors: { run: '#2e8f52', pass: '#b8860b' },
      ratioColors: { run: '#3ecf6e', pass: '#ffc633' },
      ratioDash: { run: [6, 4], pass: [6, 4] },
      unitLabel: 'プレー回数',
      ratioAxisLabel: 'ラン/パス合計プレー回数に対する比率'
    },
    {
      metricKey: 'coverage_type',
      sectionId: 'chart-coverage-type',
      canvasId: 'chart-coverage-type-canvas',
      categories: ['man', 'zone'],
      labels: { man: 'マンツーマン', zone: 'ゾーン' },
      barColors: { man: '#2e8f52', zone: '#b8860b' },
      ratioColors: { man: '#3ecf6e', zone: '#ffc633' },
      ratioDash: { man: [6, 4], zone: [6, 4] },
      unitLabel: 'プレー回数',
      ratioAxisLabel: 'マンツーマン/ゾーン合計プレー回数に対する比率'
    }
  ];'''

results = []

for slug in SLUGS:
    path = f"{REPO}/nfl-db/{slug}.html"
    with open(path, encoding="utf-8") as f:
        html = f.read()

    orig = html

    assert html.count(OLD_TOC) == 1, f"{slug}: TOC anchor not found/unique"
    html = html.replace(OLD_TOC, NEW_TOC)

    assert html.count(OLD_SECTION_END) == 1, f"{slug}: section-end anchor not found/unique"
    html = html.replace(OLD_SECTION_END, NEW_SECTIONS)

    assert html.count(OLD_METRICS_TAIL) == 1, f"{slug}: METRICS-tail anchor not found/unique"
    html = html.replace(OLD_METRICS_TAIL, NEW_METRICS_TAIL)

    # 5 wording fixes
    n1 = html.count("プレー種別")
    html = html.replace("プレー種別", "プレータイプ")
    n2 = html.count("の各プレーで採用されている")
    html = html.replace("の各プレーで採用されている", "の各プレーの")

    assert html != orig, f"{slug}: no changes applied?!"

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    results.append((slug, n1, n2))
    print(f"OK: {slug} (プレー種別 replaced x{n1}, の各プレーで採用されている replaced x{n2})")

print(f"ALL {len(SLUGS)} TEAM HTML FILES UPDATED")
