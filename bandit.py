import subprocess

def run_bandit():
    subprocess.run([
        "bandit", "-r", ".", "-f", "json", "-o", "reports/bandit_report.json"
    ])
