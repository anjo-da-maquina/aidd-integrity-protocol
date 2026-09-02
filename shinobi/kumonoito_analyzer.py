"""
The SHINOBI Protocol - Kumonoito (蜘蛛の糸) Analyzer
ブロックチェーンのトランザクションを有向グラフとして解析し、
公金の不正な還流（ループ）や隠蔽されたマネーロンダリングを数学的に摘発する。
"""

import sys
import networkx as nx
from typing import List, Tuple, Dict

class KumonoitoAnalyzer:
    def __init__(self):
        # 資金の流れを管理する有向グラフ（Directed Graph）
        self.graph = nx.DiGraph()

    def add_transaction(self, sender: str, receiver: str, amount: float):
        """トランザクションをグラフの「エッジ（辺）」として追加する"""
        if self.graph.has_edge(sender, receiver):
            self.graph[sender][receiver]['weight'] += amount
        else:
            self.graph.add_edge(sender, receiver, weight=amount)

    def detect_circular_laundering(self) -> List[List[str]]:
        """
        還流検知：A -> B -> C -> A のような資金のループ構造（閉路）を見つけ出す。
        公金の分配においてループが発生することは論理的にあり得ず、100%不正である。
        """
        cycles = list(nx.simple_cycles(self.graph))
        illicit_cycles = [cycle for cycle in cycles if len(cycle) > 1]
        return illicit_cycles

    def detect_suspicious_convergence(self, threshold_ratio: int = 5) -> List[str]:
        """
        収束検知：多数のダミー団体から特定の1つのアドレスへ不自然に資金が
        集まっている（In-Degreeが極端に高い）ブラックホール・アドレスを特定する。
        """
        suspicious_nodes = []
        for node in self.graph.nodes():
            in_degree = self.graph.in_degree(node)
            out_degree = self.graph.out_degree(node)
            
            # 多数から受け取っているのに、他に一切分配していないノード
            if in_degree >= threshold_ratio and out_degree == 0:
                suspicious_nodes.append(node)
                
        return suspicious_nodes

    def expose_shame(self, reason: str, entities: List[Any]):
        """暗闇から引きずり出し、恥を公開する（社会的な死の宣告）"""
        print(f"\n[暗部摘発: 蜘蛛の糸 / KUMONOITO TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print(f"対象者 (Disgraced Entities): {entities}")
        print("複雑な偽装をグラフ理論によって破壊した。これらの一族郎党をシステムから永久追放する。")

    def execute_audit(self):
        """常駐監査プロセス"""
        print("蜘蛛の糸を張り巡らせている... (Analyzing transaction graphs)")
        
        # 1. ループ構造（還流）の監査
        cycles = self.detect_circular_laundering()
        if cycles:
            self.expose_shame("公金の不正還流（ループ）を検知", cycles)
            sys.exit(1) # 腹切り（即時停止）

        # 2. 資金の不自然な収束の監査
        blackholes = self.detect_suspicious_convergence()
        if blackholes:
            self.expose_shame("ダミーを経由した特定個人への資金収束を検知", blackholes)
            sys.exit(1)

        print("[監査完了] 資金の淀みなし。正当な分配木（Tree）であることを確認。")
