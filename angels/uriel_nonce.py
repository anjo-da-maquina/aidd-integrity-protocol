"""
The "Anjo da máquina" Protocol - Uriel (ウリエルの炎)
過去の成功データや証明（JSON, ZKP）の使い回し（リプレイ攻撃）を検知し、
使い捨ての暗号札（Nonce）の重複をもって「偽物」と断定、炎で焼き尽くす。
"""

import sys
import uuid
import datetime
from pathlib import Path

class UrielNonce:
    def __init__(self, log_file: str):
        self.log_file = Path(log_file)
        if not self.log_file.exists():
            self.log_file.touch()

    def execute_dies_irae(self, reason: str, fake_nonce: str):
        """偽物を検知し、最後の審判を下す"""
        print(f"\n[聖なる摘発: ウリエルの炎 / URIEL TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print(f"使用済みの刻印: {fake_nonce}")
        print("過去の成功データを使い回す卑劣な欺瞞（リプレイ攻撃）を検知。")
        print("ウリエルの炎が穢れを焼き尽くす。これより最後の審判へ移行する。")
        sys.exit(1)

    def generate_nonce(self) -> str:
        """その瞬間しか有効でない使い捨ての刻印（Nonce）を発行する"""
        return f"{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}"

    def verify_and_burn_nonce(self, nonce_to_check: str):
        """
        提出されたNonceが過去に使われた履歴がないか検証し、
        問題なければ炎の痕跡として記録する。
        """
        print(f"ウリエルが刻印を検分している... [Nonce: {nonce_to_check}]")
        
        used_nonces = self.log_file.read_text(encoding="utf-8").splitlines()
        if nonce_to_check in used_nonces:
            self.execute_dies_irae("この刻印は既に過去の審査で使用されている。", nonce_to_check)

        with self.log_file.open("a", encoding="utf-8") as f:
            f.write(nonce_to_check + "\n")

        print("[ウリエルの炎 検証通過] 提出されたデータは使い回しではない『真実』であることを確認した。")

if __name__ == "__main__":
    graveyard = "premise/.used_nonces.log"
    uriel = UrielNonce(graveyard)
    
    current_request_nonce = uriel.generate_nonce()
    uriel.verify_and_burn_nonce(current_request_nonce)
