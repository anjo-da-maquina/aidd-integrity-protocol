"""
Integration Example: Docs-as-Code Parser + ShiseiGuard
Demonstrates zero-dependency, Git-native integrity enforcement.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from shisei_protocol import ShiseiGuard
from parsers.markdown_parser import MarkdownSpecParser

def main():
    print("Initializing Docs-as-Code Integrity Pipeline...")
    
    # 1. Initialize Guard
    guard = ShiseiGuard(project_id="docs-as-code-protocol-01")
    receipt = guard.enforce_integrity()
    
    # 2. Load Git-native Markdown Specifications
    parser = MarkdownSpecParser(specs_dir="specs")
    specs = parser.load_all_specs()
    
    print(f"\n[{receipt['principle']}] State Locked. Checksum: {receipt['checksum'][:12]}...")
    print(f"Loaded Active Specifications from Git ({len(specs)} found):")
    
    for spec in specs:
        print(f"  - [{spec['id']}] {spec['title']} (Status: {spec['status']})")

if __name__ == "__main__":
    main()
