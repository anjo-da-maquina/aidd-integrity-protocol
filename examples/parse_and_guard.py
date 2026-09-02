"""
Integration Example: Zero-Trust Cartesian Audit
"""

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
if sys.path[0] != str(root_dir):
    sys.path.insert(0, str(root_dir))

from shisei_protocol import ShiseiGuard

def main():
    print("=== 至誠プロトコル起動: ゼロトラスト検証 ===")
    guard = ShiseiGuard(project_id="docs-as-code-protocol-01")
    
    # 直積マトリクス監査（MECEの証明）の実行
    premise_path = "premise/001_alignment.json"
    guard.validate_mece_coverage(premise_path)

if __name__ == "__main__":
    main()
