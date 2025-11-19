#!/usr/bin/env python3
"""Advent of Code 2018 - Day 3: No Matter How You Slice It"""

import re
from collections import defaultdict

def solve():
    with open('/Users/adamemery/advent-of-code/2018/input3', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Parse claims: #ID @ X,Y: WxH
    claims = []
    for line in lines:
        match = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        if match:
            claim_id = int(match.group(1))
            x = int(match.group(2))
            y = int(match.group(3))
            w = int(match.group(4))
            h = int(match.group(5))
            claims.append((claim_id, x, y, w, h))

    # Count how many claims cover each square inch
    fabric = defaultdict(int)
    for claim_id, x, y, w, h in claims:
        for dx in range(w):
            for dy in range(h):
                fabric[(x + dx, y + dy)] += 1

    # Part 1: Count squares with 2+ claims
    part1 = sum(1 for count in fabric.values() if count >= 2)

    # Part 2: Find claim with no overlaps
    part2 = None
    for claim_id, x, y, w, h in claims:
        overlaps = False
        for dx in range(w):
            for dy in range(h):
                if fabric[(x + dx, y + dy)] > 1:
                    overlaps = True
                    break
            if overlaps:
                break
        if not overlaps:
            part2 = claim_id
            break

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    solve()
