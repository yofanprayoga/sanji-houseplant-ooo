#!/usr/bin/env python3
"""Sanji's houseplant out-of-office auto-reply.

Writes one out-of-office auto-reply, at most 120 characters, to
/output/entry.txt. The line is the whole entry.
"""

import os

LINE = "I am out of office. My desk is my entire world, and someone keeps watering me with coffee."


def main():
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
