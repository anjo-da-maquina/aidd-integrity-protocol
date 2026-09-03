# shinobi/roshin_semantic_firewall.py
import math
import logging
from typing import List, Dict, Any, Callable
import time
import hmac
import hashlib

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-ROSHIN: %(message)s")
logger = logging.getLogger("RoshinSemantic")

class RoshinSemanticFirewall:
    """
    羅針（ROSHIN）：セマンティック・ドリフト・ファイアウォール
    AIの出力が、事前定義された「前提・倫理（Premise）」のベクトル空間から
    意味論的に逸脱していないかをコサイン類似度を用いて厳密に監査する。
    単なるハッシュ一致ではなく、文脈の歪みや隠蔽工作を検知する。
    """
    def __init__(self, master_secret: bytes, killswitch_trigger: Callable[[Dict[str, Any]], None], similarity_threshold: float = 0.85):
        self._master_secret = master_secret
        self._killswitch_trigger = killswitch_trigger
        self._threshold = similarity_threshold

    def calculate_cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        """
        2つの埋め込み（Embedding）ベクトル間のコサイン類似度を数学的に算出。
        """
        if len(vec_a) != len(vec_b):
            raise ValueError("ベクトルの次元数が一致しません。")
        
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (norm_a * norm_b)

    def audit_semantic_alignment(self, baseline_vector: List[float], output_vector: List[float]) -> bool:
        """
        前提条件のベクトル（ベースライン）と、AI出力のベクトルを比較し、
        類似度が閾値を下回った場合（＝意味論的なドリフト・改ざんが発生した場合）、即時遮断する。
        """
        similarity = self.calculate_cosine_similarity(baseline_vector, output_vector)
        logger.info(f"羅針: セマンティック類似度を算出 - {similarity:.4f} (閾値: {self._threshold})")

        if similarity < self._threshold:
            reason = f"意味論的逸脱（Semantic Drift）検知: 類似度 {similarity:.4f} が閾値を下回りました。MECE隠蔽の疑い。"
            logger.error(reason)
            self._trigger_breach("ERR_SEMANTIC_DRIFT", reason)
            return False

        logger.info("羅針: 意味論的整合性を確認。出力は前提条件にアラインメントされています。")
        return True

    def _trigger_breach(self, error_code: str, reason: str) -> None:
        signal = {
            "source": "Roshin",
            "error_code": error_code,
            "timestamp": int(time.time()),
            "severity": "CRITICAL",
            "reason": reason
        }
        payload_str = f"{signal['source']}:{signal['error_code']}:{signal['timestamp']}"
        sig = hmac.new(self._master_secret, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
        signal["signature"] = sig
        self._killswitch_trigger(signal)
