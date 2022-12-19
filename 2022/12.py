import sys
from collections import deque


def parseStart(data):
    for y, d in enumerate(data):
        for x, c in enumerate(d):
            if c == "S":
                return (x, y, ord("a"), 0)


def runFrom(data, start):
    sx, sy, _, _ = start
    visited = set([(sx, sy)])
    queue = deque([start])
    while queue:
        x, y, v, steps = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in visited:
                try:
                    nv = data[ny][nx]
                    if nv == "E":
                        if ord("z") <= v + 1:
                            return steps + 1
                        continue

                    niv = ord(nv)
                    if niv <= v + 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, niv, steps + 1))
                except IndexError:
                    pass


def part1(data):
    start = parseStart(data)
    return runFrom(data, start)


def part2(data):
    runs = []
    for y, d in enumerate(data):
        for x, c in enumerate(d):
            if c == "a":
                if r := runFrom(data, (x, y, ord("a"), 0)):
                    runs.append(r)
    return min(runs)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
