# shinobi/jukai_merkle_tree.py
import hashlib
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-JUKAI: %(message)s")
logger = logging.getLogger("JukaiMerkleTree")

class JukaiMerkleTree:
    """
    受戒（JUKAI）：イミュータブル・マークルツリー監査証跡
    発生したすべてのイベント、トランザクション、監査結果を葉（Leaf）として追加し、
    暗号学的なマークルツリーを構築。事後的な隠蔽やログの改ざんを数学的に不可能にする。
    """
    def __init__(self):
        self._leaves: List[str] = []
        self._tree: List[List[str]] = []

    def append_audit_trail(self, data_str: str) -> str:
        """
        新規の監査イベントをツリーの葉として追加し、リーフハッシュを返す。
        """
        leaf_hash = hashlib.sha256(data_str.encode('utf-8')).hexdigest()
        self._leaves.append(leaf_hash)
        logger.info(f"受戒: 新たな監査証跡を刻み込みました。Leaf Hash: {leaf_hash[:16]}...")
        return leaf_hash

    def compute_merkle_root(self) -> str:
        """
        現在のすべての葉からマークルツリーを再構築し、ルートハッシュ（Root Hash）を算出。
        これにより、これまでの全履歴の完全性が単一のハッシュで証明される。
        """
        if not self._leaves:
            return hashlib.sha256(b"").hexdigest()

        current_level = self._leaves.copy()
        self._tree = [current_level]

        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                node_left = current_level[i]
                node_right = current_level[i + 1] if i + 1 < len(current_level) else node_left
                combined = f"{node_left}{node_right}"
                node_hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
                next_level.append(node_hash)
            
            self._tree.append(next_level)
            current_level = next_level

        root_hash = current_level[0]
        logger.info(f"受戒: マークルルートが確定しました。Root Hash: {root_hash}")
        return root_hash

    def verify_leaf_integrity(self, index: int, expected_leaf_hash: str) -> bool:
        """
        特定の証跡が改ざんされずにツリー内に存在しているかを検証。
        """
        if index < 0 or index >= len(self._leaves):
            return False
        is_valid = hmac.compare_digest(self._leaves[index], expected_leaf_hash)
        if not is_valid:
            logger.critical(f"【受戒 整合性崩壊】インデックス {index} の監査証跡に改ざんの痕跡を検知。")
        return is_valid
