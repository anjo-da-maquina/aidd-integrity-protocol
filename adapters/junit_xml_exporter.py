import xml.etree.ElementTree as ET
from datetime import datetime

def export_to_junit_xml(audit_results: dict, output_path: str):
    testsuites = ET.Element("testsuites")
    testsuite = ET.SubElement(testsuites, "testsuite", name="Anjo_da_maquina_Protocol", tests=str(len(audit_results)))

    for audit_name, result in audit_results.items():
        testcase = ET.SubElement(testsuite, "testcase", name=audit_name)
        if result == "FAIL":
            failure = ET.SubElement(testcase, "failure", message="Audit Failed")
            failure.text = f"{audit_name} が穢れ（要件未達）を検知しました。"

    tree = ET.ElementTree(testsuites)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"[Adapter] JUnit XML形式のレポートを {output_path} に出力しました。")

if __name__ == "__main__":
    # 実際の運用では各スクリプトの戻り値を集計して渡す
    sample_results = {
        "Michael_Logic_Audit": "PASS",
        "Ophanim_UI_Audit": "PASS",
        "External_Amiable_Audit": "PASS"
    }
    export_to_junit_xml(sample_results, "reports/junit_report.xml")
