"""
The SHISEI Protocol - Docs-as-Code Markdown Parser
Extracts specifications and criteria directly from Git-tracked Markdown files.
"""

import re
from pathlib import Path
from typing import List, Dict, Any

class MarkdownSpecParser:
    def __init__(self, specs_dir: str = "specs"):
        self.specs_dir = Path(specs_dir)

    def parse_spec_file(self, file_path: Path) -> Dict[str, Any]:
        content = file_path.read_text(encoding="utf-8")
        frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        metadata = {}
        if frontmatter_match:
            for line in frontmatter_match.group(1).splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    metadata[key.strip()] = val.strip()

        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Untitled"

        return {
            "file": file_path.name,
            "id": metadata.get("id", "UNKNOWN"),
            "status": metadata.get("status", "PENDING"),
            "title": title,
            "raw_content": content
        }

    def load_all_specs(self) -> List[Dict[str, Any]]:
        if not self.specs_dir.exists():
            return []
        specs = []
        for md_file in self.specs_dir.glob("*.md"):
            specs.append(self.parse_spec_file(md_file))
        return specs
