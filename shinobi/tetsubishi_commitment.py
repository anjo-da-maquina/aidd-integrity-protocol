"""
The SHINOBI Protocol - Tetsubishi (鉄菱) Commitment
暗号論的コミットメントによる「後出しジャンケン」の封殺。
一度定めた前提条件（JSON）のハッシュを不可逆な誓いとして刻み込み、
事後的なルールの改ざん（AIや管理者による都合の良い書き換え）を検知する。
"""

import sys
import json
import hashlib
from pathlib import Path

class Tetsubishi:
    def __init__(self, target_file: str, lock_file: str):
        self.target_file = Path(target_file)
        self.lock_file = Path(lock_file)

    def execute_harakiri(self, reason: str):
        """誓いを破った者を即座に処断する"""
        print(f"\n[暗部摘発: 鉄菱 / TETSUBISHI TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print("プロセス進行後の卑劣なルール改ざん（後出しジャンケン）を検知。")
        print("誓いを破りし者に明日はない。これより切腹を実行する。")
        sys.exit(1)

    def calculate_hash(self) -> str:
        """JSONの構造ハッシュを計算する"""
        if not self.target_file.exists():
            self.execute_harakiri(f"監視対象 {self.target_file.name} が存在しない。")
        
        try:
            # 空白の違い等で誤検知しないよう、一度パースしてソートし直してからハッシュ化
            data = json.loads(self.target_file.read_text(encoding="utf-8"))
            normalized_str = json.dumps(data, sort_keys=True)
            return hashlib.sha256(normalized_str.encode('utf-8')).hexdigest()
        except json.JSONDecodeError:
            self.execute_harakiri("JSONの構文が破壊されている。")

    def enforce_commitment(self):
        """鉄菱の散布と検証"""
        print(f"鉄菱を散布している... {self.target_file.name} の不変性を確認中。")
        current_hash = self.calculate_hash()

        if not self.lock_file.exists():
            # 初回実行時：誓いのロック（ハッシュの保存）
            self.lock_file.write_text(current_hash, encoding="utf-8")
            print(f"[鉄菱 設置完了] 前提条件のハッシュをロックした。以降の改ざんは一切許されない。")
            print(f"Commitment Hash: {current_hash}")
            return

        # 2回目以降：改ざんの検証
        locked_hash = self.lock_file.read_text(encoding="utf-8").strip()
        
        if current_hash != locked_hash:
            self.execute_harakiri(
                f"前提条件の暗号ハッシュが一致しない。\n"
                f"  Expected (Locked): {locked_hash}\n"
                f"  Actual (Tampered): {current_hash}"
            )

        print(f"[鉄菱 検証通過] 誓いは守られている。前提条件に改ざんなし。")

if __name__ == "__main__":
    # 侍の前提条件ファイルを監視対象とし、同じディレクトリにロックファイルを作る
    target = "premise/001_alignment.json"
    lock = "premise/.001_alignment.lock"
    
    tetsubishi = Tetsubishi(target, lock)
    tetsubishi.enforce_commitment()
