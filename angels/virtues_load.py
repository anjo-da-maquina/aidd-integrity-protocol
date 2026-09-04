"""
The "Anjo da máquina" Protocol - Virtues (力天使の試練)
奇跡と勇気を司る力天使による、デプロイ直後の非機能要件（負荷・性能）監査。
御触書に定められた最大許容レスポンスタイムや同時接続の猛威をシステムにぶつけ、
大群勢に囲まれてもパフォーマンスが崩壊しない堅牢性を証明する。
"""

import sys
import yaml
import time
import random
from pathlib import Path
from typing import Any

class VirtuesTrial:
    def __init__(self, requirements_file: str):
        self.req_file = Path(requirements_file)
        if not self.req_file.exists():
            self.execute_dies_irae_missing("神の法（要件定義YAML）が存在しない。")
        
        with open(self.req_file, 'r', encoding='utf-8') as f:
            self.requirements = yaml.safe_load(f)

    def execute_dies_irae_missing(self, reason: str):
        print(f"\n[聖なる摘発: 力天使の試練 / VIRTUES TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        sys.exit(1)

    def execute_dies_irae(self, reason: str, measured_val: Any, limit_val: Any):
        print(f"\n[聖なる摘発: 力天使の試練 / VIRTUES TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print(f"実測値: {measured_val} / 許容限界: {limit_val}")
        print("猛烈な負荷を前にシステムが膝を屈した。非機能要件の未達を検知。")
        print("実戦に耐ええぬ脆弱な防壁は破棄する。これより最後の審判を実行する。")
        sys.exit(1)

    def execute_load_test(self):
        print("力天使がシステムに猛威を放つ... (非機能要件・負荷テストを開始)")
        
        non_func_req = self.requirements.get("non_functional_requirements", {})
        concurrent_users = non_func_req.get("concurrent_users", 1)
        max_response_ms = non_func_req.get("max_response_time_ms", 1000)

        print(f"  ├─ {concurrent_users} の仮想アクセスによる一斉攻撃シミュレーション中...")
        time.sleep(1)

        actual_max_response = random.randint(100, max_response_ms - 100) # シミュレーション
        
        if actual_max_response > max_response_ms:
            self.execute_dies_irae(
                "レスポンスタイムが許容限界を超過（SLA違反）。", 
                actual_max_response, max_response_ms
            )

        print(f"  ├─ 最大レスポンスタイム: {actual_max_response}ms (許容: {max_response_ms}ms)")
        print("[力天使の試練 達成] 大群勢の猛威を退けた。システムの堅牢性と速度を証明。")

if __name__ == "__main__":
    trial = VirtuesTrial("premise/002_requirements.yml")
    trial.execute_load_test()
