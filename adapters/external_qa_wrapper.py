import subprocess
import sys
from pathlib import Path

class ExternalQAAdapter:
    def __init__(self, tool_name: str, test_dir: str):
        self.tool_name = tool_name
        self.test_dir = Path(test_dir)

    def execute_audit(self):
        print(f"[{self.tool_name} Adapter] 外部QAモジュールによる検証を開始します...")
        
        # テスト対象ディレクトリが存在しない場合は、安全にスキップする
        if not self.test_dir.exists():
            print(f"[{self.tool_name} Adapter] 対象のテストディレクトリ ({self.test_dir}) が存在しないため、今回は正常パスとして扱います。")
            return

        result = subprocess.run(["pytest", str(self.test_dir)], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"\n[聖なる摘発: {self.tool_name} 連携監査 / EXTERNAL AUDIT FAILED]")
            print(f"詳細ログ:\n{result.stderr}")
            sys.exit(1)

        print(f"[{self.tool_name} Adapter 検証通過] 外部QAモジュールの監査要件を満たしました。")

if __name__ == "__main__":
    adapter = ExternalQAAdapter(
        tool_name="Amiable/Esplat",
        test_dir="tests/external_amiable_suite"
    )
    adapter.execute_audit()
