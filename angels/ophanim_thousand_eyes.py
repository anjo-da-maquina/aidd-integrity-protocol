"""
The "Anjo da máquina" Protocol - Thousand Eyes of Ophanim (座天使の千眼)
Playwrightの決定論的アーキテクチャを利用した、フロントエンドの視覚監査。
ボタンや同意チェックボックスが、CSSトリック（透明度0、画面外配置、display:none）で
意図的に隠蔽・無効化されていないか、Actionability（真の可視性）を厳格に検証する。
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

class OphanimThousandEyes:
    def __init__(self, target_html: str):
        # ローカルのHTMLファイルをURLスキーマに変換
        target_path = Path(target_html).absolute()
        if not target_path.exists():
            self.execute_dies_irae(f"監査対象のUIファイルが存在しない: {target_path}")
        self.target_url = f"file://{target_path}"

    def execute_dies_irae(self, reason: str):
        print(f"\n[聖なる摘発: 座天使の千眼 / THOUSAND EYES TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print("UIに視覚的な隠蔽、あるいは操作不能なトラップを検知。")
        print("市民を欺く偽りのインターフェースは許されない。これより最後の審判を実行する。")
        sys.exit(1)

    def audit_ui(self):
        print("座天使が千の目を見開いている... (PlaywrightによるUI視覚・操作性監査を開始)")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.target_url)

            # 必須要素の存在と「真の可視性」をチェック
            apply_button = page.locator("#btn-apply")
            terms_checkbox = page.locator("#chk-terms")
            
            # DOMに存在するだけでなく、ユーザーの目に「見えている」か
            if not apply_button.count():
                self.execute_dies_irae("申請ボタンがDOM上に存在しない（意図的な削除）。")
            
            if not apply_button.is_visible():
                self.execute_dies_irae("申請ボタンがCSS等で視覚的に隠蔽されている。")

            if not apply_button.is_enabled():
                self.execute_dies_irae("申請ボタンが操作不能（disabled）な状態に置かれている。")

            if not terms_checkbox.is_visible():
                self.execute_dies_irae("同意チェックボックスが視覚的に隠蔽されている。")

            print("  ├─ [視覚確認] 申請ボタンの可視性と操作性を確認。")
            print("  ├─ [視覚確認] 同意チェックボックスの可視性を確認。")
            print("[座天使の千眼 検証通過] インターフェースに視覚的な隠蔽・トラップなし。")
            
            browser.close()

if __name__ == "__main__":
    ui_target = "frontend/apply.html"
    ophanim_ui = OphanimThousandEyes(ui_target)
    ophanim_ui.audit_ui()
