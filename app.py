import os, sys, subprocess, tempfile, site, streamlit as st   # keep Streamlit import

# 1️⃣ PAT injected from Streamlit ▶ Secrets
token = os.environ["GITHUB_TOKEN"]           # MUST exist in Cloud

# 2️⃣ install private package into a writable /tmp folder
tmp_dir = tempfile.mkdtemp()                 # e.g. /tmp/tmpabcd
repo_url = (
    f"git+https://__token__:{token}"
    f"@github.com/CParchinnovo/zoning-core.git@main"
)
subprocess.check_call(
    [
        sys.executable, "-m", "pip", "install",
        "--no-cache-dir", "--target", tmp_dir,   # ✔ write to /tmp
        repo_url,
    ]
)

# 3️⃣ make Python import from that folder
site.addsitedir(tmp_dir)

# 4️⃣ launch your real Streamlit app
from zoning_core import run_app

if __name__ == "__main__":
    run_app()
