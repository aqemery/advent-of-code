import sys
from itertools import combinations
from collections import deque


def part1(data):
    sides = 6 * len(data)
    for c1, c2 in combinations(data, 2):
        x_same = c1[0] == c2[0]
        y_same = c1[1] == c2[1]
        z_same = c1[2] == c2[2]

        if x_same and y_same:
            if abs(c1[2] - c2[2]) == 1:
                sides -= 2
        elif x_same and z_same:
            if abs(c1[1] - c2[1]) == 1:
                sides -= 2
        elif y_same and z_same:
            if abs(c1[0] - c2[0]) == 1:
                sides -= 2
    return sides


def offsets(x, y, z):
    offsets = []
    for delta in [-1, 1]:
        pos1 = (x + delta, y, z)
        pos2 = (x, y + delta, z)
        pos3 = (x, y, z + delta)
        offsets += [pos1, pos2, pos3]
    return offsets


def part2(data):
    cubes = set(data)
    min_v = -2
    max_v = max(x for d in data for x in d) + 2
    q = deque([(min_v, min_v, min_v)])
    visited = set()

    total = 0

    while q:
        pos = q.popleft()
        if pos in visited:
            continue

        if any(i < min_v or i > max_v for i in pos):
            continue

        if pos in cubes:
            total += 1
            continue

        visited.add(pos)
        q.extend(offsets(*pos))
    return total


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    d = [tuple(int(x) for x in d.split(",")) for d in data]
    print("part 1:", part1(d))
    print("part 2:", part2(d))
