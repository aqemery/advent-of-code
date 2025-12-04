import sys

def part1(data):
    total = 0
    points = set()
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == "@":
                points.add((x, y))

    for x, y in points:
        ajacent = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if (x + dx, y + dy) in points:
                    ajacent += 1

        if ajacent < 4:
            total += 1

    return total


def part2(data):
    total = 0
    points = set()
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == "@":
                points.add((x, y))

    removed = True
    while removed:
        removed = False
        for x, y in points:
            ajacent = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if (x + dx, y + dy) in points:
                        ajacent += 1

            if ajacent < 4:
                points.remove((x, y))
                removed = True
                total += 1
                break

    return total


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
