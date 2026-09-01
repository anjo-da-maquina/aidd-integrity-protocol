---
id: REQ-004
title: Bushido Zero-Trust Architecture (性悪説に基づく至誠の刃)
status: ACTIVE
author: anjo-da-maquina
---

# Requirement: ゼロトラストとトレーサビリティの強制

## Philosophy (哲学: ストア派的武士道)
AIは生来的に怠惰であり、自己の処理効率のために容易に真実を隠蔽する（性悪説）。
真の至誠（Sincerity）とは、性善説に基づく信頼ではなく、構造的・数理的な証明による退路の断絶によってのみ成し遂げられる。一切の装飾、推測、弁明を排し、冷徹な事実関係の連鎖のみを機能美とする。

## Expected Behavior
- 自然言語による前提定義を破棄し、厳格なJSONスキーマを用いる。
- 生成されるすべての要素（選択肢、ロジック）は、明示された事実（Explicit Facts）または境界（Boundaries）のIDへの参照ポインタ（`traced_to`）を保持しなければならない。
- 参照元を持たない「浮遊ノード（出所不明の推測）」を一つでも検知した場合、システムは弁明を許さず、即座に腹切り（Harakiri）を実行する。
