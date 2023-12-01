import sys


def part1(data):
    total = 0
    for line in data:
        values = [c for c in line if c.isdigit()]
        total += int(values[0] + values[-1])
    return total


def part2(data):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    for line in data:
        values = ""
        for index, c in enumerate(line):
            if c.isdigit():
                values += c
            else:
                for i, w in enumerate(words):
                    if line[index:].startswith(w):
                        values += str(i + 1)
                        break

        total += int(values[0] + values[-1])
    return total


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
