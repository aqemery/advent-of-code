#!/usr/bin/env python3
"""Advent of Code 2018 Day 25: Four-Dimensional Adventure"""

def solve(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')

    points = []
    for line in lines:
        coords = tuple(map(int, line.split(',')))
        points.append(coords)

    def manhattan(p1, p2):
        return sum(abs(a - b) for a, b in zip(p1, p2))

    # Union-Find for constellation detection
    parent = list(range(len(points)))
    rank = [0] * len(points)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1

    # Connect points that are within distance 3
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if manhattan(points[i], points[j]) <= 3:
                union(i, j)

    # Count unique constellations
    constellations = len(set(find(i) for i in range(len(points))))

    return constellations

if __name__ == '__main__':
    part1 = solve('/Users/adamemery/advent-of-code/2018/input25')
    print(f"Part 1: {part1}")
    print("Part 2: (free star - no puzzle)")
