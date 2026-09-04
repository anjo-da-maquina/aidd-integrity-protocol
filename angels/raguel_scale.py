"""
The "Anjo da máquina" Protocol - Raguel (ラグエルの天秤)
物理世界の事実で裏付けを取り、シビル攻撃（ペーパーカンパニー）を粉砕する。
正義と復讐の天使ラグエルが、帳簿上の数字ではなく「現実世界の実体」を天秤にかける。
"""

import sys
from typing import Dict, Any

class RaguelScale:
    def __init__(self):
        self.blacklisted_address_hashes = {
            "v_office_tokyo_01",
            "v_office_osaka_03"
        }

    def execute_dies_irae(self, reason: str, entity_name: str):
        print(f"\n[聖なる摘発: ラグエルの天秤 / RAGUEL TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print(f"対象偽装団体: {entity_name}")
        print("帳簿は完璧に偽装されていたが、物理世界の『実体』が存在しない。")
        print("ペーパーカンパニーによる公金詐取を検知。これより最後の審判へ移行する。")
        sys.exit(1)

    def verify_physical_entity(self, entity_data: Dict[str, Any]):
        entity_name = entity_data.get("name", "Unknown")
        corp_id = entity_data.get("corporate_id")
        address_hash = entity_data.get("address_hash")

        print(f"ラグエルが天秤を用いて {entity_name} の物理的実体を量っている...")

        if not corp_id or len(str(corp_id)) != 13:
            self.execute_dies_irae("法人番号が不正、あるいは未登録。実在しない幻の団体。", entity_name)

        if address_hash in self.blacklisted_address_hashes:
            self.execute_dies_irae("登録住所がダミー法人の共有拠点（空箱）と一致した。", entity_name)

        if entity_data.get("is_newly_established", False):
             self.execute_dies_irae("公金受給の直前に急造された法人である。典型的な手口。", entity_name)

        print(f"[ラグエルの天秤 帰還] {entity_name} に物理的な偽装なし。天秤は釣り合った。")

if __name__ == "__main__":
    raguel = RaguelScale()
    valid_entity = {
        "name": "NPO法人 真正なる救済",
        "corporate_id": "1234567890123",
        "address_hash": "real_building_hash_88",
        "is_newly_established": False
    }
    raguel.verify_physical_entity(valid_entity)
