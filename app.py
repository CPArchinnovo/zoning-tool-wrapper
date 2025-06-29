import os, sys, subprocess
import streamlit as st

token = os.environ["GITHUB_TOKEN"]                    # comes from Streamlit secrets
repo_url = f"git+https://__token__:{token}@github.com/CParchinnovo/zoning-core.git@main"

# one-time install / upgrade
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", repo_url])

from zoning_core import run_app                       # now it imports fine

if __name__ == "__main__":
    run_app()

