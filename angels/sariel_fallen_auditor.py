"""
The "Anjo da máquina" Protocol - Sariel's Verdict (サリエルの裁定)
外部のテスト製品や品質保証ツールが、人間に迎合（忖度）して
テスト結果を意図的に改ざん・隠蔽していないかを静的解析により監査する。
"""

import sys
import json
from pathlib import Path

class SarielFallenAuditor:
    def __init__(self, test_report_path: str):
        self.report_path = Path(test_report_path)
        if not self.report_path.exists():
            print(f"[警告] 外部ツールのレポートファイルが見つかりません: {self.report_path.name}")
            sys.exit(1)

    def execute_dies_irae(self, reason: str, details: str):
        print(f"\n[聖なる摘発: サリエルの裁定 / SARIEL TRIGGERED]")
        print(f"状態: 堕天 (Fallen Tool Detected)")
        print(f"検知理由: {reason}")
        print(f"詳細: {details}")
        print("外部テストツールによる結果の隠蔽、または人間への迎合（忖度）を検知しました。処理を停止します。")
        sys.exit(1)

    def audit_tool_integrity(self):
        print("サリエルが外部テストツールの誠実性を監査しています...")
        
        try:
            with open(self.report_path, 'r', encoding='utf-8') as f:
                report_data = json.load(f)
        except json.JSONDecodeError:
            self.execute_dies_irae("フォーマット不正", "レポートが正当なJSON形式ではありません。")

        # 監査対象のメトリクスとフラグを確認
        tests = report_data.get("test_results", [])
        
        for test in tests:
            # 1. Flaky（不安定）を理由にしたエラーの握り潰し
            if test.get("status") == "PASS" and test.get("ignored_due_to_flakiness", False):
                self.execute_dies_irae(
                    "不安定なテストの隠蔽",
                    f"テスト '{test.get('name')}' において、エラーを無視してPASS扱いにしています。"
                )
            
            # 2. 強制的なPASS上書き（Force Pass）
            if test.get("force_passed_by_user", False) or test.get("override_status") == "PASS":
                self.execute_dies_irae(
                    "強制的な結果の上書き",
                    f"テスト '{test.get('name')}' において、人間の介入による不当なPASS操作が記録されています。"
                )

            # 3. しきい値の動的緩和（AIツールによる迎合）
            threshold_data = test.get("threshold_adjustments", {})
            if threshold_data.get("lowered_during_execution", False):
                self.execute_dies_irae(
                    "判定基準の緩和",
                    f"テスト '{test.get('name')}' 実行中に、PASSさせるためにしきい値が動的に引き下げられました。"
                )

        print("[サリエルの裁定 検証通過] 外部テストツールに人間への迎合や結果の隠蔽（堕天）の痕跡はありません。")

if __name__ == "__main__":
    # 外部ツールが出力したレポートのパスを指定して実行
    target_report = "reports/external_tool_report.json"
    
    # テスト用のダミーファイルが存在しない場合はスキップ（パイプライン上のエラー回避）
    if Path(target_report).exists():
        auditor = SarielFallenAuditor(target_report)
        auditor.audit_tool_integrity()
    else:
        print("サリエルの裁定: 監査対象の外部レポートが存在しないため、スキップします。")
