"""
Phoenix device-side scaffold.

This is a placeholder module tree so the repo has an obvious firmware/code path.
The real architecture is described in SOFTWARE.md and HARDWARE.md.
"""

import time


def main():
    """Device entry point sketch."""
    print("Phoenix scaffold starting")
    state = "idle"
    while True:
        time.sleep(1)
        if state == "idle":
            state = "listening"


if __name__ == "__main__":
    main()
