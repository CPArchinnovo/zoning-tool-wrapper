import os, sys, subprocess, tempfile, site
import streamlit as st   # keep Streamlit imported first for safety

# 1️⃣  PAT injected from Streamlit → Secrets
token = os.environ["GITHUB_TOKEN"]          # MUST exist in Cloud

# 2️⃣  writable temp dir + pip install *into* that dir
tmp_dir = tempfile.mkdtemp()                # e.g. /tmp/tmpabc123
repo_url = (
    f"git+https://__token__:{token}"
    f"@github.com/CParchinnovo/zoning-core.git@main"
)

subprocess.check_call(
    [
        sys.executable,
        "-m", "pip", "install",
        "--no-cache-dir",
        "--target", tmp_dir,               # <-- critical: write to /tmp
        repo_url,
    ]
)

# 3️⃣  make Python import from /tmp/tmpabc123
site.addsitedir(tmp_dir)

# 4️⃣  import and launch your real Streamlit app
from zoning_core import run_app

if __name__ == "__main__":
    run_app()
