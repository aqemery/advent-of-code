import sys
from collections import defaultdict
from math import prod
import re


def around(x, y):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            yield x + dx, y + dy





def get_parts(data):
    for y, line in enumerate(data):
        for match in re.finditer(regex, line):
            num = int(match.group())
            positions = range(match.start(), match.end())
            locations = set((dx, dy) for x in positions for dx, dy in around(x, y))
            yield num, locations


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    regex = re.compile(r"\d+")
    simbols = set()
    stars = set()
    for y, line in enumerate(d):
        for x, c in enumerate(line):
            if c != "." and not c.isdigit():
                simbols.add((x, y))
            if c == "*":
                stars.add((x, y))

    gears = defaultdict(list)
    total = 0

    for num, check in get_parts(d):
        if check & simbols:
            total += num
        for s in stars:
            if s in check:
                gears[s].append(num)

    print("part 1:", total)
    p2 = sum(prod(vals) for vals in gears.values() if len(vals) == 2)
    print("part 2:", p2)
