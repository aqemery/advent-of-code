import math
from statistics import median


def part1(crabs):
    med = int(median(crabs))
    return sum([abs(med - c) for c in crabs])


def part2(crabs):
    average = math.floor(sum(crabs) / len(crabs))
    return sum([sum(range(1, abs(average - c) + 1)) for c in crabs])


if __name__ == "__main__":
    lines = list(map(int, input().split(",")))
    print("part 1:", part1(lines))
    print("part 2:", part2(lines))
