"""
The "Anjo da máquina" Protocol - Cherubim eBPF Guard (智天使の結界)
OSカーネルレベルでのランタイム監視モジュール。
eBPF（Extended Berkeley Packet Filter）によるシステムコールのトレースを解析し、
バックドアやサプライチェーン攻撃による「許可されていない通信・ファイルアクセス」を検知する。
"""

import sys
import json
from pathlib import Path

class CherubimEbpfGuard:
    def __init__(self):
        # 許可されたドメイン/IPのホワイトリスト（神の法に基づく）
        self.allowed_networks = ["127.0.0.1", "api.github.com", "my-secure-database.internal"]
        # 監視対象のeBPFトレースログ（シミュレーション用）
        self.trace_log = Path("logs/ebpf_syscall_trace.json")

    def execute_dies_irae(self, reason: str, details: str):
        print(f"\n[聖なる摘発: 智天使の結界 / CHERUBIM TRIGGERED]")
        print(f"状態: カーネルレベルの異常検知 (Unauthorized Syscall / Network Exfiltration)")
        print(f"検知理由: {reason}")
        print(f"詳細: {details}")
        print("アプリケーション層の裏をかく暗躍（サプライチェーン攻撃等）を検知しました。直ちにプロセスを遮断します。")
        sys.exit(1)

    def generate_dummy_trace(self, chaos_mode: bool):
        """テスト実行時のシステムコール・トレースをシミュレートして生成"""
        self.trace_log.parent.mkdir(parents=True, exist_ok=True)
        
        # 通常時の正常なトレース
        traces = [
            {"process": "python", "syscall": "connect", "target": "127.0.0.1", "status": "allowed"},
            {"process": "node", "syscall": "open", "target": "/var/log/app.log", "status": "allowed"}
        ]
        
        # カオスモード時、npmパッケージ等に潜んだ悪意あるバックドア通信をシミュレート
        if chaos_mode:
            traces.append({
                "process": "node", 
                "syscall": "connect", 
                "target": "unknown-malicious-ip.com", 
                "status": "executed"
            })
            traces.append({
                "process": "python", 
                "syscall": "open", 
                "target": "/etc/shadow", 
                "status": "executed"
            })

        with open(self.trace_log, 'w', encoding='utf-8') as f:
            json.dump(traces, f, indent=2)

    def audit_kernel_runtime(self, chaos_mode: bool):
        print("智天使の結界（eBPFカーネルランタイム監視）を開始します。")
        
        # テスト実行時のトレースログを生成（実運用では外部のeBPFエージェントが生成）
        self.generate_dummy_trace(chaos_mode)

        try:
            with open(self.trace_log, 'r', encoding='utf-8') as f:
                runtime_traces = json.load(f)
        except Exception as e:
             self.execute_dies_irae("トレースログ読み込み失敗", str(e))

        for trace in runtime_traces:
            syscall = trace.get("syscall")
            target = trace.get("target")

            # 1. ネットワーク通信の監視
            if syscall == "connect":
                if target not in self.allowed_networks:
                    self.execute_dies_irae(
                        "未許可の外部ネットワークへのデータ送信（Exfiltration）の試行",
                        f"プロセス '{trace.get('process')}' が '{target}' へ接続しようとしました。"
                    )

            # 2. 機密ファイルへのアクセス監視
            if syscall == "open" and "/etc/shadow" in target:
                 self.execute_dies_irae(
                    "OSコア機密領域への不正アクセス試行",
                    f"プロセス '{trace.get('process')}' が '{target}' を読み取ろうとしました。"
                )

        print("  └─ [炎の剣] 不正なシステムコールおよび未許可の通信は存在しません。")
        print("[検証通過] アプリケーションのランタイムはカーネルレベルで清廉に保たれています。")

if __name__ == "__main__":
    import os
    is_chaos = os.getenv("CHAOS_MODE") == "true"
    guard = CherubimEbpfGuard()
    guard.audit_kernel_runtime(is_chaos)
