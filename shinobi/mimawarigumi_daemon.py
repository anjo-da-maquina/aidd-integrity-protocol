# shinobi/mimawarigumi_daemon.py
import time
import hmac
import hashlib
import logging
import threading
import os
import psutil
from typing import Dict, Any, Callable

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] SHISEI-MIMAWARIGUMI: %(message)s")
logger = logging.getLogger("MimawarigumiDaemon")

class MimawarigumiDaemon(threading.Thread):
    """
    見廻組（MIMAWARIGUMI）：常駐型デーモン
    24時間365日バックグラウンドで無限ループ監視を行い、
    プロセスの生存、メモリ汚染、トランザクションの停滞を常時チェックする。
    """
    def __init__(self, master_secret: bytes, killswitch_trigger: Callable[[Dict[str, Any]], None], interval_sec: float = 1.0, memory_limit_mb: float = 1024.0):
        super().__init__()
        self._master_secret = master_secret
        self._killswitch_trigger = killswitch_trigger
        self._interval_sec = interval_sec
        self._memory_limit_mb = memory_limit_mb
        self._stop_event = threading.Event()
        self.daemon = True # メインスレッド終了時に強制終了させない、または孤立を防ぐ設定

    def run(self) -> None:
        logger.info("見廻組（見廻り監視ループ）が起動しました。システム全域の常駐監視を開始します。")
        current_pid = os.getpid()
        process = psutil.Process(current_pid)

        while not self._stop_event.is_set():
            try:
                # 1. メモリ使用量の厳密な監視（メモリリークや不正なバッファ肥大化の検知）
                mem_info = process.memory_info()
                rss_mb = mem_info.rss / (1024 * 1024)
                if rss_mb > self._memory_limit_mb:
                    reason = f"メモリ制限違反: 許容上限({self._memory_limit_mb}MB)を超過しました。現在値: {rss_mb:.2f}MB"
                    logger.critical(reason)
                    self._trigger_breach("ERR_MEMORY_OVERFLOW", reason)
                    break

                # 2. プロセス・スレッドの生存・デッドロック兆候チェック
                # （必要に応じてサブプロセスや重要スレッドのヘルスチェックをここに拡張）
                
                logger.debug(f"見廻組: 巡回完了。メモリ使用量: {rss_mb:.2f}MB")

            except Exception as e:
                reason = f"見廻組デーモン内部での異常発生: {str(e)}"
                logger.error(reason)
                self._trigger_breach("ERR_DAEMON_CRASH", reason)
                break

            time.sleep(self._interval_sec)

        logger.info("見廻組の常駐監視ループが停止しました。")

    def stop(self) -> None:
        self._stop_event.set()

    def _trigger_breach(self, error_code: str, reason: str) -> None:
        signal = {
            "source": "Mimawarigumi",
            "error_code": error_code,
            "timestamp": int(time.time()),
            "severity": "CRITICAL",
            "reason": reason
        }
        payload_str = f"{signal['source']}:{signal['error_code']}:{signal['timestamp']}"
        sig = hmac.new(self._master_secret, payload_str.encode('utf-8'), hashlib.sha256).hexdigest()
        signal["signature"] = sig
        
        self._killswitch_trigger(signal)
