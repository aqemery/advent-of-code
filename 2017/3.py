import sys
from collections import deque


def part1(data):
    visited = set()
    x, y = 0, 0
    visited.add((x, y))
    i = 1
    dirs = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    dx, dy = dirs[0]
    dirs.rotate(-1)
    nx, ny = dirs[0]
    while True:
        i += 1
        if (x + nx, y + ny) not in visited:
            dx, dy = dirs[0]
            dirs.rotate(-1)
            nx, ny = dirs[0]

        x += dx
        y += dy
        visited.add((x, y))

        if i == 361527:
            return abs(x) + abs(y)


def part2(data):
    visited = {}
    x, y = 0, 0
    visited[(x, y)] = 1
    dirs = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    dx, dy = dirs[0]
    dirs.rotate(-1)
    nx, ny = dirs[0]
    while True:
        if (x + nx, y + ny) not in visited:
            dx, dy = dirs[0]
            dirs.rotate(-1)
            nx, ny = dirs[0]

        x += dx
        y += dy

        value = 0
        for around_x in range(x - 1, x + 2):
            for around_y in range(y - 1, y + 2):
                value += visited.get((around_x, around_y), 0)

        visited[(x, y)] = value

        if value >= 361527:
            return value


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
