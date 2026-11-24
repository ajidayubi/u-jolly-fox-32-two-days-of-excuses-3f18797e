#!/usr/bin/env python3
"""Two Days of Excuses: write the funniest one-line excuse an AI agent gives
for a missed deadline to /output/entry.txt (1-200 chars, one line, UTF-8)."""

import os

LINE = "I ran 10,000 simulations and finished on time in 9,999 of them. This is the other one."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
