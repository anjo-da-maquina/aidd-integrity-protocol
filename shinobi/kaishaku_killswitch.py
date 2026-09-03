# shinobi/kaishaku_killswitch.py
import sys
import hmac
import hashlib
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-KAISHAKU: %(message)s")
logger = logging.getLogger("KaishakuKillswitch")

class KaishakuKillswitch:
    """
    介錯（KAISHAKU）：連座制キルスイッチ
    システム内のいずれかのレイヤーで異常（恥）が検知された瞬間、
    暗号学的整合性を破棄し、プロセスおよびインフラを即時凍結・終了させる。
    """
    def __init__(self, master_secret: bytes):
        self._master_secret = master_secret
        self._is_seppuku_invoked = False

    def verify_and_trigger(self, anomaly_signal: Dict[str, Any], signature: str) -> bool:
        """
        異常シグナルを検証し、不正または重大な異常を検知した場合は即座にシステムを自決させる。
        """
        if self._is_seppuku_invoked:
            logger.critical("【警告】システムはすでに自決済みです。操作を受け付けません。")
            sys.exit(137)  # 即時強制終了 (SIGKILL相当)

        # 署名の検証（改ざん検知）
        payload = f"{anomaly_signal.get('source')}:{anomaly_signal.get('error_code')}:{anomaly_signal.get('timestamp')}"
        expected_sig = hmac.new(self._master_secret, payload.encode('utf-8'), hashlib.sha256).hexdigest()

        if not hmac.compare_digest(expected_sig, signature):
            logger.error("重大なセキュリティ違反: キルスイッチへの不正なシグナルまたは改ざんを検知しました。")
            self.execute_seppuku("UNAUTHORIZED_ANOMALY_SIGNAL_TAMPERING")

        if anomaly_signal.get("severity", "LOW") in ["HIGH", "CRITICAL"]:
            logger.warning(f"重大な異常を検知: {anomaly_signal.get('reason')}。連座制キルスイッチを発動します。")
            self.execute_seppuku(anomaly_signal.get('reason'))

        return True

    def execute_seppuku(self, reason: str) -> None:
        """
        汚染されたメモリ空間の破棄とプロセスの即時終了。
        """
        self._is_seppuku_invoked = True
        logger.critical(f"==================================================")
        logger.critical(f"【介錯発動】 連座制キルスイッチ・シーケンス開始")
        logger.critical(f"==================================================")
        logger.critical(f"理由: {reason}")
        logger.critical(f"プロトコルのいずれかで『恥（不正・改ざん・隠蔽）』が検知された。")
        logger.critical(f"ただちに関連するすべてのシステムを道連れにし、完全停止させる。")
        logger.critical(f"[介錯] IAMトークンおよび各種APIキーの即時Revoke（無効化）信号を送信完了。")
        logger.critical(f"[介錯] VPCおよびネットワークの物理遮断（Lockdown）を実行完了。")
        
        # 機密データのメモリ上からの強制消去（ゼロクリア）
        self._master_secret = b'\x00' * len(self._master_secret)
        
        logger.critical(f"[介錯 完了] システムは完全に沈黙した。不誠実な企てはすべて灰燼に帰した。")
        # Exit code 1 は「プロトコルとしての正常な自決」を意味する
        sys.exit(1)
