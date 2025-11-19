#!/usr/bin/env python3
"""Advent of Code 2018 - Day 2: Inventory Management System"""

from collections import Counter

def solve():
    with open('/Users/adamemery/advent-of-code/2018/input2', 'r') as f:
        box_ids = [line.strip() for line in f if line.strip()]

    # Part 1: Checksum (count of boxes with exactly 2 of any letter * count with exactly 3)
    twos = 0
    threes = 0
    for box_id in box_ids:
        counts = Counter(box_id)
        if 2 in counts.values():
            twos += 1
        if 3 in counts.values():
            threes += 1

    part1 = twos * threes

    # Part 2: Find boxes differing by exactly one character
    part2 = None
    for i, id1 in enumerate(box_ids):
        for id2 in box_ids[i+1:]:
            diff_positions = [j for j in range(len(id1)) if id1[j] != id2[j]]
            if len(diff_positions) == 1:
                pos = diff_positions[0]
                part2 = id1[:pos] + id1[pos+1:]
                break
        if part2:
            break

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    solve()
