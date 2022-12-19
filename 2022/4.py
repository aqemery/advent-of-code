import sys


def part1(data):
    total = 0
    groups = (d.split(",") for d in data)
    groups = [[[int(i) for i in e.split("-")] for e in g] for g in groups]
    for a, b in groups:
        if a[0] <= b[0] and a[1] >= b[1]:
            total += 1
        elif b[0] <= a[0] and b[1] >= a[1]:
            total += 1

    return total


def part2(data):
    total = 0
    groups = (d.split(",") for d in data)
    groups = [[[int(i) for i in e.split("-")] for e in g] for g in groups]
    for a, b in groups:
        if b[0] <= a[0] <= b[1] or a[0] <= b[0] <= a[1]:
            total += 1

    return total


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
