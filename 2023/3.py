import sys
from collections import defaultdict
from math import prod


def around(x, y):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            yield x + dx, y + dy


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    stars = set()
    simbols = set()
    parts = []
    for y, line in enumerate(d):
        checks = set()
        number = ""
        for x, c in enumerate(line):
            if c.isdigit():
                number += c
                checks.update(around(x, y))
                continue

            if number:
                parts.append((number, checks))
                number = ""
                checks = set()

            if c != ".":
                simbols.add((x, y))
            if c == "*":
                stars.add((x, y))
        if number:
            parts.append((number, checks))
            number = ""
            checks = set()

    total = 0
    for num, check in parts:
        for c in check:
            if c in simbols:
                break
        else:
            continue
        total += int(num)
    print("part 1:", total)

    gears = defaultdict(list)
    for num, check in parts:
        for c in check:
            if c in stars:
                gears[c].append(int(num))
    gr = sum(prod(vals) for vals in gears.values() if len(vals) == 2)

    print("part 2:", gr)
