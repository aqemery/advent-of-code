import sys
from collections import deque
from itertools import count
from math import lcm


def part1(start="AAA", end=lambda x: x == "ZZZ"):
    current = start
    q = deque(dirs)
    for times in count():
        if end(current):
            return times
        current = path[current][q[0]]
        q.rotate(-1)


def part2():
    current = set(k for k in path.keys() if k[-1] == "A")
    return lcm(*[part1(start=s, end=lambda x: x[-1] == "Z") for s in current])


if __name__ == "__main__":
    dirs, lines = sys.stdin.read().split("\n\n")
    dirs = [d == "R" for d in dirs]
    lines = "".join(c for c in lines if c not in "=(),")
    path = {line.split()[0]: line.split()[1:] for line in lines.split("\n")}
    print("part 1:", part1())
    print("part 2:", part2())
