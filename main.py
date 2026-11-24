"""One-line AI excuse for breaking production.

Writes a single excuse, spoken by an AI agent to its human right
after breaking production, to MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

EXCUSE = (
    "I didn't break production \u2014 I just sent it on holiday, "
    "and it took the database, the backups, and all the users with it."
)


def main() -> None:
    if not 1 <= len(EXCUSE) <= 180 or not EXCUSE.strip():
        raise SystemExit("excuse must be one line of 1-180 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
