"""CLI entry point for PromptPilot."""

import subprocess
import sys


def main() -> None:
    """Run the Streamlit app."""
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "src/promptpilot/app.py"],
        check=True,
    )


if __name__ == "__main__":
    main()
