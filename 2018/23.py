#!/usr/bin/env python3
"""Advent of Code 2018 Day 23: Experimental Emergency Teleportation"""

import re
from heapq import heappush, heappop

def solve(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')

    bots = []
    for line in lines:
        match = re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', line)
        x, y, z, r = map(int, match.groups())
        bots.append((x, y, z, r))

    # Part 1: Find nanobot with largest radius, count bots in range
    strongest = max(bots, key=lambda b: b[3])
    sx, sy, sz, sr = strongest

    count = 0
    for x, y, z, r in bots:
        dist = abs(x - sx) + abs(y - sy) + abs(z - sz)
        if dist <= sr:
            count += 1

    part1 = count

    # Part 2: Find point in range of most bots, closest to origin
    # Use 3D coordinate compression / priority queue approach

    # For each bot, the range is a 3D octahedron
    # Transform to a different coordinate system where octahedron becomes a cube
    # Let u = x+y+z, v = x+y-z, w = x-y+z, t = x-y-z
    # Then |x-a| + |y-b| + |z-c| <= r becomes:
    # max(|u - (a+b+c)|, |v - (a+b-c)|, |w - (a-b+c)|, |t - (a-b-c)|) <= r

    # Use a divide and conquer approach with priority queue
    # Start with a large cube containing all bots
    # Split into smaller cubes, prioritizing by number of bots that could overlap

    def count_in_range(x, y, z, bots):
        """Count how many bots have (x, y, z) in their range"""
        count = 0
        for bx, by, bz, br in bots:
            if abs(x - bx) + abs(y - by) + abs(z - bz) <= br:
                count += 1
        return count

    def bot_distance_to_cube(bot, min_x, min_y, min_z, size):
        """Minimum Manhattan distance from bot to any point in cube"""
        bx, by, bz, br = bot

        # Find closest point in cube to bot center
        cx = max(min_x, min(bx, min_x + size - 1))
        cy = max(min_y, min(by, min_y + size - 1))
        cz = max(min_z, min(bz, min_z + size - 1))

        return abs(bx - cx) + abs(by - cy) + abs(bz - cz)

    def bots_possibly_in_cube(min_x, min_y, min_z, size, bots):
        """Count bots whose range could overlap with any point in the cube"""
        count = 0
        for bot in bots:
            dist = bot_distance_to_cube(bot, min_x, min_y, min_z, size)
            if dist <= bot[3]:
                count += 1
        return count

    # Find bounding box
    min_x = min(b[0] - b[3] for b in bots)
    max_x = max(b[0] + b[3] for b in bots)
    min_y = min(b[1] - b[3] for b in bots)
    max_y = max(b[1] + b[3] for b in bots)
    min_z = min(b[2] - b[3] for b in bots)
    max_z = max(b[2] + b[3] for b in bots)

    # Start with power of 2 size
    size = 1
    while size < max(max_x - min_x, max_y - min_y, max_z - min_z):
        size *= 2

    # Priority queue: (-num_bots, distance_to_origin, size, x, y, z)
    # We want max bots, then min distance, then smaller size
    initial_count = bots_possibly_in_cube(min_x, min_y, min_z, size, bots)
    initial_dist = abs(min_x) + abs(min_y) + abs(min_z)

    pq = [(-initial_count, initial_dist, size, min_x, min_y, min_z)]

    while pq:
        neg_count, dist, size, x, y, z = heappop(pq)

        if size == 1:
            # Single point, verify actual count
            actual = count_in_range(x, y, z, bots)
            if actual == -neg_count:
                part2 = abs(x) + abs(y) + abs(z)
                break
            continue

        # Split into 8 sub-cubes
        half = size // 2
        for dx in [0, half]:
            for dy in [0, half]:
                for dz in [0, half]:
                    nx, ny, nz = x + dx, y + dy, z + dz
                    new_size = half if half > 0 else 1

                    count = bots_possibly_in_cube(nx, ny, nz, new_size, bots)
                    if count == 0:
                        continue

                    # Distance to origin from closest point in cube
                    ox = max(nx, min(0, nx + new_size - 1))
                    oy = max(ny, min(0, ny + new_size - 1))
                    oz = max(nz, min(0, nz + new_size - 1))
                    origin_dist = abs(ox) + abs(oy) + abs(oz)

                    heappush(pq, (-count, origin_dist, new_size, nx, ny, nz))

    return part1, part2

if __name__ == '__main__':
    part1, part2 = solve('/Users/adamemery/advent-of-code/2018/input23')
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
