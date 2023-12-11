import sys
from itertools import combinations


def solve(data, gap=1):
    gpos = [(x, y) for y, l in enumerate(data) for x, c in enumerate(l) if c == "#"]
    x_expand = [x for x in range(len(data[0])) if not any(gx == x for gx, _ in gpos)]
    y_expand = [y for y in range(len(data)) if not any(gy == y for _, gy in gpos)]
    gpos = [
        (
            gx + (sum(gx > xp for xp in x_expand) * gap),
            gy + (sum(gy > yp for yp in y_expand) * gap),
        )
        for gx, gy in gpos
    ]
    return sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in combinations(gpos, 2))


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, 1_000_000 - 1))
