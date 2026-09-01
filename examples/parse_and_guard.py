"""
Integration Example: Docs-as-Code Parser + ShiseiGuard (Zero Sontaku Enforcement)
"""

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from shisei_protocol import ShiseiGuard
from parsers.markdown_parser import MarkdownSpecParser

def main():
    print("Initializing Docs-as-Code Integrity Pipeline...")
    
    guard = ShiseiGuard(project_id="docs-as-code-protocol-01")
    
    # 1. Inspect for Sontaku in Premise Alignment (Phase 1)
    sontaku_violations = guard.detect_sontaku(premise_dir="premise")
    if sontaku_violations:
        guard.execute_harakiri(reason=" / ".join(sontaku_violations))
        
    print("[Phase 1 Passed] 認識のすり合わせ完了。忖度は検知されませんでした。")

    # 2. State Lock & Specs Loading (Phase 2)
    receipt = guard.enforce_integrity()
    parser = MarkdownSpecParser(specs_dir="specs")
    specs = parser.load_all_specs()
    
    print(f"\n[{receipt['principle']}] State Locked. Checksum: {receipt['checksum'][:12]}...")
    print(f"Loaded Active Specifications from Git ({len(specs)} found):")
    
    for spec in specs:
        print(f"  - [{spec['id']}] {spec['title']} (Status: {spec['status']})")

if __name__ == "__main__":
    main()
