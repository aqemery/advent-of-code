#!/usr/bin/env python3
"""Advent of Code 2018 Day 11: Chronal Charge"""

def get_power_level(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    power -= 5
    return power

def solve(serial):
    # Build 300x300 grid of power levels
    grid = [[0] * 301 for _ in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            grid[y][x] = get_power_level(x, y, serial)

    # Build summed area table for fast square sum queries
    sat = [[0] * 302 for _ in range(302)]
    for y in range(1, 301):
        for x in range(1, 301):
            sat[y][x] = grid[y][x] + sat[y-1][x] + sat[y][x-1] - sat[y-1][x-1]

    def get_square_sum(x, y, size):
        """Get sum of square with top-left corner at (x, y) and given size"""
        x1, y1 = x - 1, y - 1
        x2, y2 = x + size - 1, y + size - 1
        return sat[y2][x2] - sat[y1][x2] - sat[y2][x1] + sat[y1][x1]

    # Part 1: Find 3x3 square with largest total power
    best_power_3x3 = float('-inf')
    best_coord_3x3 = None

    for y in range(1, 299):
        for x in range(1, 299):
            power = get_square_sum(x, y, 3)
            if power > best_power_3x3:
                best_power_3x3 = power
                best_coord_3x3 = (x, y)

    # Part 2: Find any-size square with largest total power
    best_power_any = float('-inf')
    best_coord_any = None

    for size in range(1, 301):
        for y in range(1, 302 - size):
            for x in range(1, 302 - size):
                power = get_square_sum(x, y, size)
                if power > best_power_any:
                    best_power_any = power
                    best_coord_any = (x, y, size)

    return best_coord_3x3, best_coord_any

if __name__ == "__main__":
    with open("/Users/adamemery/advent-of-code/2018/input11") as f:
        serial = int(f.read().strip())

    part1, part2 = solve(serial)
    print(f"Part 1: {part1[0]},{part1[1]}")
    print(f"Part 2: {part2[0]},{part2[1]},{part2[2]}")
