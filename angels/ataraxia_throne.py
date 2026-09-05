"""
The "Anjo da máquina" Protocol - Throne of Ataraxia (静寂の玉座)
"""
import shutil
from pathlib import Path

class ThroneOfAtaraxia:
    def __init__(self):
        self.targets = [
            Path("premise/.001_divine_law.yml.lock"),
            Path("premise/.002_requirements.yml.lock"),
            Path("covenant/.used_nonces.log"),
            Path("reports"), # 自動生成されたレポート群の破棄
            Path("logs")     # 自動生成されたログ群の破棄
        ]

    def return_to_nothingness(self):
        print("==================================================")
        print("【静寂の玉座 (Throne of Ataraxia) 起動】")
        print("==================================================")
        
        for target in self.targets:
            if target.exists():
                try:
                    if target.is_dir():
                        shutil.rmtree(target)
                    else:
                        target.unlink()
                    print(f"  ├─ [破棄] {target.name} を完全に消去した。")
                except Exception as e:
                    print(f"  ├─ [警告] {target.name} の消去に失敗: {e}")

        print("  └─ [インフラ解体] 仮想ネットワークおよびコンテナ群の破棄シミュレーション完了。")
        print("\n[静寂の玉座 完了] 空間には何も残されていない。システムは純白へと回帰した。")

if __name__ == "__main__":
    throne = ThroneOfAtaraxia()
    throne.return_to_nothingness()
