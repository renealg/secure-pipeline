from gitleaks import run_gitleaks
from bandit import run_bandit
from trivy import run_trivy
import os

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

print("🔍 Running Gitleaks...")
run_gitleaks()

print("🐍 Running Bandit...")
run_bandit()

print("🐳 Running Trivy...")
run_trivy()

print("✅ All scans completed.")