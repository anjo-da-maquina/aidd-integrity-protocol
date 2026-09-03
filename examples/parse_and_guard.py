# examples/parse_and_guard.py
import sys
import os
import hmac
import hashlib
import time

# プロジェクトのルートディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shinobi.kaishaku_killswitch import KaishakuKillswitch
from shinobi.kageboushi_middleware import KageboushiMiddleware
from shinobi.kumonoito_analyzer import TransactionSandbox
from shinobi.tsujigiri_redteam import TsujigiriRedTeam

def main():
    print("=== 至誠プロトコル: 統合防衛・カオスシミュレーション開始 ===")
    
    master_secret = b"shisei_enterprise_master_secret"
    
    # 1. キルスイッチの初期化
    killswitch = KaishakuKillswitch(master_secret)
    
    # キルスイッチのトリガー関数を定義
    def trigger_killswitch(signal):
        killswitch.verify_and_trigger(signal, signal.get("signature", ""))

    # 2. ミドルウェア・サンドボックスの初期化
    kageboushi = KageboushiMiddleware(master_secret, trigger_killswitch)
    sandbox = TransactionSandbox(master_secret, trigger_killswitch)
    tsujigiri = TsujigiriRedTeam(master_secret)

    # 3. 辻斬り（動的攻撃）のシミュレーション実行
    attack = tsujigiri.generate_attack_vector()
    print(f"[シミュレーション] 攻撃ベクトル検知: {attack['payload']}")

    # 4. 影法師によるプレ監査（不正な攻撃に対して自動的にキルスイッチが発動するべき場面）
    print("--- 影法師プレ監査および介錯連動テスト ---")
    
    # 意図的に不正な署名やタイムウィンドウ違反、または辻斬りの毒を流し込む
    try:
        # ここで防壁が破綻または攻撃を検知してキルスイッチ（sys.exit(1)）が走ることを期待
        kageboushi.pre_audit(
            payload={"action": "unauthorized_fund_transfer", "amount": 1000000},
            nonce=attack["nonce"],
            timestamp_ms=attack["timestamp_ms"] - 500000, # タイムウィンドウ違反を誘発
            signature=attack["signature"]
        )
    except SystemExit as e:
        # キルスイッチによる自決（Exit code 1）を「プロトコル正常防衛成功」としてハンドリング
        if e.code == 1:
            print("=== 【判定: 合格】至誠プロトコルの介錯が正常に発動し、脅威を完全に暗殺しました。 ===")
            sys.exit(0) # テスト・スクリプトとしては正常終了（Exit 0）にする
        else:
            raise e

if __name__ == "__main__":
    main()
