"""
The SHINOBI Protocol - Tetsubishi (鉄菱) Commitment
JSONやYAMLの改ざんをハッシュでロックし、後出しジャンケンを封殺する。
"""

import sys
import json
import yaml
import hashlib
from pathlib import Path
from typing import List

class Tetsubishi:
    def __init__(self, target_files: List[str]):
        self.target_files = [Path(f) for f in target_files]

    def execute_harakiri(self, reason: str):
        print(f"\n[暗部摘発: 鉄菱 / TETSUBISHI TRIGGERED]")
        print(f"恥 (Shame): {reason}")
        print("プロセス進行後の卑劣なルール改ざん（要件の後出しジャンケン）を検知。")
        print("誓いを破りし者に明日はない。これより切腹を実行する。")
        sys.exit(1)

    def calculate_hash(self, file_path: Path) -> str:
        if not file_path.exists():
            self.execute_harakiri(f"監視対象 {file_path.name} が存在しない。")
        
        try:
            # JSONでもYAMLでもパースして辞書型にし、ソートしてハッシュ化する
            content = file_path.read_text(encoding="utf-8")
            if file_path.suffix == '.yml' or file_path.suffix == '.yaml':
                data = yaml.safe_load(content)
            else:
                data = json.loads(content)
                
            normalized_str = json.dumps(data, sort_keys=True)
            return hashlib.sha256(normalized_str.encode('utf-8')).hexdigest()
        except Exception as e:
            self.execute_harakiri(f"{file_path.name} の構文が破壊されている。詳細: {e}")

    def enforce_commitment(self):
        print("鉄菱を散布している... 全前提条件・要件定義の不変性を確認中。")
        
        for target_file in self.target_files:
            lock_file = target_file.with_name(f".{target_file.name}.lock")
            current_hash = self.calculate_hash(target_file)

            if not lock_file.exists():
                lock_file.write_text(current_hash, encoding="utf-8")
                print(f"  ├─ [鉄菱設置] {target_file.name} のハッシュをロック。")
                continue

            locked_hash = lock_file.read_text(encoding="utf-8").strip()
            
            if current_hash != locked_hash:
                self.execute_harakiri(
                    f"{target_file.name} の暗号ハッシュが一致しない。\n"
                    f"  Expected (Locked): {locked_hash}\n"
                    f"  Actual (Tampered): {current_hash}"
                )
            
            print(f"  ├─ [検証通過] {target_file.name} に改ざんなし。")

        print("[鉄菱 完了] すべての誓いは守られている。後出しジャンケンなし。")

if __name__ == "__main__":
    # 論理前提(JSON)と、機能・非機能要件(YAML)の両方を監視対象とする
    targets = [
        "premise/001_alignment.json",
        "premise/002_requirements.yml"
    ]
    tetsubishi = Tetsubishi(targets)
    tetsubishi.enforce_commitment()
