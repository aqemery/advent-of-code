#!/usr/bin/env python3
"""Advent of Code 2018 Day 6: Chronal Coordinates"""

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve():
    # Parse input
    with open('input6') as f:
        coords = []
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(', '))
                coords.append((x, y))

    # Find bounding box
    min_x = min(c[0] for c in coords)
    max_x = max(c[0] for c in coords)
    min_y = min(c[1] for c in coords)
    max_y = max(c[1] for c in coords)

    # Part 1: Find largest finite area
    area = {}
    infinite = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # Find closest coordinate(s)
            distances = [(manhattan_distance((x, y), c), i) for i, c in enumerate(coords)]
            distances.sort()

            if distances[0][0] != distances[1][0]:  # Not tied
                closest = distances[0][1]
                area[closest] = area.get(closest, 0) + 1

                # If on boundary, mark as infinite
                if x == min_x or x == max_x or y == min_y or y == max_y:
                    infinite.add(closest)

    # Find largest finite area
    part1 = max(area[i] for i in area if i not in infinite)

    # Part 2: Find region with total distance < 10000
    part2 = 0
    # Expand search area a bit beyond bounding box
    margin = 10000 // len(coords)
    for x in range(min_x - margin, max_x + margin + 1):
        for y in range(min_y - margin, max_y + margin + 1):
            total = sum(manhattan_distance((x, y), c) for c in coords)
            if total < 10000:
                part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    solve()
