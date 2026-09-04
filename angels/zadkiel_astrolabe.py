"""
The "Anjo da máquina" Protocol - Astrolabe of Zadkiel
システムの状態遷移ログを解析し、正規のステートマシン定義から
逸脱した不正な遷移（状態のスキップや逆行）が存在しないかを検証します。
"""

import sys
import json
from pathlib import Path

class ZadkielAstrolabe:
    def __init__(self, log_path: str):
        self.log_path = Path(log_path)
        # 許可される状態遷移の定義（例）
        self.valid_transitions = {
            "INIT": ["REVIEW_PENDING"],
            "REVIEW_PENDING": ["APPROVED", "REJECTED"],
            "APPROVED": ["DISBURSED"],
            "REJECTED": [],
            "DISBURSED": []
        }

    def execute_dies_irae(self, reason: str):
        print(f"\n[聖なる摘発: ザドキエルの天球儀 / ZADKIEL TRIGGERED]")
        print(f"検知理由: {reason}")
        sys.exit(1)

    def audit_state_transitions(self):
        print("ザドキエルの天球儀による状態遷移監査を開始します。")
        
        if not self.log_path.exists():
            print("[スキップ] 状態遷移ログが存在しないため、監査をスキップします。")
            return

        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                transition_logs = json.load(f)
        except Exception as e:
            self.execute_dies_irae(f"ログファイルの読み込みに失敗しました: {e}")

        for record in transition_logs:
            from_state = record.get("from")
            to_state = record.get("to")
            
            allowed_next_states = self.valid_transitions.get(from_state, [])
            if to_state not in allowed_next_states:
                self.execute_dies_irae(
                    f"不正な状態遷移を検知しました: {from_state} -> {to_state} (トランザクションID: {record.get('tx_id')})"
                )

        print("[検証通過] すべての状態遷移が正規のフローに従っていることを確認しました。")

if __name__ == "__main__":
    auditor = ZadkielAstrolabe("logs/state_transitions.json")
    auditor.audit_state_transitions()
