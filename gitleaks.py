import subprocess

def run_gitleaks():
    subprocess.run([
        "gitleaks", "detect",
        "--source=.",  # current dir
        "--no-git",
        "--report-path=reports/gitleaks_report.json",
        "--verbose"
    ])
