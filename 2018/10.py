#!/usr/bin/env python3
"""Advent of Code 2018 Day 10: The Stars Align"""

import re

def solve():
    with open('input10') as f:
        lines = f.read().strip().split('\n')

    # Parse positions and velocities
    pattern = r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>'

    positions = []
    velocities = []

    for line in lines:
        match = re.search(pattern, line)
        if match:
            px, py, vx, vy = map(int, match.groups())
            positions.append([px, py])
            velocities.append([vx, vy])

    # Find when the bounding box is smallest (stars aligned)
    def get_bounds(positions):
        xs = [p[0] for p in positions]
        ys = [p[1] for p in positions]
        return min(xs), max(xs), min(ys), max(ys)

    def get_area(positions):
        min_x, max_x, min_y, max_y = get_bounds(positions)
        return (max_x - min_x) * (max_y - min_y)

    # Advance time until area starts increasing
    prev_area = float('inf')
    seconds = 0

    while True:
        curr_area = get_area(positions)

        if curr_area > prev_area:
            # Went too far, step back
            for i in range(len(positions)):
                positions[i][0] -= velocities[i][0]
                positions[i][1] -= velocities[i][1]
            seconds -= 1
            break

        prev_area = curr_area

        # Advance
        for i in range(len(positions)):
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]
        seconds += 1

    # Render the message
    min_x, max_x, min_y, max_y = get_bounds(positions)

    # Create grid
    points = set((p[0], p[1]) for p in positions)

    print("Part 1:")
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                row += '#'
            else:
                row += '.'
        print(row)

    print(f"Part 2: {seconds}")

if __name__ == '__main__':
    solve()
