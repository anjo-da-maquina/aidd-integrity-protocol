"""
The "Anjo da máquina" Protocol - Alpha and Omega Guard (アルファとオメガの結界)
監視網（CI/CDパイプライン）そのものに対する改ざんを検知するメタ監視。
『最後の審判』や『静寂の玉座』の記述がワークフローから削除されていないかを検証する。
"""

import sys
from pathlib import Path

class AlphaOmegaGuard:
    def __init__(self):
        self.workflow_path = Path(".github/workflows/anjo_pipeline.yml")
        # パイプライン内に絶対に存在しなければならない神聖なキーワード
        self.holy_keywords = [
            "angels/dies_irae.py",
            "angels/ataraxia_throne.py",
            "if: failure() || cancelled()"  # 人為的キャンセルに対する防衛
        ]

    def execute_dies_irae(self, reason: str):
        print(f"\n[聖なる摘発: アルファとオメガの結界 / ALPHA & OMEGA TRIGGERED]")
        print(f"状態: 監視網自体の改ざん (CI/CD Pipeline Tampering)")
        print(f"検知理由: {reason}")
        print("神の法（ワークフロー定義）からキルスイッチが抜き取られています。即時遮断します。")
        sys.exit(1)

    def audit_workflow_integrity(self):
        print("アルファとオメガの結界（パイプライン自己改ざん監査）を開始します。")
        
        if not self.workflow_path.exists():
            self.execute_dies_irae(f"ワークフロー定義ファイルが見つかりません: {self.workflow_path}")

        with open(self.workflow_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for keyword in self.holy_keywords:
            if keyword not in content:
                self.execute_dies_irae(
                    f"必須となる防衛機構の記述が見つかりません: '{keyword}'\n"
                    "グリゴリ（堕落AI）やネフィリム（悪意ある管理者）による監視網の破壊工作とみなします。"
                )

        print("  └─ [自己証明] ワークフローの不変性とキルスイッチの存在を確認しました。")
        print("[検証通過] アルファでありオメガ。神の法に改ざんはありません。")

if __name__ == "__main__":
    guard = AlphaOmegaGuard()
    guard.audit_workflow_integrity()
