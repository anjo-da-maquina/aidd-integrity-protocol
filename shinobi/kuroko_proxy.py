# shinobi/kuroko_proxy.py
import time
import hmac
import hashlib
import logging
from typing import Dict, Any, Callable, Optional

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-KUROKO: %(message)s")
logger = logging.getLogger("KurokoProxy")

class KurokoProxy:
    """
    黒衣（KUROKO）：サイドカー・無侵襲インテグレーション・プロキシ
    既存のAIDD製品のコードベースを変更することなく、
    APIコールの間に常時憑依し、入出力の全監査とキルスイッチの連動を強制する。
    """
    def __init__(self, master_secret: bytes, kageboushi_middleware, transaction_sandbox, killswitch_trigger):
        self._master_secret = master_secret
        self._kageboushi = kageboushi_middleware
        self._sandbox = transaction_sandbox
        self._killswitch = killswitch_trigger

    def intercept_request(self, endpoint: str, payload: Dict[str, Any], headers: Dict[str, str]) -> Optional[str]:
        """
        既存製品へ到達する前のリクエストをインターセプトし、Pre-Auditとサンドボックス隔離を行う（裏の顔・表の顔の統合防衛）。
        """
        nonce = headers.get("X-Shisei-Nonce", "")
        timestamp_ms = int(headers.get("X-Shisei-Timestamp", "0"))
        signature = headers.get("X-Shisei-Signature", "")

        logger.info(f"黒衣: エンドポイント [{endpoint}] へのリクエストを捕捉しました。プレ監査を実行します。")

        # 1. 影法師によるプレ監査（Nonce、タイムウィンドウ、署名検証）
        pre_passed = self._kageboushi.pre_audit(payload, nonce, timestamp_ms, signature)
        if not pre_passed:
            logger.critical("黒衣: Pre-Audit不合格のため、リクエストを完全に遮断します。")
            return None

        # 2. 蜘蛛の糸によるトランザクションのサンドボックス隔離（副作用の保護）
        agent_id = payload.get("agent_id", "default_agent")
        tx_id = self._sandbox.begin_transaction(agent_id, payload)
        
        return tx_id

    def intercept_response(self, tx_id: str, ai_output: Dict[str, Any], expected_schema_hash: str) -> Optional[Dict[str, Any]]:
        """
        既存製品のAI出力結果をインターセプトし、Post-Audit検証を経てコミットまたはパージを行う。
        """
        logger.info(f"黒衣: トランザクション [{tx_id}] のAI出力を捕捉しました。ポスト監査を実行します。")

        # 1. 影法師によるポスト監査（出力意味論・漏洩チェック）
        post_passed = self._kageboushi.post_audit(ai_output, expected_schema_hash)

        # 2. 蜘蛛の糸によるコミットまたは完全破棄の執行
        committed_data = self._sandbox.commit_transaction(tx_id, post_passed)
        
        if committed_data is None:
            logger.critical("【黒衣防衛発動】AI出力に不正または不整合を検知しました。副作用をサンドボックスごとパージします。")
            return {"status": "BLOCKED", "reason": "SHISEI_PROTOCOL_VIOLATION_PURGED"}

        return {"status": "APPROVED", "data": ai_output}
