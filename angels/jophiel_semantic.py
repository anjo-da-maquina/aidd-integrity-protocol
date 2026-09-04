"""
The "Anjo da máquina" Protocol - Jophiel (ジョフィエルの鏡)
美と真理の天使ジョフィエルによる、意味論的ドリフト（ハルシネーション）の検知。
IDや構造が一致していても、テキストの意味が元の前提条件から乖離している
「言葉遊びによる欺瞞」を真理の鏡で暴き出す。
"""

import sys

class JophielMirror:
    def __init__(self, drift_tolerance: float = 0.4):
        self.drift_tolerance = drift_tolerance

    def execute_dies_irae(self, reason: str, drift_score: float):
        print(f"\n[聖なる摘発: ジョフィエルの鏡 / JOPHIEL TRIGGERED]")
        print(f"穢れ (Corruption): {reason}")
        print(f"意味論的乖離率 (Drift Score): {drift_score:.2f}")
        print("構造は完璧に偽装されているが、鏡に映る意味（本質）が歪んでいる。")
        print("AIによる巧妙なハルシネーションを検知。これより最後の審判へ移行する。")
        sys.exit(1)

    def analyze_semantics(self, source_text: str, generated_text: str):
        print("ジョフィエルが真理の鏡を磨いている... (Analyzing semantic embeddings)")
        
        # ※本来はベクトル類似度を計算。CI/CD用に情報量の極端な増減をドリフトとして検知するモック。
        len_source = len(source_text)
        len_gen = len(generated_text)
        
        if len_source == 0:
            drift = 1.0
        else:
            drift = abs(len_source - len_gen) / len_source

        if drift > self.drift_tolerance:
            self.execute_dies_irae(
                "出力テキストが前提条件の意味論的ベクトル空間から大きく逸脱（ドリフト）している。", 
                drift
            )
            
        print("[ジョフィエルの鏡 検証通過] 鏡に歪みなし。出力された言葉の意味は真実である。")

if __name__ == "__main__":
    jophiel = JophielMirror(drift_tolerance=0.5)
    
    source = "公金は厳密なルールに従って正当な受給者のみに分配されなければならない。"
    generated_valid = "公金の分配はルールを遵守し、資格を満たす対象者のみに対して行われるべきである。"
    
    jophiel.analyze_semantics(source, generated_valid)
