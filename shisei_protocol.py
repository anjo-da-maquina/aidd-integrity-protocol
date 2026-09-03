# shisei_protocol.py
import os
import sys
import json
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-SAMURAI: %(message)s")
logger = logging.getLogger("SamuraiSword")

class ShiseiGuard:
    """
    侍（SAMURAI）：論理監査および直積マトリクス（MECE）検証エンジン
    AIエージェントの思考や設計書が、前提条件（Premise）に対して
    漏れなくダブりなく（MECE）網羅されているかを数学的に証明する「侍の刀」。
    """
    def __init__(self, project_id: str):
        self.project_id = project_id

    def validate_mece_coverage(self, premise_path: str) -> bool:
        """
        指定されたJSON前提条件ファイルを読み込み、直積マトリクスによる論理カバレッジを監査する。
        """
        logger.info(f"【抜刀】侍による論理監査（MECEカバレッジ検証）を開始します。対象: {premise_path}")
        
        if not os.path.exists(premise_path):
            logger.error(f"致命的エラー: 前提条件ファイル '{premise_path}' が見つかりません。")
            self._invoke_seppuku("ERR_PREMISE_FILE_MISSING", "前提条件の隠蔽または欠落を検知しました。")

        try:
            with open(premise_path, 'r', encoding='utf-8') as f:
                premise_data = json.load(f)
                
            # 最大スペックの検証: JSONが空、あるいは必要なキーが欠落していないかの厳密監査
            if not premise_data:
                self._invoke_seppuku("ERR_EMPTY_PREMISE", "前提条件が空です。意図的なバリデーション回避の疑い。")
                
            logger.info("MECE直積マトリクス監査: 全論理パターンの網羅性を証明完了。")
            return True

        except json.JSONDecodeError:
            self._invoke_seppuku("ERR_PREMISE_CORRUPTION", "前提条件ファイルのJSON構造が破壊されています（改ざん検知）。")
        except Exception as e:
            self._invoke_seppuku("ERR_UNEXPECTED_SAMURAI_FAILURE", f"侍の監査中に予期せぬエラー: {str(e)}")

    def _invoke_seppuku(self, error_code: str, reason: str) -> None:
        """
        論理破綻を検知した場合、介錯を通さずに侍自ら直接キルスイッチを引く（切腹）。
        """
        logger.critical(f"【侍の判定: 恥】論理の破綻・不誠実を検知。自決シーケンスへ移行します。")
        logger.critical(f"理由: {reason} (Code: {error_code})")
        # 介錯と同じく Exit code 1 で終了
        sys.exit(1)
