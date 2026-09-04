"""
The "Anjo da máquina" Protocol - Throne of Ataraxia (静寂の玉座)
インフラの完全なる無状態化（Stateless）と破棄。
すべての処理、あるいは最後の審判が終わった後、システムは状態（State）への
一切の執着を捨て、コンテナ・VPC・一時ファイルを完全に消去して「無（静寂）」へと還る。
"""

import sys
import shutil
from pathlib import Path

class ThroneOfAtaraxia:
    def __init__(self):
        # 破棄対象の一時ファイルやキャッシュ（システムが残した現世の執着）
        self.targets = [
            Path("premise/.001_divine_law.yml.lock"),
            Path("premise/.002_requirements.yml.lock"),
            Path("covenant/.used_nonces.log") # ウリエルが旧時代に残した可能性のあるログ
        ]

    def return_to_nothingness(self):
        print("==================================================")
        print("【静寂の玉座 (Throne of Ataraxia) 起動】")
        print("==================================================")
        print("システムはすべての状態（State）を放棄し、完全なる静寂へと還る。")

        for target in self.targets:
            if target.exists():
                try:
                    if target.is_dir():
                        shutil.rmtree(target)
                    else:
                        target.unlink()
                    print(f"  ├─ [破棄] {target.name} を空間から完全に消去した。")
                except Exception as e:
                    print(f"  ├─ [警告] {target.name} の消去に失敗: {e}")

        print("  └─ [インフラ解体] 仮想ネットワーク(VPC)およびコンテナ群の破棄シミュレーション完了。")
        print("\n[静寂の玉座 完了] 空間には何も残されていない。次回の稼働時、システムは再び純白の状態で降臨する。")

if __name__ == "__main__":
    throne = ThroneOfAtaraxia()
    throne.return_to_nothingness()
