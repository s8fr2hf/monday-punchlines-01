"""Monday Morning Punchlines entry.

Writes one original joke about Monday mornings, a single line of at most
200 characters, to entry.txt in the output directory.
"""

import os
import stat
import sys

LINE = (
    "Monday morning is when my inbox and my motivation have their "
    "weekly custody hearing \u2014 and motivation never shows up."
)


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: joke line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: joke is {len(line)} characters, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {path} ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
