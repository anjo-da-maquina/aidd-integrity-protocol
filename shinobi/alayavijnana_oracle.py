# shinobi/alayavijnana_oracle.py
import logging
import time
import hmac
import hashlib
from typing import Dict, Any, List, Set

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-ALAYAVIJNANA: %(message)s")
logger = logging.getLogger("AlayavijnanaOracle")

class AlayavijnanaOracle:
    """
    阿頼耶識（ALAYAVIJNANA）：分散型ビザンチン合意監査オーラクル
    インフラ内の単一障害点（SPOF）を排除するため、複数ノードによるBFT投票を実施。
    (2/3 + 1) の定足数（Quorum）を満たさない限り、資金移動などの高リスク操作を承認しない。
    """
    def __init__(self, node_secrets: Dict[str, bytes]):
        """
        node_secrets: 各監査ノード（例: node_1, node_2, node_3...）が持つ個別の署名キー
        """
        self._nodes = node_secrets
        self._total_nodes = len(node_secrets)
        # BFT定足数: N = 3f + 1 を前提とした 2f + 1 のマジョリティ
        self._quorum_needed = (2 * self._total_nodes // 3) + 1
        logger.info(f"阿頼耶識: 総ノード数 {self._total_nodes} / 必要定足数 {self._quorum_needed}")

    def request_consensus(self, transaction_hash: str, node_signatures: Dict[str, str]) -> bool:
        """
        各ノードから提出された署名（投票）を暗号学的に検証し、
        合意形成（Consensus）に達したかを確認する。
        """
        valid_votes: Set[str] = set()

        for node_id, signature in node_signatures.items():
            if node_id not in self._nodes:
                logger.warning(f"阿頼耶識: 未知のノード [{node_id}] からの投票を破棄。")
                continue

            # ノード固有の秘密鍵を用いた署名検証
            node_secret = self._nodes[node_id]
            expected_sig = hmac.new(node_secret, transaction_hash.encode('utf-8'), hashlib.sha256).hexdigest()

            if hmac.compare_digest(expected_sig, signature):
                valid_votes.add(node_id)
            else:
                logger.error(f"阿頼耶識: ノード [{node_id}] の署名が不正または改ざんされています。")

        vote_count = len(valid_votes)
        logger.info(f"阿頼耶識: トランザクション [{transaction_hash[:16]}...] に対する有効票数: {vote_count}")

        if vote_count >= self._quorum_needed:
            logger.info("【阿頼耶識 合意形成】定足数を満たしました。高リスク操作の監査を可決します。")
            return True
        else:
            logger.critical("【阿頼耶識 否決】ビザンチン合意に至りませんでした。システム内に汚染ノードが存在する可能性があります。")
            return False
