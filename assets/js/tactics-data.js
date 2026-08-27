// ---- Tactics (戦術まとめ) dataset (shared) ---------------------------------
// Single source of truth for all tactics.html cards, grouped by section.
// tags: reserved for future glossary-term hashtags (Phase 3), empty for now.
window.TACTICS_DATA = [
  {
    id: 'offense-tactics',
    label: 'オフェンス',
    entries: [
    {
      slug: 'offense-formations',
      url: 'tactics/offense-formations.html',
      title: 'オフェンスフォーメーションまとめ',
      excerpt: 'シングルバック、ショットガン、アイフォーメーションなどの代表的なオフェンスフォーメーションを、 パーソネルとフィールド図つきで解説。',
      meta: '全12フォーメーション',
      tags: [],
      thumb: '<line x1="0" y1="26" x2="70" y2="26" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="25" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="35" cy="26" r="3.5" fill="#3ecf6e"/><circle cx="45" cy="26" r="3.5" fill="#3ecf6e"/>
          <circle cx="10" cy="26" r="3.5" fill="#ffc633"/><circle cx="60" cy="26" r="3.5" fill="#ffc633"/>
          <circle cx="31" cy="34" r="3.5" fill="#eceee9"/><circle cx="41" cy="38" r="3.5" fill="#eceee9"/>'
    },
    {
      slug: 'offense-run',
      url: 'tactics/offense-run.html',
      title: 'ランコンセプトまとめ',
      excerpt: 'インサイド・ゾーン、アウトサイド・ゾーン、パワーなどの代表的なランコンセプトを、 ブロッキング図とアサイメント表つきで解説。',
      meta: '全6コンセプト',
      tags: [],
      thumb: '<line x1="0" y1="50" x2="70" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="35" cy="50" r="3.5" fill="#eceee9"/>
          <path d="M35,50 L20,40" stroke="#424242" stroke-width="4" stroke-linecap="round"/>
          <path d="M35,50 L50,40" stroke="#1e88e5" stroke-width="4" stroke-linecap="round"/>
          <path d="M35,50 L35,20" stroke="#e53935" stroke-width="2" fill="none"/>'
    },
    {
      slug: 'offense-pass',
      url: 'tactics/offense-pass.html',
      title: 'パスコンセプトまとめ',
      excerpt: 'フォー・バーティカルズ、レベルズ、ダガーなどの代表的なパスコンセプトを、 フィールド図とルート表つきで解説。',
      meta: '全12コンセプト',
      tags: [],
      thumb: '<line x1="0" y1="55" x2="70" y2="55" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="14" cy="55" r="3" fill="#eceee9"/><circle cx="32" cy="55" r="3" fill="#eceee9"/><circle cx="50" cy="55" r="3" fill="#eceee9"/>
          <path d="M14,55 L8,10" stroke="#e53935" stroke-width="2" fill="none"/>
          <path d="M32,55 L34,12" stroke="#1e88e5" stroke-width="2" fill="none"/>
          <path d="M50,55 L54,18" stroke="#8e24aa" stroke-width="2" fill="none"/>'
    },
    {
      slug: 'offense-rpo',
      url: 'tactics/offense-rpo.html',
      title: 'RPOコンセプトまとめ',
      excerpt: 'バブル、スティック、グランスなどの代表的なRPOコンセプトを、 読みのキーとなるディフェンダーつきで解説。',
      meta: '全6コンセプト',
      tags: [],
      thumb: '<line x1="0" y1="50" x2="70" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="35" cy="50" r="3.5" fill="#eceee9"/>
          <path d="M35,50 L20,40" stroke="#424242" stroke-width="4" stroke-linecap="round"/>
          <path d="M35,50 L35,20" stroke="#e53935" stroke-width="2" fill="none"/>
          <path d="M35,50 L50,32" stroke="#1e88e5" stroke-width="2.4" fill="none"/>
          <circle cx="50" cy="32" r="6" fill="none" stroke="#ffc633" stroke-width="1.4" stroke-dasharray="2,2"/>'
    }
    ]
  },
  {
    id: 'defense-tactics',
    label: 'ディフェンス',
    entries: [
    {
      slug: 'defense-formations',
      url: 'tactics/defense-formations.html',
      title: 'ディフェンスフォーメーションまとめ',
      excerpt: 'ベース3-4、ベース4-3、ニッケル4-2-5などの代表的なディフェンスフォーメーションを、 カバレッジとの組み合わせでフィールド図つきで解説。',
      meta: '全12パターン',
      tags: [],
      thumb: '<line x1="0" y1="50" x2="70" y2="50" stroke="#3d4238" stroke-width="1" stroke-dasharray="2,4"/>
          <circle cx="20" cy="42" r="3.5" fill="#3ecf6e"/><circle cx="35" cy="42" r="3.5" fill="#3ecf6e"/><circle cx="50" cy="42" r="3.5" fill="#3ecf6e"/>
          <circle cx="27" cy="27" r="3.5" fill="#eceee9"/><circle cx="43" cy="27" r="3.5" fill="#eceee9"/>
          <circle cx="10" cy="38" r="3.5" fill="#ffc633"/><circle cx="60" cy="38" r="3.5" fill="#ffc633"/>'
    },
    {
      slug: 'defense-coverages',
      url: 'tactics/defense-coverages.html',
      title: 'カバレッジまとめ',
      excerpt: 'カバー1、カバー2、カバー3などの代表的なマン・ゾーンカバレッジを、 担当するマッチアップ・ゾーンがわかるフィールド図つきで解説。',
      meta: '全12カバレッジ',
      tags: [],
      thumb: '<path d="M8,50 Q35,15 62,50" fill="rgba(62,207,110,0.12)" stroke="#3ecf6e" stroke-width="1.5"/>
          <path d="M8,50 Q35,58 62,50" fill="rgba(30,136,229,0.12)" stroke="#1e88e5" stroke-width="1.5"/>
          <circle cx="35" cy="50" r="3" fill="#eceee9"/>'
    }
    ]
  }
];
