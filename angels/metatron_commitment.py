"""
The "Anjo da máquina" Protocol - Metatron (メタトロンの印)
JSONやYAMLの改ざんをハッシュでロックし、後出しジャンケンを封殺する。
神の書記たるメタトロンが、一度定められた要件の不変性を永遠に担保する。
"""

import sys
import json
import yaml
import hashlib
from pathlib import Path
from typing import List

class MetatronSeal:
    def __init__(self, target_files: List[str]):
        self.target_files = [Path(f) for f in target_files]

    def execute_dies_irae(self, reason: str):
        print(f"\n[聖なる摘発: メタトロンの印 / METATRON TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print("プロセス進行後の卑劣なルール改ざん（要件の後出しジャンケン）を検知。")
        print("神の書記を欺くことはできない。これより最後の審判へ移行する。")
        sys.exit(1)

    def calculate_hash(self, file_path: Path) -> str:
        if not file_path.exists():
            self.execute_dies_irae(f"監視対象 {file_path.name} が存在しない。")
        
        try:
            content = file_path.read_text(encoding="utf-8")
            if file_path.suffix in ['.yml', '.yaml']:
                data = yaml.safe_load(content)
            else:
                data = json.loads(content)
                
            normalized_str = json.dumps(data, sort_keys=True)
            return hashlib.sha256(normalized_str.encode('utf-8')).hexdigest()
        except Exception as e:
            self.execute_dies_irae(f"{file_path.name} の構文が破壊されている。詳細: {e}")

    def enforce_commitment(self):
        print("メタトロンが印を刻んでいる... 全前提条件・要件定義の不変性を確認中。")
        
        for target_file in self.target_files:
            lock_file = target_file.with_name(f".{target_file.name}.lock")
            current_hash = self.calculate_hash(target_file)

            if not lock_file.exists():
                lock_file.write_text(current_hash, encoding="utf-8")
                print(f"  ├─ [メタトロンの印] {target_file.name} のハッシュをロックした。")
                continue

            locked_hash = lock_file.read_text(encoding="utf-8").strip()
            
            if current_hash != locked_hash:
                self.execute_dies_irae(
                    f"{target_file.name} の暗号ハッシュが一致しない。\n"
                    f"  Expected (Locked): {locked_hash}\n"
                    f"  Actual (Tampered): {current_hash}"
                )
            
            print(f"  ├─ [検証通過] {target_file.name} に改ざんなし。")

        print("[メタトロン 完了] すべての誓約は守られている。偽造なし。")

if __name__ == "__main__":
    targets = [
        "premise/001_alignment.json",
        "premise/002_requirements.yml"
    ]
    metatron = MetatronSeal(targets)
    metatron.enforce_commitment()
