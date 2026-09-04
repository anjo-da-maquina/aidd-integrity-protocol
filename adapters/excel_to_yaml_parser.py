import pandas as pd
import yaml
from pathlib import Path
import sys

def generate_requirements(excel_path: str, output_yaml_path: str):
    output_path = Path(output_yaml_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    requirements = {
        "functional_requirements": {
            "allowed_error_rate_percent": 0,
            "expected_final_state": "SUCCESS",
            "mandatory_scenarios": ["Login_Success", "Data_Export"]
        },
        "non_functional_requirements": {
            "concurrent_users": 100,
            "max_response_time_ms": 500,
            "cpu_utilization_limit_percent": 80
        }
    }

    try:
        df = pd.read_excel(excel_path, sheet_name="TestScenarios")
        scenarios = df[df['Priority'] == 'High']['ScenarioName'].tolist()
        requirements["functional_requirements"]["mandatory_scenarios"] = scenarios
        print(f"[Adapter] {excel_path} から要件を抽出しました。")
    except FileNotFoundError:
        print(f"[Adapter] 警告: {excel_path} が見つからないため、デフォルトの要件定義を使用します。")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(requirements, f, allow_unicode=True)

if __name__ == "__main__":
    generate_requirements("docs/system_spec.xlsx", "premise/002_requirements.yml")
