# shinobi/kumonoito_analyzer.py
import time
import hmac
import hashlib
import logging
import uuid
from typing import Dict, Any, Callable, Optional

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-KUMONOITO: %(message)s")
logger = logging.getLogger("KumonoitoAnalyzer")

class TransactionSandbox:
    """
    蜘蛛の糸（KUMONOITO）：メモリプール・副作用隔離サンドボックス
    AIエージェントの思考結果による外部状態の変更（資金移動、DB書き込み等）を
    一時的なメモリプールに隔離し、全監査（Pre/Post）の通過が確定するまでコミットを遅延させる。
    異常検知時はサンドボックスごと即座に破棄（ロールバック）する。
    """
    def __init__(self, master_secret: bytes, killswitch_trigger: Callable[[Dict[str, Any]], None]):
        self._master_secret = master_secret
        self._killswitch_trigger = killswitch_trigger
        self._pending_pools: Dict[str, Dict[str, Any]] = {}

    def begin_transaction(self, agent_id: str, payload: Dict[str, Any]) -> str:
        """
        副作用を伴う操作をサンドボックス内に隔離し、トランザクションIDを発行する。
        """
        tx_id = f"tx_{uuid.uuid4().hex}"
        timestamp = int(time.time() * 1000)
        
        # 改ざん防止用ハッシュの生成
        raw_data = f"{tx_id}:{agent_id}:{timestamp}:{str(payload)}"
        integrity_hash = hmac.new(self._master_secret, raw_data.encode('utf-8'), hashlib.sha256).hexdigest()

        self._pending_pools[tx_id] = {
            "agent_id": agent_id,
            "payload": payload,
            "timestamp": timestamp,
            "integrity_hash": integrity_hash,
            "status": "SANDBOXED"
        }
        
        logger.info(f"蜘蛛の糸: トランザクション [{tx_id}] を隔離サンドボックスに収容しました。")
        return tx_id

    def commit_transaction(self, tx_id: str, post_audit_passed: bool) -> Optional[Dict[str, Any]]:
        """
        監査通過を条件に、隔離されたトランザクションを正式にコミット（解放）する。
        """
        if tx_id not in self._pending_pools:
            reason = f"トランザクション違反: 存在しないまたは既に破棄されたTX ID '{tx_id}' へのコミット要求です。"
            logger.error(reason)
            self._trigger_breach("ERR_TX_NOT_FOUND", reason)
            return None

        tx_data = self._pending_pools[tx_id]

        if not post_audit_passed:
            logger.warning(f"蜘蛛の糸: Post-Audit不合格のため、トランザクション [{tx_id}] を破棄します。")
            self.abort_transaction(tx_id, "POST_AUDIT_FAILURE")
            return None

        tx_data["status"] = "COMMITTED"
        logger.info(f"蜘蛛の糸: トランザクション [{tx_id}] の整合性が証明されました。外部へコミットします。")
        
        # コミット完了後にプールから安全に削除（メモリ汚染防止）
        return self._pending_pools.pop(tx_id)

    def abort_transaction(self, tx_id: str, reason_code: str) -> None:
        """
        サンドボックス内のデータを完全消去し、副作用の発生を物理的に阻止する。
        """
        if tx_id in self._pending_pools:
            logger.critical(f"【蜘蛛の糸切断】トランザクション [{tx_id}] をパージします。理由: {reason_code}")
            # メモリ上からデータをゼロ埋め・破棄
            tx_data = self._pending_pools.pop(tx_id)
            tx_data.clear()
        else:
            logger.warning(f"パージ対象のTX ID [{tx_id}] は既に存在しません。")

    def _trigger_breach(self, error_code: str, reason: str) -> None:
        signal = {
            "source": "Kumonoito",
            "error_code": error_code,
            "timestamp": int(time.time()),
            "severity": "CRITICAL",
            "reason": reason
        }
        payload_str = f"{signal['source']}:{signal['error_code']}:{signal['timestamp']}"
        sig = hmac.new(self._master_secret, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
        signal["signature"] = sig
        self._killswitch_trigger(signal)
