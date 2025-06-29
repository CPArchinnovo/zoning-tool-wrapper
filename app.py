import os, sys, subprocess, tempfile, site, streamlit as st

# 1️⃣ retrieve the PAT that Streamlit injects as an env-var
token = os.environ["GITHUB_TOKEN"]              # MUST exist in Settings ▸ Secrets

# 2️⃣ pip-install the private repo into a writable temp directory
tmp_dir = tempfile.mkdtemp()                    # e.g. /tmp/tmpabcd1234
repo_url = (
    f"git+https://__token__:{token}"
    f"@github.com/CParchinnovo/zoning-core.git@main"
)

subprocess.check_call(
    [
        sys.executable, "-m", "pip", "install",
        "--no-cache-dir", "--target", tmp_dir, repo_url,
    ]
)

# 3️⃣ tell Python to import from that folder
site.addsitedir(tmp_dir)

# 4️⃣ launch the real Streamlit app
from zoning_core import run_app

if __name__ == "__main__":
    run_app()
