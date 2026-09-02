"""
The SHINOBI Protocol - Kageuchi (影討ち) Anti-Replay
過去の成功データや証明（JSON, ZKP）の使い回し（リプレイ攻撃）を検知し、
使い捨ての暗号札（Nonce）の重複をもって「影（偽物）」と断定、処断する。
"""

import sys
import uuid
import datetime
from pathlib import Path

class Kageuchi:
    def __init__(self, log_file: str):
        self.log_file = Path(log_file)
        if not self.log_file.exists():
            self.log_file.touch()

    def execute_harakiri(self, reason: str, fake_nonce: str):
        """過去のデータを使い回した影（偽物）を討ち果たす"""
        print(f"\n[暗部摘発: 影討ち / KAGEUCHI TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print(f"使用済みの暗号札: {fake_nonce}")
        print("過去の成功データを使い回す卑劣な欺瞞（リプレイ攻撃）を検知。")
        print("これは本物ではない『影』である。即座に斬り捨てる。")
        sys.exit(1)

    def generate_nonce(self) -> str:
        """その瞬間しか有効でない使い捨ての暗号札を発行する"""
        return f"{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}"

    def verify_and_burn_nonce(self, nonce_to_check: str):
        """
        提出されたNonceが過去に使われた履歴がないか検証し、
        問題なければ履歴（焼け跡）として記録する。
        """
        print(f"影討ちが暗号札を検分している... [Nonce: {nonce_to_check}]")
        
        # 過去の履歴（焼け跡）と照合
        used_nonces = self.log_file.read_text(encoding="utf-8").splitlines()
        if nonce_to_check in used_nonces:
            self.execute_harakiri("この暗号札は既に過去の審査で使用されている。", nonce_to_check)

        # 検証通過：このNonceを「使用済み」としてログに焼付ける
        with self.log_file.open("a", encoding="utf-8") as f:
            f.write(nonce_to_check + "\n")

        print("[影討ち 検証通過] 提出されたデータは使い回しではない『本物』であることを確認した。")

if __name__ == "__main__":
    # 使用済みNonceを記録する墓場（ログファイル）
    graveyard = "premise/.used_nonces.log"
    kageuchi = Kageuchi(graveyard)
    
    # 【シミュレーション】
    # 本来は前提条件JSONやZKP証明の中にNonceが埋め込まれている。
    # 今回は新規に発行した正しいNonceを検証に通す。
    # （※もしここで過去の固定文字列 "20260903-abcdef12" などを渡して2回実行すると腹切りが発動する）
    current_request_nonce = kageuchi.generate_nonce()
    kageuchi.verify_and_burn_nonce(current_request_nonce)
