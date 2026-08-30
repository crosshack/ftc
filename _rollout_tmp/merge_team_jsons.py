# -*- coding: utf-8 -*-
import json
import sys

REPO = sys.argv[1]  # repo root path on the Mac

TEAM_SLUG_TO_CODE = {
    "arizona-cardinals": "ARI", "atlanta-falcons": "ATL", "baltimore-ravens": "BAL",
    "buffalo-bills": "BUF", "carolina-panthers": "CAR", "chicago-bears": "CHI",
    "cincinnati-bengals": "CIN", "cleveland-browns": "CLE", "dallas-cowboys": "DAL",
    "denver-broncos": "DEN", "detroit-lions": "DET", "green-bay-packers": "GB",
    "houston-texans": "HOU", "indianapolis-colts": "IND", "jacksonville-jaguars": "JAX",
    "kansas-city-chiefs": "KC", "las-vegas-raiders": "LV", "los-angeles-chargers": "LAC",
    "los-angeles-rams": "LA", "miami-dolphins": "MIA", "minnesota-vikings": "MIN",
    "new-orleans-saints": "NO", "new-york-giants": "NYG", "new-york-jets": "NYJ",
    "philadelphia-eagles": "PHI", "pittsburgh-steelers": "PIT", "san-francisco-49ers": "SF",
    "seattle-seahawks": "SEA", "tampa-bay-buccaneers": "TB", "tennessee-titans": "TEN",
    "washington-commanders": "WAS",
}
# NOTE: new-england-patriots intentionally excluded -- already has these metrics deployed.

PLAY_TYPE_NOTE = (
    "total=run+pass+other。other=ラン/パス以外のスクリメージ関連スナップ"
    "(ニーダウン・スパイク・ノープレー〈スナップ前反則等による無効試行〉)の合計。"
    "パント/キックオフ/FG/PAT等の特別チームスナップは対象外。"
    "オフェンス側(自チームのプレーコール)の集計。"
)
COVERAGE_TYPE_NOTE = (
    "nflverseのdefense_man_zone_typeフィールド(NFL Next Gen Stats/2023年以降はFTN社チャート提供)"
    "が実際に値を持つ2018年シーズン以降のみ集計可能"
    "(2016・2017年シーズンはフィールド自体は存在するが値が全件欠測のためデータなし)。"
    "集計対象は相手オフェンスのスクリメージプレー(ラン/パス)のみ、レギュラーシーズン限定"
    "(defense_formationと同一のプレー母集団)。"
    "マンツーマン=defense_man_zone_typeがMAN_COVERAGE、ゾーン=同ZONE_COVERAGEのプレー。"
    "その他=上記2つに該当しないプレーで、その大半はランプレー"
    "(コンセプト上マン/ゾーンの区分がチャートされない)であり、"
    "残りはパスプレーのうちNGS/FTNのチャートでカバレッジ種別が判定されなかったもの。"
    "ディフェンス側(相手オフェンスに対する自チームの守備)の集計。"
)

COVERAGE_SEASONS = [str(y) for y in range(2018, 2026)]


def main():
    with open(f"{REPO}/_rollout_tmp/rollout_team_playtype.json", encoding="utf-8") as f:
        rollout_pt = json.load(f)
    with open(f"{REPO}/_rollout_tmp/rollout_team_coverage.json", encoding="utf-8") as f:
        rollout_cov = json.load(f)

    for slug, code in TEAM_SLUG_TO_CODE.items():
        path = f"{REPO}/assets/data/nfl-db/{slug}.json"
        with open(path, encoding="utf-8") as f:
            d = json.load(f)

        team_seasons_covered = d["seasons_covered"]

        pt_data = rollout_pt[code]
        cov_data = rollout_cov[code]

        d["metrics"]["play_type"] = {
            "label": "プレータイプ別プレー回数",
            "unit": "plays",
            "seasons_covered": team_seasons_covered,
            "note": PLAY_TYPE_NOTE,
            "by_season": pt_data["by_season"],
            "by_week": pt_data["by_week"],
            "by_quarter": pt_data["by_quarter"],
        }
        d["metrics"]["coverage_type"] = {
            "label": "カバレッジタイプ別プレー回数",
            "unit": "plays",
            "seasons_covered": COVERAGE_SEASONS,
            "note": COVERAGE_TYPE_NOTE,
            "by_season": cov_data["by_season"],
            "by_week": cov_data["by_week"],
            "by_quarter": cov_data["by_quarter"],
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)

        print(f"OK: {slug} ({code}) merged")

    print("ALL TEAM JSONS MERGED")


if __name__ == "__main__":
    main()
