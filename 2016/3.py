import sys
from itertools import batched


def part1(data):
    possible = 0
    for d in data:
        a, b, c = sorted(int(x) for x in d.split())
        if a + b > c:
            possible += 1
    return possible


def part2(data):
    possible = 0
    for lines in batched(data, 3):
        triangles = [[int(x) for x in l.split()] for l in lines]
        for t in zip(*triangles):
            a, b, c = sorted(t)
            if a + b > c:
                possible += 1
    return possible


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
