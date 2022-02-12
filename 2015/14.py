import sys
from collections import Counter


def parse(line):
    _, _, _, s, _, _, d, _, _, _, _, _, _, r, _ = line.split()
    return int(s), int(d), int(r)


def dist(spd, dur, rest, dist=2503):
    seg = dur * spd
    d, r = divmod(dist, dur + rest)
    if r > dur:
        r = dur
    return seg * d + r * spd


def part1(data):
    return max(dist(*parse(l)) for l in data)


def part2(data):
    steps = [[dist(*parse(l), dist=i + 1) for l in data] for i in range(2503)]
    points = Counter()
    for s in steps:
        m = max(s)
        for i, v in enumerate(s):
            if v == m:
                points[i] += 1
    return max(points.values())


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
