import sys
from collections import deque
from contextlib import suppress


def part1(data, start=(0, 0, 1, 0)):
    beams = deque([start])
    energized = set()
    visited = set()
    while beams:
        x, y, dx, dy = beams.popleft()
        with suppress(IndexError):
            while tile := data[y][x]:
                if (x, y, dx, dy) in visited:
                    break
                visited.add((x, y, dx, dy))
                energized.add((x, y))
                if tile == "\\":
                    dx, dy = dy, dx
                elif tile == "/":
                    dx, dy = -dy, -dx
                elif tile == "|" and dy == 0:
                    beams.append((x, y, 0, 1))
                    beams.append((x, y, 0, -1))
                    break
                elif tile == "-" and dx == 0:
                    beams.append((x, y, 1, 0))
                    beams.append((x, y, -1, 0))
                    break
                x += dx
                y += dy
                if x < 0 or y < 0:
                    break
    return len(energized)


def part2(data):
    height = len(data)
    width = len(data[0])
    horiz = [[(0, y, 1, 0), (width - 1, y, -1, 0)] for y in range(height)]
    vert = [[(x, 0, 0, 1), (x, height - 1, 0, -1)] for x in range(width)]
    return max(part1(data, b) for a in horiz + vert for b in a)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
