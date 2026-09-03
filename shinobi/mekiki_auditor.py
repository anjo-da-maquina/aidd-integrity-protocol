"""
The SHINOBI Protocol - Mekiki (目利き) Smart Contract Auditor
ブロックチェーンにデプロイされるスマートコントラクト（影縫い・水月）の鑑定。
悪意ある者によって「腹切り（revert）」のロジックが密かに削除されたり、
無効化されたりしていないかを静的解析で監査し、刃の鋭さを担保する。
"""

import sys
from pathlib import Path

class MekikiAuditor:
    def __init__(self, contracts_dir: str):
        self.contracts_dir = Path(contracts_dir)
        # 各コントラクトに必ず存在しなければならない「致命の刃（必須文字列）」
        self.required_blades = {
            "ZKDistribution.sol": 'revert("Harakiri:',
            "SuigetsuHoneypot.sol": 'revert("Harakiri:'
        }

    def execute_harakiri(self, reason: str):
        """刃こぼれ（ロジックの弱体化）を検知し、システムを処断する"""
        print(f"\n[暗部摘発: 目利き / MEKIKI TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print("スマートコントラクトから『腹切り』のロジックが意図的に削られている。")
        print("牙を抜かれた防壁に価値はない。内部犯行とみなし、これより切腹を実行する。")
        sys.exit(1)

    def appraise_swords(self):
        """鍛え上げられたSolidityファイルの刃を鑑定する"""
        print("目利きが刀（スマートコントラクト）の刃文を鑑定している...")

        if not self.contracts_dir.exists():
            self.execute_harakiri(f"コントラクトの格納庫 ({self.contracts_dir}) が存在しない。")

        for contract_name, required_blade in self.required_blades.items():
            contract_path = self.contracts_dir / contract_name
            
            if not contract_path.exists():
                self.execute_harakiri(f"必須の武具 '{contract_name}' が紛失している。")

            content = contract_path.read_text(encoding="utf-8")
            
            if required_blade not in content:
                self.execute_harakiri(
                    f"'{contract_name}' の中に致命の刃（{required_blade}）が見当たらない。"
                )
            
            print(f"[目利き] {contract_name} の鑑定完了。刃こぼれなし。鋭利な殺意を確認。")

        print("[目利き 検証通過] すべてのスマートコントラクトは実戦投入可能（Deployable）である。")

if __name__ == "__main__":
    # shinobi/contracts ディレクトリ内の .sol ファイルを監査する
    contracts_path = "shinobi/contracts"
    mekiki = MekikiAuditor(contracts_path)
    mekiki.appraise_swords()
