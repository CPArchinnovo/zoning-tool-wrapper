import os, sys, subprocess, tempfile, site
import streamlit as st

# ── 1. get your GitHub token that Streamlit injects ────────────────────────────
token = os.environ["GITHUB_TOKEN"]      # ⚠️ make sure the secret exists in Cloud

# ── 2. build a writable temp dir and pip-install the private repo there ───────
tmp_dir = tempfile.mkdtemp()            # e.g. /tmp/tmpabcdef
repo_url = (
    f"git+https://__token__:{token}"
    f"@github.com/CParchinnovo/zoning-core.git@main"
)

subprocess.check_call(
    [
        sys.executable,
        "-m", "pip", "install",
        "--upgrade",
        "--no-cache-dir",
        "--target", tmp_dir,   # <-- install INTO the temp folder
        repo_url,
    ]
)

# ── 3. add that temp dir to Python’s import path ──────────────────────────────
site.addsitedir(tmp_dir)

# ── 4. Import and run your REAL app ───────────────────────────────────────────
from zoning_core import run_app         # now import succeeds

if __name__ == "__main__":
    run_app()
