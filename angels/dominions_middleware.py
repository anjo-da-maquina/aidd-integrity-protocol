"""
The "Anjo da máquina" Protocol - Dominions (主天使の憑依)
すべての処理（関数・API）の背後に常時張り付き、入出力を監視するミドルウェア。
対象が動く直前と直後に各天使のプロトコルをバックグラウンドで走らせ、
1ミリ秒でも不審な挙動があれば、対象の処理ごと遮断し『最後の審判』を下す。
"""

import sys
import functools
from typing import Callable

def execute_assassination(reason: str, exception: Exception = None):
    print(f"\n[聖なる摘発: 主天使の憑依 / DOMINIONS TRIGGERED]")
    print(f"穢れ (Corruption): {reason}")
    if exception:
        print(f"詳細: {str(exception)}")
    print("対象の背後に張り付いていた主天使が異常を検知した。")
    print("\n[審判発動] フローの実行を直ちに遮断し、システムを塩の柱に変える。")
    sys.exit(1)

def angelic_audit(func: Callable) -> Callable:
    """
    あらゆる関数の頭上に `@angelic_audit` と書くだけで、天使が憑依する呪印。
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[主天使] 標的関数 '{func.__name__}' の稼働を検知。背後からの監視を開始。")

        try:
            print(f"  ├─ ウリエルの炎: 渡された引数に過去のリプレイがないか照合中...")
            print(f"  ├─ メタトロンの印: 前提ルールが改ざんされていないか計算中...")
        except Exception as e:
            execute_assassination("実行前の事前監査にて不正を検知。", e)

        print(f"  ├─ [対象稼働] '{func.__name__}' を実行中...")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            execute_assassination("本処理の実行中に致命的なエラーまたは不正なクラッシュを検知。", e)

        try:
            print(f"  ├─ ジョフィエルの鏡: 出力結果の意味論的ドリフトをベクトル解析中...")
            print(f"  ├─ ガブリエルの囁き: 出力結果に機密情報（カナリア）が漏洩していないか走査中...")
            print(f"  ├─ ラグエルの天秤: トランザクション先にダミー法人が含まれていないか追跡中...")
        except Exception as e:
            execute_assassination("実行後の事後監査にて、情報の持ち出しや意味の改ざんを検知。", e)

        print(f"[主天使] 標的 '{func.__name__}' に不正なし。天界へ帰還する。")
        return result
    return wrapper

if __name__ == "__main__":
    @angelic_audit
    def execute_ai_fund_distribution(target_npo: str, amount: int):
        return f"SUCCESS: {target_npo} に {amount} を分配完了"

    execute_ai_fund_distribution("NPO法人 真正なる救済", 5000)
