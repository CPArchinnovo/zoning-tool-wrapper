import os, sys, subprocess
import streamlit as st

# 1️⃣ one-time install of the private core
token = os.environ["GITHUB_TOKEN"]          # injected by Streamlit secrets
repo_url = (
    f"git+https://{token}:x-oauth-basic@github.com/CParchinnovo/zoning-core.git@main"
)
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", repo_url])

# 2️⃣ now import and launch the real app
from zoning_core import run_app

if __name__ == "__main__":
    run_app()
