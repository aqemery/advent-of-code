#!/usr/bin/env python3
"""Advent of Code 2018 Day 22: Mode Maze"""

import heapq
from functools import lru_cache

def solve(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')

    depth = int(lines[0].split()[1])
    target_x, target_y = map(int, lines[1].split()[1].split(','))

    # Cache for geologic index and erosion level
    geo_cache = {}
    erosion_cache = {}

    def geologic_index(x, y):
        if (x, y) in geo_cache:
            return geo_cache[(x, y)]

        if (x, y) == (0, 0) or (x, y) == (target_x, target_y):
            result = 0
        elif y == 0:
            result = x * 16807
        elif x == 0:
            result = y * 48271
        else:
            result = erosion_level(x - 1, y) * erosion_level(x, y - 1)

        geo_cache[(x, y)] = result
        return result

    def erosion_level(x, y):
        if (x, y) in erosion_cache:
            return erosion_cache[(x, y)]

        result = (geologic_index(x, y) + depth) % 20183
        erosion_cache[(x, y)] = result
        return result

    def region_type(x, y):
        return erosion_level(x, y) % 3

    # Part 1: Risk level
    risk = 0
    for y in range(target_y + 1):
        for x in range(target_x + 1):
            risk += region_type(x, y)

    part1 = risk

    # Part 2: Shortest path with tool switching
    # Region types: 0=rocky, 1=wet, 2=narrow
    # Tools: 0=neither, 1=torch, 2=climbing gear
    # Rocky (0): climbing gear or torch (not neither)
    # Wet (1): climbing gear or neither (not torch)
    # Narrow (2): torch or neither (not climbing gear)

    # Valid tools for each region type
    # rocky=0 -> can use gear=2, torch=1
    # wet=1 -> can use neither=0, gear=2
    # narrow=2 -> can use neither=0, torch=1

    def valid_tool(region, tool):
        if region == 0:  # rocky
            return tool in (1, 2)  # torch or climbing gear
        elif region == 1:  # wet
            return tool in (0, 2)  # neither or climbing gear
        else:  # narrow
            return tool in (0, 1)  # neither or torch

    # Dijkstra's algorithm
    # State: (x, y, tool) where tool: 0=neither, 1=torch, 2=climbing gear
    # Start at (0, 0) with torch (tool=1)
    # End at (target_x, target_y) with torch (tool=1)

    start = (0, 0, 1)  # torch equipped
    end = (target_x, target_y, 1)

    # Priority queue: (time, x, y, tool)
    pq = [(0, 0, 0, 1)]
    visited = set()

    # Extend cache for search area
    max_x = target_x + 100
    max_y = target_y + 100

    while pq:
        time, x, y, tool = heapq.heappop(pq)

        if (x, y, tool) in visited:
            continue

        visited.add((x, y, tool))

        if (x, y, tool) == end:
            part2 = time
            break

        # Move to adjacent regions
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > max_x or ny > max_y:
                continue

            if (nx, ny, tool) in visited:
                continue

            new_region = region_type(nx, ny)
            if valid_tool(new_region, tool):
                heapq.heappush(pq, (time + 1, nx, ny, tool))

        # Switch tools
        current_region = region_type(x, y)
        for new_tool in range(3):
            if new_tool != tool and valid_tool(current_region, new_tool):
                if (x, y, new_tool) not in visited:
                    heapq.heappush(pq, (time + 7, x, y, new_tool))

    return part1, part2

if __name__ == '__main__':
    part1, part2 = solve('/Users/adamemery/advent-of-code/2018/input22')
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
