#!/usr/bin/env python3
"""Advent of Code 2017 Day 24: Electromagnetic Moat"""

def parse_input(filename):
    """Parse the input file and return list of components as tuples."""
    components = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                a, b = map(int, line.split('/'))
                components.append((a, b))
    return components

def build_bridges(components, current_port, used, current_strength, current_length):
    """
    DFS to find all possible bridges.
    Returns (max_strength, max_length, strength_of_longest)
    """
    max_strength = current_strength
    max_length = current_length
    strength_of_longest = current_strength

    for i, (a, b) in enumerate(components):
        if i in used:
            continue

        # Check if this component can connect
        if a == current_port or b == current_port:
            # Determine the next port
            next_port = b if a == current_port else a
            new_strength = current_strength + a + b

            # Mark as used and recurse
            used.add(i)
            result = build_bridges(
                components,
                next_port,
                used,
                new_strength,
                current_length + 1
            )
            used.remove(i)

            # Update max strength (Part 1)
            if result[0] > max_strength:
                max_strength = result[0]

            # Update longest bridge tracking (Part 2)
            if result[1] > max_length:
                max_length = result[1]
                strength_of_longest = result[2]
            elif result[1] == max_length:
                if result[2] > strength_of_longest:
                    strength_of_longest = result[2]

    return (max_strength, max_length, strength_of_longest)

def solve(filename):
    """Solve both parts of the puzzle."""
    components = parse_input(filename)

    # Start building from port 0
    max_strength, max_length, strength_of_longest = build_bridges(
        components,
        current_port=0,
        used=set(),
        current_strength=0,
        current_length=0
    )

    return max_strength, strength_of_longest

if __name__ == "__main__":
    part1, part2 = solve("/Users/adamemery/advent-of-code/2017/input24")
    print(f"Day 24: Part 1 = {part1}, Part 2 = {part2}")
