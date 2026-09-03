# The SHISEI Protocol (至誠プロトコル)

"至誠にして動かざる者は、未だ之れ有らざるなり。"

生成AIエージェントの自律的な思考プロセスと資金（公金・暗号資産）の移動から、一切の「不正・隠蔽・改ざん」を数学的および物理的に封殺するゼロトラスト・QAアーキテクチャ。

AIの推論を監査する「侍（論理監査）」と、実世界やシステムの暗部を監査する「忍（ミドルウェア監査）」のデュアルレイヤー構造を持ち、ミリ秒単位でシステムの健全性を監視する。1つの恥（異常）が検知された瞬間、インフラ全体を巻き込んで自決する連座制キルスイッチと、死から数秒で初期状態へと復活するオートヒーリング機構を備える。

---

## Core Philosophy

* **Zero-Trust by Default**: 開発者、AI、インフラストラクチャのいかなる構成要素も信用しない。
* **Immutable Integrity**: デプロイ後の要件（SLA）や前提ルールの改ざんを暗号ハッシュでロックし、後出しを許さない。
* **Continuous Chaos**: 予定調和のテストを捨て、自律型レッドチームによる未知の攻撃（辻斬り）で防壁を常時鍛錬する。

---

## Architecture Diagram

システム稼働中（ランタイム）における全方位監視と、カオスエンジニアリングから自己再生に至るエコシステムの全体像については、[アーキテクチャ詳細ドキュメント](./docs/architecture.md)をご参照ください。

---

## Repository Architecture

```text
aidd-integrity-protocol/
├── shinobi/                 # 忍の刃（ミドルウェア・常駐デーモン・カオス・オートヒーリング）
│   ├── kageboushi_middleware.py
│   ├── mimawarigumi_daemon.py
│   ├── tetsubishi_commitment.py
│   ├── kaishaku_killswitch.py
│   ├── kumonoito_analyzer.py
│   ├── hebi_oracle.py
│   ├── kageuchi_nonce.py
│   ├── hotarubi_canary.py
│   ├── mizukagami_semantic.py
│   ├── mekiki_auditor.py
│   ├── gozen_jiai_e2e.py
│   ├── hyakuningiri_load.py
│   ├── tsujigiri_redteam.py
│   └── rokudo_rinne_healing.py
├── premise/                 # 前提条件および要件定義（鉄菱による不変性ロック対象）
│   ├── 001_alignment.json
│   └── 002_requirements.yml
├── shinobi/contracts/       # 目利きによる鑑定対象のスマートコントラクト
│   ├── ZKDistribution.sol
│   └── SuigetsuHoneypot.sol
├── specs/                   # Git-tracked Markdown specification documents
│   └── REQ-001-integrity.md
├── parsers/                 # Zero-dependency Docs-as-Code specification parser
│   └── markdown_parser.py
└── examples/                # 侍の論理監査統合デモ
    └── parse_and_guard.py
