#!/usr/bin/env python3
"""Advent of Code 2018 - Day 5: Alchemical Reduction"""

def react_polymer(polymer):
    """Reduce polymer by removing adjacent units that react (same letter, different case)"""
    stack = []
    for unit in polymer:
        if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)

def solve():
    with open('/Users/adamemery/advent-of-code/2018/input5', 'r') as f:
        polymer = f.read().strip()

    # Part 1: Length after full reduction
    part1 = react_polymer(polymer)

    # Part 2: Shortest polymer after removing one unit type
    unit_types = set(polymer.lower())
    min_length = len(polymer)

    for unit_type in unit_types:
        # Remove all instances of this unit type (both cases)
        filtered = [c for c in polymer if c.lower() != unit_type]
        length = react_polymer(filtered)
        min_length = min(min_length, length)

    part2 = min_length

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    solve()
