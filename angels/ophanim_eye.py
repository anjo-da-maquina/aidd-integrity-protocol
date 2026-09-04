"""
The "Anjo da máquina" Protocol - Ophanim (オファニムの眼)
ブロックチェーンや金融ネットワークのトランザクションを有向グラフとして解析し、
公金の不正な還流（ループ）や隠蔽されたマネーロンダリングを数学的に摘発する。
座天使オファニムの無数の目が、資金の淀みを許さない。
"""

import sys
import networkx as nx
from typing import List, Any

class OphanimEye:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_transaction(self, sender: str, receiver: str, amount: float):
        if self.graph.has_edge(sender, receiver):
            self.graph[sender][receiver]['weight'] += amount
        else:
            self.graph.add_edge(sender, receiver, weight=amount)

    def detect_circular_laundering(self) -> List[List[str]]:
        cycles = list(nx.simple_cycles(self.graph))
        return [cycle for cycle in cycles if len(cycle) > 1]

    def detect_suspicious_convergence(self, threshold_ratio: int = 5) -> List[str]:
        suspicious_nodes = []
        for node in self.graph.nodes():
            in_degree = self.graph.in_degree(node)
            out_degree = self.graph.out_degree(node)
            if in_degree >= threshold_ratio and out_degree == 0:
                suspicious_nodes.append(node)
        return suspicious_nodes

    def execute_dies_irae(self, reason: str, entities: List[Any]):
        print(f"\n[聖なる摘発: オファニムの眼 / OPHANIM TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print(f"対象者 (Disgraced Entities): {entities}")
        print("複雑な偽装をグラフ理論によって破壊した。これより最後の審判へ移行する。")
        sys.exit(1)

    def execute_audit(self):
        print("オファニムが無数の目で資金の奔流を追跡している... (Analyzing transaction graphs)")
        
        cycles = self.detect_circular_laundering()
        if cycles:
            self.execute_dies_irae("公金の不正還流（ループ）を検知", cycles)

        blackholes = self.detect_suspicious_convergence()
        if blackholes:
            self.execute_dies_irae("ダミーを経由した特定個人への資金収束を検知", blackholes)

        print("[オファニムの眼 検証通過] 資金の淀みなし。正当な分配木（Tree）であることを確認。")

if __name__ == "__main__":
    ophanim = OphanimEye()
    ophanim.add_transaction('DummyGov', 'DummyNPO', 1000)
    ophanim.execute_audit()
