import sys


def part1(data):
    groups = [map(int, g.split("-")) for g in data]
    total = 0
    for a, b in groups:
        for i in range(a, b + 1):
            value = str(i)
            slice = len(value) // 2

            if value[:slice] == value[slice:]:
                total += i
    return total


def part2(data):
    groups = [map(int, g.split("-")) for g in data]

    total = 0
    for a, b in groups:
        for i in range(a, b + 1):
            value = str(i)
            for slice in range(1, len(value) // 2 + 1):
                slices = [value[i : i + slice] for i in range(0, len(value), slice)]
                check = all(s == slices[0] for s in slices)
                if check:
                    total += i
                    break
    return total


if __name__ == "__main__":
    d = sys.stdin.read().split(",")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
