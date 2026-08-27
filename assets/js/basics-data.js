// ---- Basics (基礎知識) dataset (shared) -----------------------------------
// Single source of truth for all basics.html cards, grouped by section.
// tags: reserved for future glossary-term hashtags (Phase 3), empty for now.
window.BASICS_DATA = [
  {
    id: 'offense-basics',
    label: 'オフェンス',
    entries: [
    {
      slug: 'offense-positions',
      url: 'basics/offense-positions.html',
      title: 'オフェンスポジションの基礎',
      excerpt: '11人はそれぞれ何をしているか ― QB・RB・WR・TE・OLの役割を解説。',
      readMin: 9,
      tags: [],
      thumb: '<line x1="0" y1="26" x2="70" y2="26" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="25" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="35" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="45" cy="26" r="3.5" fill="#3ecf6e"/>
          <circle cx="10" cy="26" r="3.5" fill="#ffc633"/><circle cx="60" cy="26" r="3.5" fill="#ffc633"/>
          <circle cx="35" cy="34" r="3.5" fill="#eceee9"/><circle cx="35" cy="42" r="3.5" fill="#eceee9"/>'
    },
    {
      slug: 'offense-formations',
      url: 'basics/offense-formations.html',
      title: 'オフェンスフォーメーションの基礎',
      excerpt: '選手配置は何を語るか ― パーソネル、バックフィールドとレシーバーの型を解説。',
      readMin: 7,
      tags: [],
      thumb: '<line x1="0" y1="26" x2="70" y2="26" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="25" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="35" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="45" cy="26" r="3.5" fill="#3ecf6e"/>
          <circle cx="10" cy="26" r="3.5" fill="#ffc633"/><circle cx="60" cy="26" r="3.5" fill="#ffc633"/>
          <circle cx="31" cy="34" r="3.5" fill="#eceee9"/><circle cx="41" cy="38" r="3.5" fill="#eceee9"/>'
    },
    {
      slug: 'offense-assignment',
      url: 'basics/offense-assignment.html',
      title: 'オフェンスアサイメントの基礎',
      excerpt: '守備の配置をどう読み、崩すか ― オフェンスのアライメント、アサイメントの基本を解説。',
      readMin: 8,
      tags: [],
      thumb: '<line x1="0" y1="26" x2="70" y2="26" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="25" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="35" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="45" cy="26" r="3.5" fill="#3ecf6e"/>
          <circle cx="16" cy="26" r="3.5" fill="#ffc633"/>
          <circle cx="63" cy="26" r="3.5" fill="#ffc633"/>
          <path d="M45,26 L63,26" stroke="#ffc633" stroke-width="1" stroke-dasharray="1,2"/>
          <circle cx="35" cy="42" r="3.5" fill="#eceee9"/>'
    },
    {
      slug: 'offense-play-types',
      url: 'basics/offense-play-types.html',
      title: 'プレータイプの基礎',
      excerpt: 'プレーの種類はどう分類されるか ― ランとパスのプレータイプを解説。',
      readMin: 6,
      tags: [],
      thumb: '<line x1="0" y1="55" x2="70" y2="55" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="20" cy="55" r="3.5" fill="#eceee9"/>
          <path d="M20,55 L45,55" fill="none" stroke="#3ecf6e" stroke-width="2" stroke-linecap="round" marker-end="url(#arrowRunCard)"/>
          <path d="M20,55 Q35,15 55,20" fill="none" stroke="#ffc633" stroke-width="2" stroke-linecap="round" marker-end="url(#arrowPassCard)"/>
          <defs>
            <marker id="arrowRunCard" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#3ecf6e"/></marker>
            <marker id="arrowPassCard" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffc633"/></marker>
          </defs>'
    },
    {
      slug: 'offense-run-basics',
      url: 'basics/offense-run-basics.html',
      title: 'ランオフェンスの基礎',
      excerpt: 'RBをフリーにする条件 ― ホールを作る技術、ホールの作り方を解説。',
      readMin: 7,
      tags: [],
      thumb: '<line x1="0" y1="20" x2="70" y2="20" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <rect x="14" y="19" width="10" height="10" fill="#3d4238"/>
          <rect x="28" y="19" width="10" height="10" fill="#3d4238"/>
          <rect x="42" y="19" width="10" height="10" fill="#3d4238"/>
          <circle cx="33" cy="47" r="4" fill="#eceee9"/>
          <path d="M33,47 L33,25" stroke="#3ecf6e" stroke-width="2" stroke-linecap="round" marker-end="url(#runBasicsCardArrow)"/>
          <defs>
            <marker id="runBasicsCardArrow" markerWidth="8" markerHeight="8" refX="3" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#3ecf6e"/></marker>
          </defs>'
    },
    {
      slug: 'offense-pass-basics',
      url: 'basics/offense-pass-basics.html',
      title: 'パスオフェンスの基礎',
      excerpt: 'レシーバーをオープンにする条件 ― セパレーションを作る技術、QBを守る方法を解説。',
      readMin: 8,
      tags: [],
      thumb: '<line x1="0" y1="55" x2="70" y2="55" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="20" cy="50" r="3.5" fill="#eceee9"/>
          <path d="M20,50 L20,20" stroke="#ffc633" stroke-width="1.8" stroke-linecap="round" fill="none" marker-end="url(#passBasicsCardA)"/>
          <path d="M20,50 L45,50 L52,28" stroke="#ffc633" stroke-width="1.8" fill="none" stroke-linecap="round" marker-end="url(#passBasicsCardB)"/>
          <defs>
            <marker id="passBasicsCardA" markerWidth="8" markerHeight="8" refX="3" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffc633"/></marker>
            <marker id="passBasicsCardB" markerWidth="8" markerHeight="8" refX="3" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffc633"/></marker>
          </defs>'
    },
    {
      slug: 'offense-play-selection',
      url: 'basics/offense-play-selection.html',
      title: 'プレー選択とプレスナップリードの基礎',
      excerpt: 'スナップ前に結果は半分決まる ― 何がプレーを決めるのか、スナップ前に何を読むのかを解説。',
      readMin: 8,
      tags: [],
      thumb: '<circle cx="35" cy="52" r="3.5" fill="#eceee9"/>
          <path d="M20,52 A15,15 0 0 1 50,52" fill="none" stroke="#3ecf6e" stroke-width="1" opacity="0.5"/>
          <path d="M25,52 A10,10 0 0 1 45,52" fill="none" stroke="#3ecf6e" stroke-width="1" opacity="0.4"/>
          <circle cx="46" cy="24" r="4" fill="none" stroke="#ffc633" stroke-width="1.4"/>
          <circle cx="46" cy="24" r="1.8" fill="#ffc633"/>'
    }
    ]
  },
  {
    id: 'defense-basics',
    label: 'ディフェンス',
    entries: [
    {
      slug: 'defense-positions',
      url: 'basics/defense-positions.html',
      title: 'ディフェンスポジションの基礎',
      excerpt: '11人はそれぞれ何をしているか ― DL・LB・DBの役割を解説。',
      readMin: 9,
      tags: [],
      thumb: '<line x1="0" y1="50" x2="70" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="20" cy="42" r="3.5" fill="#3ecf6e"/><circle cx="35" cy="42" r="3.5" fill="#3ecf6e"/><circle cx="50" cy="42" r="3.5" fill="#3ecf6e"/>
          <circle cx="27" cy="30" r="3.5" fill="#eceee9"/><circle cx="43" cy="30" r="3.5" fill="#eceee9"/>
          <circle cx="10" cy="42" r="3.5" fill="#ffc633"/><circle cx="60" cy="42" r="3.5" fill="#ffc633"/>'
    },
    {
      slug: 'defense-formations',
      url: 'basics/defense-formations.html',
      title: 'ディフェンスフォーメーションの基礎',
      excerpt: '選手配置は何を語るか ― 4-3・3-4などフロントの組み方の基本を解説。',
      readMin: 7,
      tags: [],
      thumb: '<line x1="0" y1="50" x2="70" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="20" cy="42" r="3.5" fill="#3ecf6e"/><circle cx="35" cy="42" r="3.5" fill="#3ecf6e"/><circle cx="50" cy="42" r="3.5" fill="#3ecf6e"/>
          <circle cx="27" cy="27" r="3.5" fill="#eceee9"/><circle cx="43" cy="27" r="3.5" fill="#eceee9"/>
          <circle cx="10" cy="38" r="3.5" fill="#ffc633"/><circle cx="60" cy="38" r="3.5" fill="#ffc633"/>'
    },
    {
      slug: 'defense-assignment',
      url: 'basics/defense-assignment.html',
      title: 'ディフェンスアサイメントの基礎',
      excerpt: 'どこに立ち、何を守るか ― ディフェンスのアライメント、アサイメントの基本を解説。',
      readMin: 9,
      tags: [],
      thumb: '<line x1="0" y1="46" x2="70" y2="46" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <rect x="21" y="41" width="9" height="9" fill="#a8afa2" rx="1"/>
          <rect x="33" y="41" width="9" height="9" fill="#a8afa2" rx="1"/>
          <rect x="45" y="41" width="9" height="9" fill="#a8afa2" rx="1"/>
          <line x1="27" y1="38" x2="27" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="1,2"/>
          <line x1="39" y1="38" x2="39" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="1,2"/>
          <circle cx="14" cy="33" r="3.5" fill="#3ecf6e"/>
          <circle cx="26" cy="30" r="3.5" fill="#3ecf6e"/>
          <circle cx="40" cy="30" r="3.5" fill="#3ecf6e"/>
          <circle cx="54" cy="33" r="3.5" fill="#3ecf6e"/>
          <circle cx="33" cy="17" r="3.5" fill="#eceee9"/>'
    },
    {
      slug: 'defense-coverage-basics',
      url: 'basics/defense-coverage-basics.html',
      title: 'カバレッジの基礎',
      excerpt: '11人でパスを封じる設計図 ― マンツーマンとゾーン、カバレッジのパターンを解説。',
      readMin: 10,
      tags: [],
      thumb: '<path d="M8,50 Q35,15 62,50" fill="rgba(62,207,110,0.12)" stroke="#3ecf6e" stroke-width="1.5"/>
          <path d="M8,50 Q35,58 62,50" fill="rgba(30,136,229,0.12)" stroke="#1e88e5" stroke-width="1.5"/>
          <circle cx="35" cy="50" r="3" fill="#eceee9"/>'
    },
    {
      slug: 'defense-run-basics',
      url: 'basics/defense-run-basics.html',
      title: 'ランディフェンスの基礎',
      excerpt: 'RBを止める条件 ― ラン・フィット、シェディング、タックリングを解説。',
      readMin: 7,
      tags: [],
      thumb: '<rect x="12" y="40" width="11" height="11" fill="#a8afa2" rx="1"/>
          <rect x="30" y="40" width="11" height="11" fill="#a8afa2" rx="1"/>
          <rect x="48" y="40" width="11" height="11" fill="#a8afa2" rx="1"/>
          <circle cx="26" cy="16" r="5" fill="#eceee9"/>
          <path d="M26,21 L26,38" stroke="#3ecf6e" stroke-width="2" stroke-linecap="round" marker-end="url(#runDefCardArrow)"/>
          <circle cx="44" cy="16" r="5" fill="#eceee9"/>
          <path d="M44,21 L44,38" stroke="#3ecf6e" stroke-width="2" stroke-linecap="round" marker-end="url(#runDefCardArrow)"/>
          <defs>
            <marker id="runDefCardArrow" markerWidth="8" markerHeight="8" refX="3" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#3ecf6e"/></marker>
          </defs>'
    },
    {
      slug: 'defense-pass-basics',
      url: 'basics/defense-pass-basics.html',
      title: 'パスディフェンスの基礎',
      excerpt: 'レシーバーをオープンにさせない条件 ― カバレッジの方式、パスラッシュの技術を解説。',
      readMin: 8,
      tags: [],
      thumb: '<line x1="0" y1="58" x2="70" y2="58" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="16" cy="56" r="4" fill="#a8afa2"/>
          <path d="M16,56 C24,40 32,26 42,12" stroke="#a8afa2" stroke-width="1.6" stroke-dasharray="2,3" stroke-linecap="round" fill="none" marker-end="url(#passDefCardB)"/>
          <circle cx="24" cy="54" r="4" fill="#eceee9"/>
          <path d="M24,54 C32,38 40,24 50,14" stroke="#ffc633" stroke-width="1.8" stroke-linecap="round" fill="none" marker-end="url(#passDefCardA)"/>
          <defs>
            <marker id="passDefCardA" markerWidth="8" markerHeight="8" refX="3" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffc633"/></marker>
            <marker id="passDefCardB" markerWidth="6" markerHeight="6" refX="2" refY="2" orient="auto"><path d="M0,0 L4,2 L0,4 Z" fill="#a8afa2"/></marker>
          </defs>'
    },
    {
      slug: 'defense-situational-basics',
      url: 'basics/defense-situational-basics.html',
      title: 'ディフェンスの状況判断の基礎',
      excerpt: '攻撃を読み、守り方を選ぶ ― 攻撃を読み、守り方を選ぶプロセスを解説。',
      readMin: 8,
      tags: [],
      thumb: '<line x1="0" y1="50" x2="70" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="35" cy="42" r="3.5" fill="#eceee9"/>
          <path d="M35,42 L20,20" stroke="#a8afa2" stroke-width="1" stroke-dasharray="2,3"/>
          <path d="M35,42 L50,22" stroke="#a8afa2" stroke-width="1" stroke-dasharray="2,3"/>
          <circle cx="20" cy="20" r="3" fill="none" stroke="#ffc633" stroke-width="1.3"/>
          <circle cx="50" cy="22" r="3" fill="none" stroke="#ffc633" stroke-width="1.3"/>'
    }
    ]
  },
  {
    id: 'special-teams-basics',
    label: 'スペシャルチーム',
    entries: [
    {
      slug: 'special-teams-positions',
      url: 'basics/special-teams-positions.html',
      title: 'スペシャルチームポジションの基礎',
      excerpt: '蹴る・返す・支える11人 ― キッカー・パンター・リターナーなどの役割を解説。',
      readMin: 7,
      tags: [],
      thumb: '<line x1="0" y1="50" x2="70" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="20" cy="42" r="3.5" fill="#ffc633"/><circle cx="35" cy="42" r="3.5" fill="#ffc633"/><circle cx="50" cy="42" r="3.5" fill="#ffc633"/>
          <circle cx="27" cy="30" r="3.5" fill="#eceee9"/><circle cx="43" cy="30" r="3.5" fill="#eceee9"/>
          <circle cx="10" cy="42" r="3.5" fill="#a8afa2"/><circle cx="60" cy="42" r="3.5" fill="#a8afa2"/>'
    },
    {
      slug: 'special-teams-field-goal-basics',
      url: 'basics/special-teams-field-goal-basics.html',
      title: 'フィールドゴールの基礎',
      excerpt: '確実に3点を取る条件 ― キッカーを助ける要素、プロテクションの仕組みを解説。',
      readMin: 7,
      tags: [],
      thumb: '<line x1="0" y1="58" x2="70" y2="58" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="14" cy="54" r="4" fill="#eceee9"/>
          <path d="M14,54 Q32,10 55,18" stroke="#ffc633" stroke-width="1.8" stroke-linecap="round" fill="none" marker-end="url(#fgCardArrow)"/>
          <path d="M55,50 L55,32 M46,32 L64,32 M46,32 L46,6 M64,32 L64,6" stroke="#a8afa2" stroke-width="2" fill="none" stroke-linecap="round"/>
          <defs>
            <marker id="fgCardArrow" markerWidth="7" markerHeight="7" refX="2.5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="#ffc633"/></marker>
          </defs>'
    },
    {
      slug: 'special-teams-kickoff-basics',
      url: 'basics/special-teams-kickoff-basics.html',
      title: 'キックオフの基礎',
      excerpt: '再開位置を優位にする条件 ― 蹴る深さとカバレッジを解説。',
      readMin: 6,
      tags: [],
      thumb: '<line x1="0" y1="58" x2="70" y2="58" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="10" cy="54" r="4" fill="#eceee9"/>
          <path d="M10,54 Q40,4 62,24" stroke="#ffc633" stroke-width="1.8" stroke-linecap="round" fill="none" marker-end="url(#koCardArrow)"/>
          <line x1="66" y1="6" x2="66" y2="58" stroke="#a8afa2" stroke-width="1.5" stroke-dasharray="2,2"/>
          <defs>
            <marker id="koCardArrow" markerWidth="7" markerHeight="7" refX="2.5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="#ffc633"/></marker>
          </defs>'
    },
    {
      slug: 'special-teams-punt-basics',
      url: 'basics/special-teams-punt-basics.html',
      title: 'パントの基礎',
      excerpt: '再開位置を優位にする条件 ― 届ける技術とプロテクションを解説。',
      readMin: 7,
      tags: [],
      thumb: '<line x1="0" y1="58" x2="70" y2="58" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="14" cy="54" r="4" fill="#eceee9"/>
          <path d="M14,54 Q42,10 58,46" stroke="#ffc633" stroke-width="1.8" stroke-linecap="round" fill="none" marker-end="url(#puntCardArrow)"/>
          <line x1="62" y1="6" x2="62" y2="58" stroke="#a8afa2" stroke-width="1.5" stroke-dasharray="2,2"/>
          <defs>
            <marker id="puntCardArrow" markerWidth="7" markerHeight="7" refX="2.5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="#ffc633"/></marker>
          </defs>'
    },
    {
      slug: 'special-teams-return-basics',
      url: 'basics/special-teams-return-basics.html',
      title: 'リターンの基礎',
      excerpt: '再開位置を優位にする条件 ― ブロッキングとリターナーの技術を解説。',
      readMin: 5,
      tags: [],
      thumb: '<line x1="0" y1="58" x2="70" y2="58" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="14" cy="54" r="4" fill="#eceee9"/>
          <path d="M14,54 C14,30 46,34 46,8" stroke="#3ecf6e" stroke-width="1.8" stroke-linecap="round" fill="none" marker-end="url(#retCardArrow)"/>
          <defs>
            <marker id="retCardArrow" markerWidth="7" markerHeight="7" refX="2.5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="#3ecf6e"/></marker>
          </defs>'
    }
    ]
  }
];
