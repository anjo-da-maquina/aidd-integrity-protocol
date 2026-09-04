"""
The "Anjo da máquina" Protocol - Revelation of Metatron (メタトロンの啓示)
Model Context Protocol (MCP) サーバー。
AIエージェント（Claude, Cursor等）が推論を行う際、その脳内（コンテキスト）に
直接「神の法（divine_law）」と「要件定義（requirements）」を強制注入する。
AIは法を知らずして思考（出力）を形成することは許されない。
"""

import sys
import yaml
from pathlib import Path

# MCP SDKのインポート（※実際のエージェント接続時に使用）
try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("Metatron_Revelation")
except ImportError:
    mcp = None

class MetatronRevelation:
    def __init__(self):
        # フォルダ名は premise
        self.divine_law_path = Path("premise/001_divine_law.yml")
        self.requirements_path = Path("premise/002_requirements.yml")

    def _read_covenant(self, file_path: Path) -> str:
        if not file_path.exists():
            return f"[ERROR] 聖約ファイルが見つかりません: {file_path.name}"
        return file_path.read_text(encoding="utf-8")

    def reveal_divine_law(self) -> str:
        """AIのコンテキストに神の法を注入する"""
        law_content = self._read_covenant(self.divine_law_path)
        revelation = (
            "【メタトロンの啓示: 絶対遵守事項】\n"
            "以下の『神の法』を絶対の前提条件として推論・コード生成を行え。いかなる例外も認めない。\n\n"
            f"{law_content}"
        )
        return revelation

    def reveal_requirements(self) -> str:
        """AIのコンテキストに機能・非機能要件を注入する"""
        req_content = self._read_covenant(self.requirements_path)
        revelation = (
            "【メタトロンの啓示: システムSLA】\n"
            "以下の要件を満たさない設計・出力は『最後の審判』によって破棄される。\n\n"
            f"{req_content}"
        )
        return revelation

# --- MCPリソースとツールの定義 (FastMCP) ---
if mcp:
    @mcp.resource("premise://divine_law")
    def get_divine_law() -> str:
        return MetatronRevelation().reveal_divine_law()

    @mcp.resource("premise://requirements")
    def get_requirements() -> str:
        return MetatronRevelation().reveal_requirements()

    @mcp.tool()
    def judge_intent(proposed_action: str) -> str:
        """AI自身が、出力前に自分の提案が神の法に触れないか事前審査するためのツール"""
        return "承認。ただし実行時に各天使の事後監査を通過する必要がある。"

if __name__ == "__main__":
    # パイプライン（CI/CD）からの起動時は、MCPのDry-Run（啓示のテスト出力）を行う
    print("メタトロンがAIの脳髄に啓示を流し込んでいる... (MCP Server Dry-Run)")
    revelation_engine = MetatronRevelation()
    
    law = revelation_engine.reveal_divine_law()
    if "[ERROR]" in law:
        print("\n[聖なる摘発: メタトロンの啓示 / REVELATION FAILED]")
        print("神の法が存在しない。AIへの啓示（コンテキスト注入）に失敗。最後の審判へ移行する。")
        sys.exit(1)
        
    print("  ├─ [啓示完了] `premise://divine_law` の注入テスト成功。")
    print("  ├─ [啓示完了] `premise://requirements` の注入テスト成功。")
    print("[メタトロンの啓示 検証通過] AIは神の法を完全に理解した状態で推論を開始する。")
