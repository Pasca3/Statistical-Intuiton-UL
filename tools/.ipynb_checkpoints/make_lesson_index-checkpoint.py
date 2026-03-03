{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww15100\viewh11660\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from pathlib import Path\
import re\
\
base = Path("01-lessons")\
out = base / "README.md"\
\
def natural_key(s: str):\
    # sorts like L1, L2, ..., L10 instead of L1, L10, L2\
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\\d+)", s)]\
\
items = sorted([p for p in base.iterdir() if p.is_dir()], key=lambda p: natural_key(p.name))\
\
lines = []\
lines.append("# Lesson Index (24 sessions)\\n\\n")\
lines.append("This folder contains the full lesson sequence and artifacts for each session.\\n\\n")\
\
for p in items:\
    lines.append(f"- [\{p.name\}](\{p.name\}/)\\n")\
\
out.write_text("".join(lines), encoding="utf-8")\
print(f"Wrote: \{out\}")}