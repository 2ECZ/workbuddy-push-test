"""Print the local Git state of this repo.

Run it after cloning from GitHub to confirm the pushed code arrived intact.
"""

from __future__ import annotations

import subprocess
import sys


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() or "(no output)"


def main() -> int:
    print("GitHub push test: OK")
    print("-" * 40)
    print(f"python     : {sys.version.split()[0]}")
    print(f"branch     : {git('branch', '--show-current')}")
    print(f"remote     : {git('remote', 'get-url', 'origin')}")
    print(f"last commit: {git('log', '-1', '--pretty=format:%h %s')}")
    print(f"tracked    : {len(git('ls-files').splitlines())} files")
    print("-" * 40)
    print("If you can read this from GitHub, the push worked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
