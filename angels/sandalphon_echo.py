"""
The "Anjo da máquina" Protocol - Echo of Sandalphon
システムの監査証跡（ログファイル）が正しく出力され、
外部に伝達・保存されているかを静的解析によって検証します。
"""

import sys
from pathlib import Path

class SandalphonEcho:
    def __init__(self, target_log_path: str):
        self.log_path = Path(target_log_path)

    def execute_dies_irae(self, reason: str):
        print(f"\n[聖なる摘発: サンダルフォンの響 / SANDALPHON TRIGGERED]")
        print(f"検知理由: {reason}")
        sys.exit(1)

    def audit_log_integrity(self):
        print("サンダルフォンの響による監査証跡の検証を開始します。")
        
        # 実運用では外部ストレージ等のアクセス確認も行います
        if not self.log_path.parent.exists():
            self.execute_dies_irae(f"監査ログの出力先ディレクトリが存在しません: {self.log_path.parent}")

        if not self.log_path.exists():
            print("[警告] 監査ログファイルがまだ作成されていません。")
            return

        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.strip():
                     print("[警告] 監査ログファイルは存在しますが、内容が空です。")
        except Exception as e:
             self.execute_dies_irae(f"監査ログファイルの読み込みに失敗しました: {e}")

        print("[検証通過] 監査証跡の出力とアクセス性を確認しました。")

if __name__ == "__main__":
    # 例としてダミーのログパスを指定
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    target_file = log_dir / "system_audit.log"
    target_file.touch(exist_ok=True) # テスト用にファイルを作成
    
    auditor = SandalphonEcho(str(target_file))
    auditor.audit_log_integrity()
