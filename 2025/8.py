import sys
from collections import defaultdict, deque
from itertools import combinations
from math import prod, sqrt


def part1(distances):
    to_connect = distances[:1000]
    connections = defaultdict(set)

    for _, a, b in to_connect:
        connections[a].add(b)
        connections[b].add(a)

    circuits = []
    visited = set()
    for conn in connections:
        if conn in visited:
            continue
        before = len(visited)
        queue = deque([conn])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            for c in connections[node]:
                if c not in visited:
                    queue.append(c)
        circuits.append(len(visited) - before)

    circuits.sort(reverse=True)
    return prod(circuits[:3])


def part2(distances):
    connections = defaultdict(set)
    for _, a, b in distances:
        connections[a].add(b)
        connections[b].add(a)

        visited = set()
        queue = deque([list(connections.keys())[0]])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            for c in connections[node]:
                if c not in visited:
                    queue.append(c)

        if len(visited) == len(data):
            return a[0] * b[0]


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    data = [[int(v) for v in l.split(",")] for l in d if l]
    distances = []
    for (a, b, c), (x, y, z) in combinations(data, 2):
        dist = sqrt((a - x) ** 2 + (b - y) ** 2 + (c - z) ** 2)
        distances.append((dist, (a, b, c), (x, y, z)))
    distances.sort()

    print("part 1:", part1(distances))
    print("part 2:", part2(distances))
