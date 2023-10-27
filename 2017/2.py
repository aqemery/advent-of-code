import sys
from itertools import combinations


def solve(data, times):
    return


def part1(data):
    total = 0
    for line in data:
        values = [int(d) for d in line.split()]
        total += max(values) - min(values)
    return total


def part2(data):
    total = 0
    for line in data:
        values = [int(d) for d in line.split()]
        for a, b in combinations(values, 2):
            if a % b == 0:
                total += a // b
            elif b % a == 0:
                total += b // a
    return total


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
