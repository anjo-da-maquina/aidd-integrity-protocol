"""
The "Anjo da máquina" Protocol - Remediation of Raphael (ラファエルの癒やし)
フェイルクローズ前の自律修復レイヤー。
軽微なフォーマットエラーや状態のドリフトを検知し、浄化（自動修復）を試みる。
ただし、意図的な改ざん（グリゴリ/ネフィリムの干渉）は「致命的な穢れ」として修復を拒絶する。
"""

import sys
from pathlib import Path

class RaphaelRemediation:
    def __init__(self):
        self.target_files = [
            Path("premise/002_requirements.yml")
        ]

    def attempt_healing(self):
        print("ラファエルの癒やし（自律的状態修復）を開始します。")

        for file_path in self.target_files:
            if not file_path.exists():
                print(f"  ├─ [警告] {file_path.name} が存在しません。修復をスキップします。")
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 致命的な穢れ（カオスモード等による意図的な改ざん）の検知
                if "corrupted_by" in content or "lucifer_test" in content:
                    print(f"  ├─ [診断] {file_path.name} に『致命的な穢れ（大罪）』を検知。")
                    print(f"  │   └─ ラファエルは修復を拒絶しました。これは人間のミスではなく、悪意ある干渉です。")
                    continue

                # 軽微な穢れ（不要な空白、フォーマットの乱れ）の自動修復
                healed_content = "\n".join([line.rstrip() for line in content.splitlines() if line.strip() != ""])
                
                if content != healed_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(healed_content)
                    print(f"  ├─ [治癒] {file_path.name} の軽微なフォーマットの乱れを浄化しました。")
                else:
                    print(f"  ├─ [診断] {file_path.name} は清廉に保たれています。")

            except Exception as e:
                print(f"  ├─ [エラー] {file_path.name} の診断中に予期せぬ障害が発生: {e}")

        print("  └─ [完了] 癒やしのプロセスが終了しました。これより厳格な監査へ移行します。")

if __name__ == "__main__":
    raphael = RaphaelRemediation()
    raphael.attempt_healing()
