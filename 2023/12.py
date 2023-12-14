import sys
from functools import cache
import re


def next_segments(c, v):
    return [
        c[m.end(1) :]
        for m in re.finditer(f"(?=([#?]{ {v} }[.?]{ {1} }))", c)
        if not c[: m.start(1)].count("#")
    ]


@cache
def possible(unknown, values):
    if len(values) == 1:
        return sum(
            1
            for m in re.finditer(f"(?=([#?]{ {values[-1]} }))", unknown)
            if not unknown[: m.start(1)].count("#")
            and not unknown[m.end(1) :].count("#")
        )

    return sum(possible(c, values[1:]) for c in next_segments(unknown, values[0]))


def part1(data):
    total = 0
    for line in data:
        unknown, values = line.split()
        values = tuple(int(v) for v in values.split(","))
        total += possible(unknown, values)
    return total


def part2(data):
    big_data = []
    for line in data:
        unknown, values = line.split()
        values = ",".join(values.split(",") * 5)
        unknown = unknown + ("?" + unknown) * 4
        big_data.append(f"{unknown} {values}")
    return part1(big_data)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
