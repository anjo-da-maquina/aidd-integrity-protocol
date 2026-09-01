"""
The SHISEI Protocol - Core Engine
Enforces exhaustive transparency, zero-sontaku (anti-assumption), 
and executes ritual halt (Harakiri) upon detecting insincerity.
"""

import hashlib
import datetime
import sys
from pathlib import Path
from typing import Dict, Any, List

class ShiseiGuard:
    def __init__(self, project_id: str):
        self.project_id = project_id

    def enforce_integrity(self) -> Dict[str, Any]:
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        raw_data = f"{self.project_id}:{timestamp}"
        checksum = hashlib.sha256(raw_data.encode("utf-8")).hexdigest()

        return {
            "project_id": self.project_id,
            "timestamp": timestamp,
            "checksum": checksum,
            "status": "SECURED",
            "principle": "至誠 (Sincerity - Zero Sontaku)"
        }

    def detect_ai_convenience_omission(self, output_text: str) -> bool:
        convenience_markers = ["etc...", "省略します", "簡略化のため", "and others"]
        for marker in convenience_markers:
            if marker in output_text:
                return True
        return False

    def detect_sontaku(self, premise_dir: str = "premise") -> List[str]:
        """
        認識のすり合わせフェーズ。AIが勝手な前提（忖度）を置いていないか検証する。
        """
        target_path = Path(premise_dir)
        violations = []
        
        if not target_path.exists():
            return ["前提条件のすり合わせディレクトリ (premise) が存在しません。ゼロベース合意がスキップされています。"]

        # 忖度や勝手な推測を示す禁止ワード群
        sontaku_markers = ["仮定して", "一般的には", "推測", "よしなに", "デフォルトで", "おそらく"]
        
        for file_path in target_path.glob("**/*.md"):
            content = file_path.read_text(encoding="utf-8")
            
            for marker in sontaku_markers:
                if marker in content:
                    violations.append(f"{file_path.name}: 忖度マーカー '{marker}' を検知。AIが勝手な前提を構築しています。")
            
            if "Missing Parameters: None" in content:
                violations.append(f"{file_path.name}: 隠蔽検知。複雑なタスクにおいて確認事項がゼロであることは不自然です。")

        return violations

    def execute_harakiri(self, reason: str):
        print(f"\n[致命的違反: 腹切り発動 / HARAKIRI TRIGGERED]")
        print(f"理由 (Reason): {reason}")
        print("AI都合の省略、または勝手な前提の構築（忖度）を固く拒絶します。")
        sys.exit(1)
