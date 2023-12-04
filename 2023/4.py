import sys
from collections import Counter


def part1(data):
    total = 0
    for line in data:
        a, b = [set(map(int, l.split())) for l in line.split(": ")[-1].split("|")]
        if winners := len(a & b):
            card_total = 1
            for _ in range(winners - 1):
                card_total *= 2
            total += card_total
    return total


def part2(data):
    more = Counter()
    for index, line in enumerate(data):
        a, b = [set(map(int, l.split())) for l in line.split(": ")[-1].split("|")]
        if winners := len(a & b):
            more.update(
                n
                for _ in range(more[index] + 1)
                for n in range(index + 1, index + winners + 1)
            )
    return sum(more.values()) + len(data)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
