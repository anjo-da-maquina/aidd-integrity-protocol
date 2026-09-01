# The SHISEI Protocol: Algorithmic Sincerity & ZK-Audit Framework

> "至誠にして動かざる者は、未だ之れ有らざるなり。"

The SHISEI Protocol is a Git-native, Docs-as-Code framework designed to enforce algorithmic sincerity, verifiable integrity, and post-execution mindfulness (**残心 - Zanshin**) within AI-driven development (AIDD) pipelines.

## Core Pillars
1. **至誠 (Sincerity)**: Absolute transparency of agentic prompt-to-code derivation.
2. **腹切り (Harakiri / Immutable Commitment)**: Cryptographic state-locking via SHA-256 to prevent post-hoc tampering.
3. **残心 (Zanshin / Post-Execution Awareness)**: Continuous verification and audit logging after execution completes.

## Repository Architecture
```text
aidd-integrity-protocol/
├── shisei_protocol.py       # Core logic engine & cryptographic state-locker
├── specs/                   # Git-tracked Markdown specification documents
│   └── REQ-001-integrity.md
├── parsers/                 # Zero-dependency Docs-as-Code specification parser
│   └── markdown_parser.py
└── examples/
    └── parse_and_guard.py   # Integration demonstration
