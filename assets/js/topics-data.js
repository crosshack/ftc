// ---- Topics dataset (shared) --------------------------------------------
// Single source of truth for all topics articles. Used by topics.html
// (full list + filtering) and index.html (latest 3, auto-sorted by date).
// Add new articles here; both pages pick them up automatically.
// theme: null for standalone articles, or {slug, name, part} for a series entry.
window.TOPICS_DATA = [
  {
    slug: "pattern-match-coverage-1",
    title: "なぜパターンマッチが主流になったのか",
    excerpt: "見た目はゾーンなのに、実際にはマンツーマンのように振る舞う「パターンマッチカバレッジ」。なぜ今これほど主流になっているのかを解説する。",
    url: "topics/pattern-match-coverage-1.html",
    date: "2026-08-21",
    readMin: 5,
    theme: { slug: "pattern-match-coverage", name: "パターンマッチの最前線", part: "前編" },
    tags: [
      { slug: "defense", name: "ディフェンス" },
      { slug: "coverage", name: "カバレッジ" },
      { slug: "scheme-analysis", name: "スキーム分析" }
    ],
    thumb: '<circle cx="35" cy="46" r="8" fill="none" stroke="#a8afa2" stroke-width="1.5" stroke-dasharray="3,3"/><path d="M35,38 Q35,26 35,18" fill="none" stroke="#eceee9" stroke-width="1.8" stroke-dasharray="4,3"/><circle cx="35" cy="18" r="4" fill="#eceee9"/><path d="M35,52 L35,60" fill="none" stroke="#ffc633" stroke-width="2"/><circle cx="35" cy="60" r="3.5" fill="#ffc633"/>'
  },
  {
    slug: "pattern-match-coverage-2",
    title: "パターンマッチ導入チームの実例と今後",
    excerpt: "ライトボックスを採用する実例チームと、スーパーボウルLIXでの実証、オフェンス側の対抗策を見ていく。",
    url: "topics/pattern-match-coverage-2.html",
    date: "2026-08-21",
    readMin: 5,
    theme: { slug: "pattern-match-coverage", name: "パターンマッチの最前線", part: "後編" },
    tags: [
      { slug: "defense", name: "ディフェンス" },
      { slug: "coverage", name: "カバレッジ" },
      { slug: "scheme-analysis", name: "スキーム分析" }
    ],
    thumb: '<circle cx="35" cy="46" r="8" fill="none" stroke="#a8afa2" stroke-width="1.5" stroke-dasharray="3,3"/><path d="M35,38 Q35,26 35,18" fill="none" stroke="#eceee9" stroke-width="1.8" stroke-dasharray="4,3"/><circle cx="35" cy="18" r="4" fill="#eceee9"/><path d="M35,52 L35,60" fill="none" stroke="#ffc633" stroke-width="2"/><circle cx="35" cy="60" r="3.5" fill="#ffc633"/>'
  },
  {
    slug: "presnap-motion-1",
    title: "なぜモーションがここまで増えたのか",
    excerpt: "NFL全体のプレスナップモーション使用率は、2014年の37.5%から2025年に64.0%まで上昇した。なぜここまで増えたのかを、データとともに解説する。",
    url: "topics/presnap-motion-1.html",
    date: "2026-08-21",
    readMin: 5,
    theme: { slug: "presnap-motion", name: "プレスナップモーションの浸透", part: "前編" },
    tags: [
      { slug: "offense", name: "オフェンス" },
      { slug: "defense", name: "ディフェンス" },
      { slug: "scheme-analysis", name: "スキーム分析" }
    ],
    thumb: '<line x1="8" y1="50" x2="62" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/><circle cx="45" cy="50" r="3.5" fill="#eceee9"/><path d="M45,50 L20,50" fill="none" stroke="#ffc633" stroke-width="2" stroke-dasharray="3,2"/><path d="M24,46 L18,50 L24,54" fill="none" stroke="#ffc633" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="18" cy="50" r="3.5" fill="#ffc633"/>'
  },
  {
    slug: "presnap-motion-2",
    title: "プレスナップモーションへの対応と今後の攻防",
    excerpt: "セーフティのポストスナップ移動やカバレッジの偽装、DBのクロストレーニングなど、プレスナップモーションに対するディフェンス側の対応を解説する。",
    url: "topics/presnap-motion-2.html",
    date: "2026-08-21",
    readMin: 5,
    theme: { slug: "presnap-motion", name: "プレスナップモーションの浸透", part: "後編" },
    tags: [
      { slug: "offense", name: "オフェンス" },
      { slug: "defense", name: "ディフェンス" },
      { slug: "scheme-analysis", name: "スキーム分析" }
    ],
    thumb: '<line x1="8" y1="50" x2="62" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/><circle cx="45" cy="50" r="3.5" fill="#eceee9"/><path d="M45,50 L20,50" fill="none" stroke="#ffc633" stroke-width="2" stroke-dasharray="3,2"/><path d="M24,46 L18,50 L24,54" fill="none" stroke="#ffc633" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="18" cy="50" r="3.5" fill="#ffc633"/>'
  },
  {
    slug: "13-personnel-1",
    title: "なぜ13パーソネルが台頭したのか",
    excerpt: "ラムズを震源地に急増した「13パーソネル」。かつて保守的とされた隊形が、なぜ攻撃的な武器として台頭したのかを解説する。",
    url: "topics/13-personnel-1.html",
    date: "2026-08-21",
    readMin: 5,
    theme: { slug: "13-personnel", name: "13パーソネルの台頭", part: "前編" },
    tags: [
      { slug: "offense", name: "オフェンス" },
      { slug: "defense", name: "ディフェンス" },
      { slug: "scheme-analysis", name: "スキーム分析" }
    ],
    thumb: '<line x1="8" y1="50" x2="62" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/><circle cx="20" cy="50" r="3.5" fill="#ffc633"/><circle cx="30" cy="50" r="3.5" fill="#ffc633"/><circle cx="40" cy="50" r="3.5" fill="#ffc633"/><circle cx="55" cy="50" r="3.5" fill="#eceee9"/><circle cx="30" cy="60" r="3.5" fill="#eceee9"/>'
  },
  {
    slug: "13-personnel-2",
    title: "13パーソネルへの対応と今後の展望",
    excerpt: "ベースパッケージ回帰やビッグニッケルの台頭など、13パーソネルの急増に対するディフェンス側の対応と、今後の展望を解説する。",
    url: "topics/13-personnel-2.html",
    date: "2026-08-21",
    readMin: 5,
    theme: { slug: "13-personnel", name: "13パーソネルの台頭", part: "後編" },
    tags: [
      { slug: "offense", name: "オフェンス" },
      { slug: "defense", name: "ディフェンス" },
      { slug: "scheme-analysis", name: "スキーム分析" }
    ],
    thumb: '<line x1="8" y1="50" x2="62" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/><circle cx="20" cy="50" r="3.5" fill="#ffc633"/><circle cx="30" cy="50" r="3.5" fill="#ffc633"/><circle cx="40" cy="50" r="3.5" fill="#ffc633"/><circle cx="55" cy="50" r="3.5" fill="#eceee9"/><circle cx="30" cy="60" r="3.5" fill="#eceee9"/>'
  }
  ,
  {
    slug: "real-play-explained-001",
    title: "ジャガーズを2週連続で沈めた、13パーソネルの1プレー",
    excerpt: "2025年シーズンWeek 7、ラムズ対ジャガーズ。4th-and-1で見せたプレーアクションの1本を、フォーメーションから結果まで解説する。",
    url: "topics/real-play-explained-001.html",
    date: "2026-08-26",
    readMin: 5,
    theme: { slug: "real-play-explained", name: "実戦プレー解説", part: "#001" },
    tags: [
      { slug: "offense", name: "オフェンス" },
      { slug: "scheme-analysis", name: "スキーム分析" },
      { slug: "play-breakdown", name: "実戦分析" }
    ],
    thumb: '<circle cx="35" cy="35" r="16" fill="none" stroke="#a8afa2" stroke-width="1.5" stroke-dasharray="3,3"/><line x1="46" y1="46" x2="58" y2="58" stroke="#a8afa2" stroke-width="2" stroke-linecap="round"/><circle cx="30" cy="38" r="3.5" fill="#eceee9"/><path d="M30,38 L40,28" stroke="#ffc633" stroke-width="2" stroke-linecap="round"/><circle cx="40" cy="28" r="3.5" fill="#ffc633"/>'
  },
  {
    slug: "real-play-explained-002",
    title: "無名ルーキーが「一週間前から知っていた」インターセプト",
    excerpt: "第49回スーパーボウル終盤、無名の新人CBマルコム・バトラーが見せたゴールラインインターセプト。土壇場の判断ではなく、直前の練習で叩き込まれた予習がどう結果に結びついたかを解説する。",
    url: "topics/real-play-explained-002.html",
    date: "2026-08-26",
    readMin: 5,
    theme: { slug: "real-play-explained", name: "実戦プレー解説", part: "#002" },
    tags: [
      { slug: "defense", name: "ディフェンス" },
      { slug: "game-management", name: "ゲームマネジメント" },
      { slug: "play-breakdown", name: "実戦分析" }
    ],
    thumb: '<circle cx="35" cy="35" r="16" fill="none" stroke="#a8afa2" stroke-width="1.5" stroke-dasharray="3,3"/><line x1="46" y1="46" x2="58" y2="58" stroke="#a8afa2" stroke-width="2" stroke-linecap="round"/><circle cx="30" cy="38" r="3.5" fill="#eceee9"/><path d="M30,38 L40,28" stroke="#ffc633" stroke-width="2" stroke-linecap="round"/><circle cx="40" cy="28" r="3.5" fill="#ffc633"/>'
  }
  ,
  {
    slug: "real-play-explained-003",
    title: "OLの「クセ」を読み切っていた、第1Qのコーナーブリッツ",
    excerpt: "第60回スーパーボウル第1Q、デヴォン・ウィザースプーンのコーナーブリッツによる10ヤードサック。ルーキー2人が並ぶペイトリオッツのオフェンスラインに、シーホークスは何を読み切っていたのかを解説する。",
    url: "topics/real-play-explained-003.html",
    date: "2026-08-26",
    readMin: 5,
    theme: { slug: "real-play-explained", name: "実戦プレー解説", part: "#003" },
    tags: [
      { slug: "defense", name: "ディフェンス" },
      { slug: "scheme-analysis", name: "スキーム分析" },
      { slug: "play-breakdown", name: "実戦分析" }
    ],
    thumb: '<circle cx="35" cy="35" r="16" fill="none" stroke="#a8afa2" stroke-width="1.5" stroke-dasharray="3,3"/><line x1="46" y1="46" x2="58" y2="58" stroke="#a8afa2" stroke-width="2" stroke-linecap="round"/><circle cx="30" cy="38" r="3.5" fill="#eceee9"/><path d="M30,38 L40,28" stroke="#ffc633" stroke-width="2" stroke-linecap="round"/><circle cx="40" cy="28" r="3.5" fill="#ffc633"/>'
  }
];
