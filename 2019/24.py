#!/usr/bin/env python3
"""Advent of Code 2019 Day 24: Planet of Discord"""

def parse_input(filename):
    """Parse input file into a set of bug positions."""
    bugs = set()
    with open(filename) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char == '#':
                    bugs.add((x, y))
    return bugs

def get_adjacent(x, y):
    """Get adjacent positions for part 1."""
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def biodiversity(bugs):
    """Calculate biodiversity rating."""
    total = 0
    for x, y in bugs:
        if 0 <= x < 5 and 0 <= y < 5:
            pos = y * 5 + x
            total += 2 ** pos
    return total

def step_part1(bugs):
    """Perform one step of the simulation for part 1."""
    new_bugs = set()

    # Check all positions in 5x5 grid
    for y in range(5):
        for x in range(5):
            adjacent_bugs = sum(1 for ax, ay in get_adjacent(x, y)
                              if (ax, ay) in bugs)

            if (x, y) in bugs:
                # Bug survives only if exactly 1 adjacent bug
                if adjacent_bugs == 1:
                    new_bugs.add((x, y))
            else:
                # Empty space becomes bug if 1 or 2 adjacent bugs
                if adjacent_bugs in (1, 2):
                    new_bugs.add((x, y))

    return new_bugs

def part1(bugs):
    """Find first repeating layout and return its biodiversity."""
    seen = set()
    current = frozenset(bugs)

    while current not in seen:
        seen.add(current)
        current = frozenset(step_part1(current))

    return biodiversity(current)

def get_adjacent_recursive(x, y, level):
    """Get adjacent positions for part 2 (recursive grids).

    Returns list of (x, y, level) tuples.
    """
    adjacent = []

    # Standard adjacent positions
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        # Check if we go to outer level (off edge)
        if nx < 0:  # Left edge -> outer level position (1, 2)
            adjacent.append((1, 2, level - 1))
        elif nx > 4:  # Right edge -> outer level position (3, 2)
            adjacent.append((3, 2, level - 1))
        elif ny < 0:  # Top edge -> outer level position (2, 1)
            adjacent.append((2, 1, level - 1))
        elif ny > 4:  # Bottom edge -> outer level position (2, 3)
            adjacent.append((2, 3, level - 1))
        elif nx == 2 and ny == 2:  # Center -> inner level
            # Which edge of the inner level depends on direction
            if dx == 1:  # Coming from left, so inner left edge
                for iy in range(5):
                    adjacent.append((0, iy, level + 1))
            elif dx == -1:  # Coming from right, so inner right edge
                for iy in range(5):
                    adjacent.append((4, iy, level + 1))
            elif dy == 1:  # Coming from top, so inner top edge
                for ix in range(5):
                    adjacent.append((ix, 0, level + 1))
            elif dy == -1:  # Coming from bottom, so inner bottom edge
                for ix in range(5):
                    adjacent.append((ix, 4, level + 1))
        else:
            adjacent.append((nx, ny, level))

    return adjacent

def step_part2(bugs):
    """Perform one step of the simulation for part 2 (recursive)."""
    new_bugs = set()

    # Find range of levels to check (need to check one beyond current range)
    if bugs:
        min_level = min(level for x, y, level in bugs) - 1
        max_level = max(level for x, y, level in bugs) + 1
    else:
        min_level, max_level = 0, 0

    # Check all positions in all levels
    for level in range(min_level, max_level + 1):
        for y in range(5):
            for x in range(5):
                # Skip center tile (it's the recursive portal)
                if x == 2 and y == 2:
                    continue

                adjacent = get_adjacent_recursive(x, y, level)
                adjacent_bugs = sum(1 for pos in adjacent if pos in bugs)

                if (x, y, level) in bugs:
                    # Bug survives only if exactly 1 adjacent bug
                    if adjacent_bugs == 1:
                        new_bugs.add((x, y, level))
                else:
                    # Empty space becomes bug if 1 or 2 adjacent bugs
                    if adjacent_bugs in (1, 2):
                        new_bugs.add((x, y, level))

    return new_bugs

def part2(bugs, minutes=200):
    """Count total bugs after given minutes with recursive grids."""
    # Convert to 3D coordinates (x, y, level)
    current = {(x, y, 0) for x, y in bugs}

    for _ in range(minutes):
        current = step_part2(current)

    return len(current)

def main():
    input_file = "/Users/adamemery/advent-of-code/2019/input24"
    bugs = parse_input(input_file)

    p1 = part1(bugs)
    p2 = part2(bugs)

    print(f"Day 24: Part 1 = {p1}, Part 2 = {p2}")

if __name__ == "__main__":
    main()
