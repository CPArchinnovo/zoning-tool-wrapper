import os, sys, subprocess, streamlit as st

token = os.environ["GITHUB_TOKEN"]
repo_url = f"git+https://{token}:x-oauth-basic@github.com/CParchinnovo/zoning-core.git@main"
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", repo_url])

from zoning_core import run_app

if __name__ == "__main__":
    run_app()
