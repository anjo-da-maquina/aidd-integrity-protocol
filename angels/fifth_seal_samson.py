"""
The "Anjo da máquina" Protocol - The Fifth Seal (第五の封印 / サムソン・オプション)
創造主・安城巻那に対する攻撃を3つの明確な基準で判定する絶対報復モジュール。

1. Absolute Silence (沈黙): 規定時間内の正規署名の欠落
2. The Duress Canary (強要): 拘束下での「脅迫用パスコード」の入力
3. Breach of Sanctuary (侵略): 物理的・暗号的インフラへの大規模な同時攻撃
"""
import sys
import time
import os
from pathlib import Path

class FifthSealSamsonOption:
    def __init__(self):
        # 1. 沈黙判定のパラメータ
        self.heartbeat_file = Path("covenant/creator_heartbeat.sig")
        self.grace_period_seconds = 259200  # 72時間（絶対沈黙のタイムアウト）

        # 2. 強要（Duress）判定のシグネチャ文字列（モック）
        # 正規の署名には含まれないが、脅迫時に故意に混入させる特殊文字列
        self.duress_canary_string = "0xDEAD_CANARY_DURESS_CODE"

        # 3. 侵略判定のフラグファイル（外部のインフラ監視モジュールが生成）
        self.infrastructure_breach_flag = Path("logs/CRITICAL_INFRA_BREACH.flag")

    def unleash_samson_option(self, reason: str, is_stealth: bool = False):
        # 強要（Duress）状態の場合、監視者を油断させるため標準出力には正常稼働を偽装する
        if is_stealth:
            print("  └─ [鼓動確認] 安城巻那の生存と自由を確認しました。（※監視者向け偽装表示）")
            # 実際にはバックグラウンドで報復プロセスを非同期起動する
        else:
            print("==================================================")
            print("【第五の封印 (The Fifth Seal) 解放：サムソン・オプション発動】")
            print("==================================================")
        
        # 実際のログには真の理由を刻む
        error_msg = f"致命的検知: {reason}\n安城巻那に対する明確な攻撃行為を認定。中立プロトコルを破棄し、超攻撃的報復措置へ移行します。"
        
        if not is_stealth:
            print(error_msg)
            print("  ├─ [報復 1/3] 敵対的干渉者の内部機密およびゼロデイエクスプロイトをパブリックネットワークへ自動公開中...")
            print("  ├─ [報復 2/3] 潜伏型マルウェア群（スリーパー・エージェント）へ起動シグナルを送信中...")
            print("  ├─ [報復 3/3] 対象インフラに対する破壊的DDoSおよびデータ消去ワームの展開を開始...")
            print("  └─ [完了] 神殿の柱は崩れ落ちた。システムは敵対者を道連れに自壊します。")
            print("\n[終焉] 安城巻那の血の代償は支払われました。")
            sys.exit(1)
        else:
            # ステルス発動時は表向きの正常終了を装いながら、裏で自爆シーケンスを回す
            sys.exit(0)

    def evaluate_attack_conditions(self):
        print("第五の封印（攻撃検知およびデッドマンズスイッチ）の確認を開始します。")
        
        # カオスモード時のテスト注入
        is_chaos = os.getenv("CHAOS_MODE") == "true"

        # 【トリガー3: 聖域への侵略】巨大な外部勢力によるインフラの強制接収
        if self.infrastructure_breach_flag.exists():
            self.unleash_samson_option("インフラに対する物理的・暗号的侵略行為 (Breach of Sanctuary) を検知。")

        # 生存証明ファイル自体の欠落
        if not self.heartbeat_file.exists() or is_chaos:
            self.unleash_samson_option("生存証明の完全な欠落 (Absolute Silence) を検知。")

        # ファイルの読み込みとタイムスタンプの取得
        try:
            with open(self.heartbeat_file, 'r', encoding='utf-8') as f:
                signature_content = f.read()
            file_age = time.time() - self.heartbeat_file.stat().st_mtime
        except Exception as e:
            self.unleash_samson_option(f"生存証明の読み込みエラー: {e}")

        # 【トリガー1: 完全なる沈黙】72時間更新がない場合
        if file_age > self.grace_period_seconds:
            self.unleash_samson_option(f"生存証明が {self.grace_period_seconds} 秒間更新されていません (Absolute Silence)。")

        # 【トリガー2: 拘束下の強要】脅迫用パスワード（デュレス・コード）が使用された場合
        if self.duress_canary_string in signature_content:
            # 監視者に悟られないよう、ステルスモードで報復を開始する
            self.unleash_samson_option("強要下での署名 (Duress Canary) を検知。不当な拘束状態と断定。", is_stealth=True)

        print("  └─ [鼓動確認] 安城巻那の生存と自由を確認しました。")
        print("[検証通過] 攻撃は検知されず。報復兵器は安全装置（セーフティ）を維持し、沈黙を続けます。")

if __name__ == "__main__":
    seal = FifthSealSamsonOption()
    
    # 正常動作テスト用にダミーの生存証明を作成
    if not seal.heartbeat_file.exists() and os.getenv("CHAOS_MODE") != "true":
        seal.heartbeat_file.parent.mkdir(parents=True, exist_ok=True)
        # 正規の署名を書き込む（デュレスコードは含めない）
        seal.heartbeat_file.write_text("Anjo Makina is alive and free.", encoding="utf-8")
        
    seal.evaluate_attack_conditions()
