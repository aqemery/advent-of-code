import sys
import string


def part1(data):
    total = 0
    for d in data:
        l = len(d) // 2
        a = set(d[:l])
        b = set(d[l:])
        items = a.intersection(b)
        total += sum(string.ascii_letters.index(i) + 1 for i in items)
    return total


def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        group = [set(data[l]) for l in range(i, i + 3)]
        items = group[0].intersection(*group[1:])
        total += sum(string.ascii_letters.index(i) + 1 for i in items)
    return total


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
