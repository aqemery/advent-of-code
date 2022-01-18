import sys
from itertools import combinations
from math import prod


def part1(data):
    total = 0
    for d in data:
        areas = [c[0] * c[1] for c in combinations(d, 2)]
        total += 2 * sum(areas) + min(areas)

    return total


def part2(data):
    total = 0
    for d in data:
        order = list(d)
        order.sort()
        total += sum(order[:2]) * 2 + prod(d)

    return total


if __name__ == "__main__":
    i = [list(map(int, l.split("x"))) for l in sys.stdin.read().split("\n")]
    print("part 1:", part1(i))
    print("part 2:", part2(i))
