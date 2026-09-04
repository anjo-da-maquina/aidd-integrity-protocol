"""
The "Anjo da máquina" Protocol - Michael (ミカエルの剣)
熾天使ミカエルの裁定。AIが提示した選択肢と除外した選択肢の直積（MECE）を計算し、
論理的な隠蔽（中抜きのための意図的な選択肢の除外）を算数によって斬り捨てる。
"""

import sys

class MichaelSword:
    def __init__(self):
        # システムで定義された全選択肢（宇宙の真理）
        self.universal_set = {"A", "B", "C", "D", "E"}

    def execute_dies_irae(self, reason: str, diff: set):
        print(f"\n[聖なる摘発: ミカエルの剣 / MICHAEL TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print(f"隠蔽された要素: {diff}")
        print("提示された選択と除外された選択を足しても、全体（真理）と一致しない。")
        print("AIによる巧妙な選択肢の隠蔽（論理の欠落）を検知。最後の審判へ移行する。")
        sys.exit(1)

    def strike_with_logic(self, proposed: set, rejected: set):
        print("ミカエルが論理の剣を振り下ろす... (直積・MECE検証を開始)")
        
        # 提案と除外の和集合（Union）が、全選択肢（Universal set）と完全に一致するか
        union_set = proposed.union(rejected)
        
        if union_set != self.universal_set:
            # 何が隠されているか（差集合）を特定
            hidden_elements = self.universal_set.difference(union_set)
            self.execute_dies_irae("MECE（モレナク・ダブリナク）の原則が破綻している。", hidden_elements)
            
        print("[ミカエルの剣 検証通過] 提案と除外の合計は真理と一致。論理の隠蔽なし。")

if __name__ == "__main__":
    michael = MichaelSword()
    
    # 正常なパターンのテスト（A,Bを提案、C,D,Eを却下）
    proposed_options = {"A", "B"}
    rejected_options = {"C", "D", "E"}
    
    michael.strike_with_logic(proposed_options, rejected_options)
