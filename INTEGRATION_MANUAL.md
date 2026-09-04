# 外部ツール連携・統合マニュアル
**— "Anjo da máquina" Protocol Integration Guide —**

本プロトコルは、独立したPythonスクリプト群と標準的な終了コード（Exit Code `0` または `1`）を基準に稼働しています。この仕様を利用し、境界部分に「アダプター（変換層）」を設けることで、既存のテスト資産や外部QAツールとのシームレスな統合が可能です。

---

## 1. 入力層の連携：設計書からの自動要件抽出
構造化されたExcel等のソフトウェア仕様書から、本プロトコルの監視基準である `premise/002_requirements.yml` を動的に生成するパーサーを実装します。

### 実装方針（Excel → YAML変換）
既存の仕様書管理フローを崩さず、CI/CDパイプラインの初期ステップでPythonスクリプトを用いてテスト要件を抽出します。

**実装例: `adapters/excel_to_yaml_parser.py`**
```python
import pandas as pd
import yaml
from pathlib import Path

def generate_requirements_from_excel(excel_path: str, output_yaml_path: str):
    # Excelの仕様書から必須テストシナリオを読み込む
    df = pd.read_excel(excel_path, sheet_name="TestScenarios")
    mandatory_scenarios = df[df['Priority'] == 'High']['ScenarioName'].tolist()

    # プロトコルが解釈可能なYAML形式にマッピング
    requirements = {
        "functional_requirements": {
            "allowed_error_rate_percent": 0,
            "expected_final_state": "SUCCESS",
            "mandatory_scenarios": mandatory_scenarios
        },
        "non_functional_requirements": {
            "concurrent_users": 100,
            "max_response_time_ms": 500,
            "cpu_utilization_limit_percent": 80
        }
    }

    with open(output_yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(requirements, f, allow_unicode=True)
    print(f"[Adapter] {excel_path} から要件を抽出し、{output_yaml_path} を生成しました。")

if __name__ == "__main__":
    generate_requirements_from_excel("docs/system_spec.xlsx", "premise/002_requirements.yml")
