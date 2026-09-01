"""
Integration Example: Docs-as-Code + Zero-Trust Engine
"""

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
if sys.path[0] != str(root_dir):
    sys.path.insert(0, str(root_dir))

from shisei_protocol import ShiseiGuard
from parsers.markdown_parser import MarkdownSpecParser

def main():
    print("=== 至誠プロトコル起動: ゼロトラスト検証 ===")
    guard = ShiseiGuard(project_id="docs-as-code-protocol-01")
    
    # 1. 性悪説に基づく厳密なポインタ検証
    premise_path = "premise/001_alignment.json"
    guard.validate_strict_traceability(premise_path)

    # 2. 状態ロック (残心)
    receipt = guard.enforce_integrity()
    print(f"[{receipt['principle']}] State Locked. Checksum: {receipt['checksum'][:12]}")
    
    # 3. 仕様のロード
    parser = MarkdownSpecParser(specs_dir="specs")
    specs = parser.load_all_specs()
    print(f"\n[稼働中の仕様群 ({len(specs)}件)]")
    for spec in specs:
        print(f"  - [{spec['id']}] {spec['title']}")

if __name__ == "__main__":
    main()
