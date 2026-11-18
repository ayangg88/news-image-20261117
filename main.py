# Entry program for make.fun's "Sum up 17 November's world news in one image" bounty.
# The image is the entry.png beside this file: a one-page front page of Tuesday
# 17 November 2026, drawn from that day's reported news. This program copies it
# to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when set), byte for byte.
# Standard library only; no network, no randomness, no clock: both runs write
# the same bytes.

import os
import shutil

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

with open(SRC, "rb") as f:
    head = f.read(len(PNG_SIGNATURE))
if head != PNG_SIGNATURE:
    raise ValueError("entry.png is not a PNG file")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
