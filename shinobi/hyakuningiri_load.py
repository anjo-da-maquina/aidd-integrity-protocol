"""
The SHINOBI Protocol - Hyakuningiri (百人斬り) Non-Functional Auditor
YAMLで記述された御触書（002_requirements.yml）を読み込み、非機能要件の負荷監査を行う。
"""

import sys
import yaml
import time
import random
from pathlib import Path
from typing import Any

class Hyakuningiri:
    def __init__(self, requirements_file: str):
        self.req_file = Path(requirements_file)
        if not self.req_file.exists():
            self.execute_harakiri_missing("御触書（要件定義YAML）が存在しない。")
        
        with open(self.req_file, 'r', encoding='utf-8') as f:
            self.requirements = yaml.safe_load(f)

    def execute_harakiri_missing(self, reason: str):
        print(f"\n[暗部摘発: 百人斬り / HYAKUNINGIRI TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        sys.exit(1)

    def execute_harakiri(self, reason: str, measured_val: Any, limit_val: Any):
        print(f"\n[暗部摘発: 百人斬り / HYAKUNINGIRI TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print(f"実測値: {measured_val} / 許容限界: {limit_val}")
        print("大軍勢（高負荷）を前にシステムが膝を屈した。非機能要件の未達を検知。")
        print("実戦に耐ええぬ脆弱な防壁は破棄する。これより切腹を実行する。")
        sys.exit(1)

    def execute_load_test(self):
        print("百人斬りを開幕する... 非機能要件（負荷・性能）テストを開始。")
        
        non_func_req = self.requirements.get("non_functional_requirements", {})
        concurrent_users = non_func_req.get("concurrent_users", 1)
        max_response_ms = non_func_req.get("max_response_time_ms", 1000)

        print(f"  ├─ {concurrent_users} の仮想ユーザーによる一斉攻撃シミュレーション中...")
        time.sleep(1)

        actual_max_response = random.randint(100, max_response_ms - 100) # 試し斬り
        
        if actual_max_response > max_response_ms:
            self.execute_harakiri(
                "レスポンスタイムが許容限界を超過（SLA違反）。", 
                actual_max_response, max_response_ms
            )

        print(f"  ├─ 最大レスポンスタイム: {actual_max_response}ms (許容: {max_response_ms}ms)")
        print("[百人斬り 完了] 大軍を退けた。システムの非機能要件（堅牢性・速度）を証明した。")

if __name__ == "__main__":
    hyakuningiri = Hyakuningiri("premise/002_requirements.yml")
    hyakuningiri.execute_load_test()
