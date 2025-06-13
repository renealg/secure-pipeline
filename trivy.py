import subprocess

def run_trivy():
    subprocess.run([
        "trivy", "config", "--format", "json",
        "--output", "reports/trivy_report.json", "."
    ])
