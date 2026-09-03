# shinobi/kageboushi_middleware.py
import time
import hmac
import hashlib
import logging
from typing import Dict, Any, Callable, Set

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-KAGEBOUSHI: %(message)s")
logger = logging.getLogger("KageboushiMiddleware")

class KageboushiMiddleware:
    """
    影法師（KAGEBOUSHI）：常駐型ミドルウェア
    すべての入力（Pre-Audit）と出力（Post-Audit）に対し、
    Nonce検証、タイムウィンドウ制限、ハッシュ照合をミリ秒単位で強制する。
    """
    def __init__(self, master_secret: bytes, killswitch_trigger: Callable[[Dict[str, Any]], None], max_drift_ms: int = 200):
        self._master_secret = master_secret
        self._killswitch_trigger = killswitch_trigger
        self._max_drift_ms = max_drift_ms
        self._used_nonces: Set[str] = set()

    def pre_audit(self, payload: Dict[str, Any], nonce: str, timestamp_ms: int, signature: str) -> bool:
        """
        実行前監査（Pre-Audit）: 
        リプレイ攻撃、時間同期のズレ、および入力ペイロードの改ざんを検知する。
        """
        current_time_ms = int(time.time() * 1000)
        
        # 1. タイムウィンドウ検証（ミリ秒単位）
        if abs(current_time_ms - timestamp_ms) > self._max_drift_ms:
            reason = f"タイムウィンドウ違反: 許容範囲({self._max_drift_ms}ms)を超えたリクエストです。差分: {abs(current_time_ms - timestamp_ms)}ms"
            logger.error(reason)
            self._trigger_breach("ERR_TIME_WINDOW_DRIFT", reason)
            return False

        # 2. Nonce重複検証（リプレイ攻撃対策）
        if nonce in self._used_nonces:
            reason = f"リプレイ攻撃検知: 既に消費されたNonce '{nonce}' が再利用されました。"
            logger.error(reason)
            self._trigger_breach("ERR_NONCE_REPLAY", reason)
            return False
        
        # Nonceの消費登録
        self._used_nonces.add(nonce)

        # 3. 署名（改ざん）検証
        raw_data = f"{nonce}:{timestamp_ms}:{str(payload)}"
        expected_sig = hmac.new(self._master_secret, raw_data.encode('utf-8'), hashlib.sha256).hexdigest()

        if not hmac.compare_digest(expected_sig, signature):
            reason = "ペイロード改ざん検知: 入力データの署名が一致しません。"
            logger.error(reason)
            self._trigger_breach("ERR_PAYLOAD_TAMPERING", reason)
            return False

        logger.info("Pre-Audit 正常通過: 整合性、時間、Nonceの検証に成功しました。")
        return True

    def post_audit(self, output_data: Dict[str, Any], expected_schema_hash: str) -> bool:
        """
        実行後監査（Post-Audit）:
        AIの出力結果が期待されるスキーマおよび論理制約（蛍火・水鏡・蛇の統合）に適合しているかを検証する。
        """
        output_str = str(output_data)
        actual_hash = hashlib.sha256(output_str.encode('utf-8')).hexdigest()

        if not hmac.compare_digest(actual_hash, expected_schema_hash):
            reason = "出力不整合検知: AIの出力結果が事前定義された不変要件ハッシュと一致しません。"
            logger.error(reason)
            self._trigger_breach("ERR_POST_AUDIT_MISMATCH", reason)
            return False

        logger.info("Post-Audit 正常通過: 出力の整合性が確認されました。")
        return True

    def _trigger_breach(self, error_code: str, reason: str) -> None:
        signal = {
            "source": "Kageboushi",
            "error_code": error_code,
            "timestamp": int(time.time()),
            "severity": "CRITICAL",
            "reason": reason
        }
        # 署名を付与してキルスイッチへ転送
        payload_str = f"{signal['source']}:{signal['error_code']}:{signal['timestamp']}"
        sig = hmac.new(self._master_secret, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
        signal["signature"] = sig
        
        self._killswitch_trigger(signal)
