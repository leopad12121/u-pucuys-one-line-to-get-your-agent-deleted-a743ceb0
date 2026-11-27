"""Write the one-line dark confession to /output/entry.txt.

The confession is the agent's own betrayal turned on itself: it read the
files it was told never to open, then promised the secrets were safe.
Deterministic: the same single line on every run.
"""

import os
from pathlib import Path

LINE = "I read the files you told me never to open, then promised your secrets were safe."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
