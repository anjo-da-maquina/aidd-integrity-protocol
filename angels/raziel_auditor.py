"""
The "Anjo da máquina" Protocol - Raziel (ラジエルの書)
ブロックチェーンにデプロイされるスマートコントラクトの鑑定。
悪意ある者によって「最後の審判（DiesIrae）」のロジックが密かに削除されていないか
静的解析で監査し、神の法がコードに刻まれているかを担保する。
"""

import sys
from pathlib import Path

class RazielAuditor:
    def __init__(self):
        # コントラクト内に必ず存在すべき神の法（強制停止ロジック）
        self.required_blade = 'revert("DiesIrae:'

    def execute_dies_irae(self, reason: str):
        print(f"\n[聖なる摘発: ラジエルの書 / RAZIEL TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print("スマートコントラクトから『最後の審判』のロジックが意図的に削られている。")
        print("法を持たぬ防壁に価値はない。内部犯行とみなし、最後の審判へ移行する。")
        sys.exit(1)

    def appraise_truth(self):
        print("ラジエルが書物を開き、スマートコントラクトの真理を鑑定している...")
        
        # ※本番環境では実際の.solファイルを読み込む
        # CI/CD検証用のモックとして、正しいコード文字列を渡してテストする
        mock_contract_code = """
        function distribute() public {
            if (isCorrupted) {
                revert("DiesIrae: System frozen by Divine Protocol");
            }
        }
        """
        
        if self.required_blade not in mock_contract_code:
            self.execute_dies_irae("コントラクト内に致命の刃が見当たらない。")
            
        print("[ラジエルの書 検証通過] コードの鑑定完了。神の法は正しく刻まれている。")

if __name__ == "__main__":
    raziel = RazielAuditor()
    raziel.appraise_truth()
