"""Funniest Time Machine Warning Label entry.

Writes a single warning label (<=120 chars) to /output/entry.txt.
The output directory honours MAKEFUN_OUTPUT_DIR for local testing;
the grader runs with /output.
"""

import os

LABEL = (
    "WARNING: Never shake hands with your past self. "
    "He knows your passwords, hates your haircut, "
    "and is dating your ex."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
