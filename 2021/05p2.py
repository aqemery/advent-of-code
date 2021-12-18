import sys

vents = [
    [list(map(int, c.split(","))) for c in l.split(" -> ")]
    for l in sys.stdin.read().split("\n")
]
vent_map = {}


def add_coord(x, y):
    global vent_map
    try:
        vent_map[(x, y)] += 1
    except KeyError:
        vent_map[(x, y)] = 1


for v in vents:
    c, end = v
    step = [0 if d == 0 else d / abs(d) for d in [end[0] - c[0], end[1] - c[1]]]
    add_coord(*c)
    while c != end:
        c = list(map(sum, zip(c, step)))
        add_coord(*c)

print(len([v for v in vent_map.values() if v > 1]))
