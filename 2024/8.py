import sys
from collections import defaultdict
from itertools import combinations

lines = sys.stdin.read().splitlines()
nodes = defaultdict(set)

bounds = (len(lines[0]) - 1, len(lines) - 1)

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c != ".":
            nodes[c].add((x, y))

antinodes = set()


def add(x, y):
    if x >= 0 and x <= bounds[0] and y >= 0 and y <= bounds[1]:
        antinodes.add((x, y))
        return True
    return False


for matches in nodes.values():
    for a, b in combinations(matches, 2):
        delta = (b[0] - a[0], b[1] - a[1])
        add(a[0] - delta[0], a[1] - delta[1])
        add(b[0] + delta[0], b[1] + delta[1])

print("p1:", len(antinodes))

antinodes = set()

for matches in nodes.values():
    for a, b in combinations(matches, 2):
        delta = (b[0] - a[0], b[1] - a[1])
        current = a
        while add(*current):
            current = (current[0] - delta[0], current[1] - delta[1])

        current = a
        while add(*current):
            current = (current[0] + delta[0], current[1] + delta[1])

print("p2:", len(antinodes))
