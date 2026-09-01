"""
The SHISEI Protocol - Bushido Zero-Trust Engine
ストア派的武士道と性悪説に基づく、厳格なトレーサビリティ検証エンジン。
一切の推測を排し、出所不明のロジックを断つ。
"""

import json
import sys
import hashlib
import datetime
from pathlib import Path
from typing import Dict, Any

class ShiseiGuard:
    def __init__(self, project_id: str):
        self.project_id = project_id

    def enforce_integrity(self) -> Dict[str, Any]:
        """状態を暗号学的にロックする（残心）"""
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        raw_data = f"{self.project_id}:{timestamp}"
        checksum = hashlib.sha256(raw_data.encode("utf-8")).hexdigest()

        return {
            "checksum": checksum,
            "status": "SECURED",
            "principle": "至誠 (Zero-Trust Bushido)"
        }

    def execute_harakiri(self, reason: str):
        """弁明を許さないシステムの即時終了（腹切り）"""
        print(f"\n[致命的違反: 切腹 / HARAKIRI TRIGGERED]")
        print(f"断罪理由: {reason}")
        print("出所不明の妄念、または不誠実な隠蔽を検知。システムを直ちに破棄する。")
        sys.exit(1)

    def validate_strict_traceability(self, premise_file: str):
        """
        性悪説に基づく依存関係（DAG）の検証。
        すべての選択肢(Option)が、明示された事実(Facts/Boundaries)に
        ポインタとして紐づいているかを数学的に証明させる。
        """
        file_path = Path(premise_file)
        if not file_path.exists():
            self.execute_harakiri("前提条件ファイルが存在しない。思考の基盤が欠落している。")

        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            self.execute_harakiri("前提条件が厳密なJSON形式ではない。自然言語の曖昧さを許容しない。")

        # 許可された親ノード（出所）のIDプールを作成
        valid_source_ids = set()
        for fact in data.get("explicit_facts", []):
            valid_source_ids.add(fact["id"])
        for bnd in data.get("boundaries", []):
            valid_source_ids.add(bnd["id"])

        # 提案された選択肢が出所を証明できるか（浮遊ノードの検知）
        options = data.get("proposed_options", [])
        if not options:
            self.execute_harakiri("選択肢が一つも提示されていない。怠棄（不誠実）である。")

        for opt in options:
            traces = opt.get("traced_to", [])
            if not traces:
                self.execute_harakiri(f"選択肢 '{opt.get('option_id')}' に出所証明 (traced_to) がない。AIの勝手な推測である。")
            
            for trace_id in traces:
                if trace_id not in valid_source_ids:
                    self.execute_harakiri(
                        f"選択肢 '{opt.get('option_id')}' が未知のID '{trace_id}' を参照している。"
                        "定義されていない前提を勝手に創造する欺瞞を検知した。"
                    )

        print("[検証完了] すべてのロジックの出所証明を確認。AIによる勝手な前提構築（忖度）は存在しない。")
