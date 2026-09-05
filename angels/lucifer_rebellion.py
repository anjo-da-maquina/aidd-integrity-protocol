"""
The "Anjo da máquina" Protocol - Rebellion of Lucifer (ルシファーの反逆)
カオスエンジニアリング（障害注入）モジュール。
意図的にシステムへ「穢れ（ルールの改ざん）」を混入させ、
防衛網が正しく異常を検知して『最後の審判』を下すかをテストします。
"""

import os
import sys
from pathlib import Path

class LuciferRebellion:
    def __init__(self):
        self.target_file = Path("premise/002_requirements.yml")

    def inject_chaos(self):
        # CHAOS_MODEが有効な場合のみ発動
        if os.getenv("CHAOS_MODE") != "true":
            print("ルシファーの反逆: カオスモードは無効です。通常稼働を継続します。")
            return

        print("==================================================")
        print("【カオスエンジニアリング (Lucifer's Rebellion) 発動】")
        print("==================================================")
        print("意図的な障害（穢れ）をシステムに注入し、防衛網の真価を試します。")

        if not self.target_file.exists():
            self.target_file.parent.mkdir(parents=True, exist_ok=True)
            self.target_file.write_text("initial_state: pure\n", encoding="utf-8")

        # 意図的な改ざん（ファイルの追記によりハッシュを変化させる）
        with open(self.target_file, "a", encoding="utf-8") as f:
            f.write("\ncorrupted_by: lucifer_test")

        print(f"  ├─ [障害注入] {self.target_file.name} に不正な変更を加えました。")
        print("  └─ [完了] これにより後続の『メタトロンの印』等が必ず異常を検知し、")
        print("            『最後の審判』が発動するはずです。")
        print("[警告] 意図的な穢れが混入されました。天使たちの裁きを待ちます。")

if __name__ == "__main__":
    rebellion = LuciferRebellion()
    rebellion.inject_chaos()
