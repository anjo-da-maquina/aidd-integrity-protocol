"""
The SHINOBI Protocol - Hebi (蛇) Oracle
Tactical Espionage Audit: 実世界の情報を無音で照会し、デジタル上の偽装を見破る単独潜入エージェント。
ブロックチェーンの正当性を物理世界の事実で裏付け、シビル攻撃（ペーパーカンパニー）を粉砕する。
"""

import sys
from typing import Dict, Any

class HebiOracle:
    def __init__(self):
        # 既知のバーチャルオフィスや、マネーロンダリングに頻用される
        # ブラックリスト化されたダミー拠点のハッシュプール
        self.blacklisted_address_hashes = {
            "v_office_tokyo_01",
            "v_office_osaka_03"
        }

    def execute_harakiri(self, reason: str, entity_name: str):
        """物理世界の虚飾を暴き、システムを停止する（任務実行）"""
        print(f"\n[暗部摘発: 蛇 / HEBI TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print(f"対象偽装団体: {entity_name}")
        print("帳簿の数字は完璧に偽装されていたが、物理世界の『実体』が存在しない。")
        print("ペーパーカンパニーによる公金詐取を検知。これより切腹（プロセス抹消）を実行する。")
        sys.exit(1)

    def verify_physical_entity(self, entity_data: Dict[str, Any]):
        """
        対象団体の実在性を裏で（対象に気付かれずに）検証する。
        """
        entity_name = entity_data.get("name", "Unknown")
        corp_id = entity_data.get("corporate_id")
        address_hash = entity_data.get("address_hash")

        print(f"蛇が単独潜入を開始... {entity_name} の物理的実体を照会中。")

        # 1. 法人番号の実在確認
        if not corp_id or len(str(corp_id)) != 13:
            self.execute_harakiri(
                "法人番号（13桁）が不正、あるいは未登録である。実在しない幻の団体。", 
                entity_name
            )

        # 2. 拠点の物理的実体チェック
        if address_hash in self.blacklisted_address_hashes:
            self.execute_harakiri(
                "登録住所が多数のダミー法人が共有する拠点（偽装基地）と一致した。空箱である。", 
                entity_name
            )

        # 3. 設立年月日の異常検知
        is_sudden_establishment = entity_data.get("is_newly_established", False)
        if is_sudden_establishment:
             self.execute_harakiri(
                "公金受給の直前に急造された法人である。典型的なペーパーカンパニーの手口。", 
                entity_name
            )

        print(f"[蛇 帰還] {entity_name} に物理的な偽装なし。任務完了。")

# --- 試し斬り（テスト実行用） ---
if __name__ == "__main__":
    oracle = HebiOracle()
    
    # 正常な法人のテスト
    valid_entity = {
        "name": "NPO法人 真正なる救済",
        "corporate_id": "1234567890123",
        "address_hash": "real_building_hash_88",
        "is_newly_established": False
    }
    oracle.verify_physical_entity(valid_entity)

    # 異常な法人のテスト（ここで腹切りが発動し、プログラムが止まる）
    dummy_entity = {
        "name": "一般社団法人 幻影福祉機構",
        "corporate_id": "9999999999999",
        "address_hash": "v_office_tokyo_01", # ブラックリスト住所
        "is_newly_established": True
    }
    oracle.verify_physical_entity(dummy_entity)
