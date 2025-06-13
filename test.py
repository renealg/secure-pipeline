import subprocess

def run_dangerous():
    subprocess.call("ls", shell=True)
