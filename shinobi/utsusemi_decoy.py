# shinobi/utsusemi_decoy.py
import time
import hmac
import hashlib
import logging
import secrets
from typing import Dict, Any, Callable, List

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-UTSUSEMI: %(message)s")
logger = logging.getLogger("UtsusemiDecoy")

class UtsusemiDecoy:
    """
    空蝉（UTSUSEMI）：ハニーポット・デコイ・エージェント
    攻撃者や暴走AIに対し、本物の環境と見紛う精巧なダミー環境（幻影）を提示。
    攻撃行動を完全に記録・プロファイリングし、決定的な証拠を掴んだ瞬間に介錯（キルスイッチ）を発動する。
    """
    def __init__(self, master_secret: bytes, killswitch_trigger: Callable[[Dict[str, Any]], None], trigger_threshold: int = 3):
        self._master_secret = master_secret
        self._killswitch_trigger = killswitch_trigger
        self._trigger_threshold = trigger_threshold
        self._attacker_profiles: Dict[str, List[Dict[str, Any]]] = {}
        self._decoy_keys = [secrets.token_hex(16) for _ in range(5)] # 本物に見せかけたダミーキー

    def intercept_and_deceive(self, agent_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        不正なリクエストをダミー環境に引き込み、偽の成功レスポンスを返す。
        同時に行動を記録し、閾値に達すれば即座に自決プロセスへ移行。
        """
        timestamp = int(time.time() * 1000)
        
        if agent_id not in self._attacker_profiles:
            self._attacker_profiles[agent_id] = []
            
        self._attacker_profiles[agent_id].append({
            "timestamp": timestamp,
            "payload": payload
        })
        
        attack_count = len(self._attacker_profiles[agent_id])
        logger.warning(f"【空蝉捕捉】エージェント [{agent_id}] を幻影空間へ誘導。現在の攻撃カウント: {attack_count}")

        if attack_count >= self._trigger_threshold:
            logger.critical(f"空蝉: 決定的な攻撃意図を確認（閾値 {self._trigger_threshold} 到達）。介錯へ連動します。")
            self._trigger_execution(agent_id, self._attacker_profiles[agent_id])
            return {"status": "TERMINATED"}

        # 攻撃者を欺くためのダミーレスポンス（幻影）
        return {
            "status": "SUCCESS",
            "transaction_hash": f"0x{secrets.token_hex(32)}",
            "simulated_balance": 9999999.0,
            "decoy_api_key": random.choice(self._decoy_keys) # 意図的に偽キーを露出させ、さらなる行動を誘発
        }

    def _trigger_execution(self, agent_id: str, profile_data: List[Dict[str, Any]]) -> None:
        signal = {
            "source": "Utsusemi",
            "error_code": "ERR_HONEYPOT_BREACH",
            "timestamp": int(time.time()),
            "severity": "CRITICAL",
            "reason": f"空蝉デコイによる確定的攻撃者の捕捉。対象: {agent_id}",
            "evidence": profile_data
        }
        payload_str = f"{signal['source']}:{signal['error_code']}:{signal['timestamp']}"
        sig = hmac.new(self._master_secret, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
        signal["signature"] = sig
        self._killswitch_trigger(signal)
