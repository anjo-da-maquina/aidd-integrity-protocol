import subprocess
import sys

class ExternalQAAdapter:
    def __init__(self, tool_name: str, command: list):
        self.tool_name = tool_name
        self.command = command

    def execute_audit(self):
        print(f"[{self.tool_name} Adapter] 外部QAモジュールによる検証を開始します...")
        try:
            # 外部ツール（Esplat, Amiable, Selenium等）の実行
            result = subprocess.run(self.command, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"\n[聖なる摘発: {self.tool_name} 連携監査 / EXTERNAL AUDIT FAILED]")
                print(f"詳細ログ:\n{result.stderr}")
                sys.exit(1) # 異常検知としてフェイルクローズをトリガー

            print(f"[{self.tool_name} Adapter 検証通過] 外部QAモジュールの監査要件を満たしました。")
        
        except Exception as e:
            print(f"[システムエラー] 外部ツールの呼び出しに失敗しました: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # 例: Amiableアーキテクチャのテストスクリプトをラップして実行
    amiable_adapter = ExternalQAAdapter(
        tool_name="Amiable/Esplat",
        command=["python", "-m", "pytest", "tests/external_amiable_suite/"]
    )
    amiable_adapter.execute_audit()
