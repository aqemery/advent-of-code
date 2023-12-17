import sys
from heapq import heappush, heappop
from contextlib import suppress


def consecutive(directions):
    total = 1
    with suppress(IndexError):
        for d in directions[::-1]:
            if not d == directions[-1]:
                break
            total += 1
    return total


def solve(forward=3, turn=0):
    states = [(0, 2, 0, 0, tuple()), (0, 3, 0, 0, tuple())]
    visited = set()
    with suppress(IndexError):
        while current := heappop(states):
            heat, index, x, y, directions = current
            dx, dy = dirs[index]
            x += dx
            y += dy
            directions = directions + tuple([index])
            if (x, y) not in grid or (x, y, directions[-forward:]) in visited:
                continue
            heat += grid[(x, y)]
            if (x, y) == (width, height):
                return heat
            visited.add((x, y, directions[-forward:]))
            cons = consecutive(directions)
            if cons <= forward:
                heappush(states, (heat, index, x, y, directions))
            if cons > turn:
                heappush(states, (heat, (index - 1) % 4, x, y, directions))
                heappush(states, (heat, (index + 1) % 4, x, y, directions))


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    grid = {(x, y): int(c) for y, row in enumerate(d) for x, c in enumerate(row)}
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    width = len(d[0]) - 1
    height = len(d) - 1

    print("part 1:", solve())
    print("part 2:", solve(10, 4))
