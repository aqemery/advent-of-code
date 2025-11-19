#!/usr/bin/env python3
"""Advent of Code 2018 - Day 1: Chronal Calibration"""

def solve():
    with open('/Users/adamemery/advent-of-code/2018/input1', 'r') as f:
        changes = [int(line.strip()) for line in f if line.strip()]

    # Part 1: Sum of all frequency changes
    part1 = sum(changes)

    # Part 2: First frequency reached twice
    seen = {0}
    freq = 0
    part2 = None
    while part2 is None:
        for change in changes:
            freq += change
            if freq in seen:
                part2 = freq
                break
            seen.add(freq)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    solve()
