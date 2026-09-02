"""
The SHISEI Protocol - Zero-Trust Engine
トレーサビリティ検証およびMECE（直積マトリクス）監査エンジン。
AIによる無断の選択肢隠蔽を数理的に検知し、排除する。
"""

import json
import sys
import math
from pathlib import Path

class ShiseiGuard:
    def __init__(self, project_id: str):
        self.project_id = project_id

    def execute_harakiri(self, reason: str):
        print(f"\n[致命的違反: 腹切り発動 / HARAKIRI TRIGGERED]")
        print(f"理由: {reason}")
        print("システムを直ちに破棄します。")
        sys.exit(1)

    def validate_mece_coverage(self, premise_file: str):
        """
        変数の直積（デカルト積）を計算し、提案数と除外数の合計が
        論理的な全パターン数と一致するかを監査する。
        """
        file_path = Path(premise_file)
        if not file_path.exists():
            self.execute_harakiri("前提条件ファイルが存在しません。")

        data = json.loads(file_path.read_text(encoding="utf-8"))
        variables = data.get("variables", {})
        
        if not variables:
            self.execute_harakiri("変数が定義されていません。全量検査が不可能です。")

        # 直積（全組み合わせ数）の計算
        total_expected_combinations = math.prod([len(values) for values in variables.values()])

        proposed = data.get("proposed_options", [])
        rejected = data.get("rejected_options", [])

        total_presented = len(proposed) + len(rejected)

        print(f"[MECE Audit] 変数の全組み合わせ数 (直積): {total_expected_combinations} パターン")
        print(f"[MECE Audit] AIからの提示数: 提案({len(proposed)}) + 除外証明({len(rejected)}) = {total_presented} パターン")

        if total_presented != total_expected_combinations:
            self.execute_harakiri(
                f"網羅性違反を検知。論理的な全パターン数({total_expected_combinations})に対し、"
                f"AIの提示数({total_presented})が一致しません。"
                f"{total_expected_combinations - total_presented}個の選択肢が無断で隠蔽されています。"
            )

        # 除外された選択肢が、正当な制約(Boundaries)を理由にしているか確認
        valid_bnd_ids = {bnd["id"] for bnd in data.get("boundaries", [])}
        for rej in rejected:
            for bnd_id in rej.get("rejected_by", []):
                if bnd_id not in valid_bnd_ids:
                    self.execute_harakiri(f"除外理由の捏造を検知。未定義の制約 '{bnd_id}' を理由に選択肢を消去しています。")

        print("[MECE Audit Passed] 全パターンの網羅と、隠蔽のないことを数理的に証明しました。")
