from collections import Counter


def part1(floors):
    counts = Counter(floors)
    return counts["("] - counts[")"]


def part2(floors):
    level = 0
    for i, v in enumerate(floors):
        if v == "(":
            level += 1
        else:
            level -= 1
        if level < 0:
            return i + 1


if __name__ == "__main__":
    i = input()
    print("part 1:", part1(i))
    print("part 2:", part2(i))
