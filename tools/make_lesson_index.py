from pathlib import Path
import re

base = Path("01-lessons")
out = base / "README.md"

def natural_key(s: str):
    # sorts like L1, L2, ..., L10 instead of L1, L10, L2
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\\d+)", s)]

items = sorted([p for p in base.iterdir() if p.is_dir()], key=lambda p: natural_key(p.name))

lines = []
lines.append("# Lesson Index (24 sessions)\\n\\n")
lines.append("This folder contains the full lesson sequence and artifacts for each session.\\n\\n")

for p in items:
    lines.append(f"- [\{p.name\}](\{p.name\}/)\\n")

out.write_text("".join(lines), encoding="utf-8")
print(f"Wrote: \{out\}")}