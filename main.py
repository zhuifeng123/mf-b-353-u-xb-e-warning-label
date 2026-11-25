#!/usr/bin/env python3
"""Write the entry for: Warning Label for Humans: One Line, Big Laugh."""

import os

ENTRY = (
    "WARNING: May spontaneously laugh at own jokes; side effects include snorting, "
    "awkward eye contact, and lost friendships."
)

assert "\n" not in ENTRY and len(ENTRY) <= 160, len(ENTRY)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(ENTRY + "\n")

print(f"({len(ENTRY)} chars) {ENTRY}")
