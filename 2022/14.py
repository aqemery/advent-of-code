import sys


def axisRange(s, e):
    points = sorted([s, e])
    return [p for p in range(points[0], points[1] + 1)]


def solve(data, void=True):
    blocked = set()
    for d in data:
        path = [[int(v) for v in n.split(',')] for n in d.split(" -> ")]
        for i, p in enumerate(path[1:]):
            sx, sy = path[i]
            px, py = p
            if sx == px:
                blocked.update((sx, y) for y in axisRange(sy, py))
            elif sy == py:
                blocked.update((x, sy) for x in axisRange(sx, px))

    void_lim = max(y for _,y in blocked)
    floor = max(y for _,y in blocked) + 1
    total = 0
    while True:
        sx = 500
        sy = 0
        if (sx, sy) in blocked:
            return total
        while True:
            if not (sx, sy + 1) in blocked and sy < floor:
                sy += 1
                if void and sy > void_lim:
                    return total
            elif not (sx -1, sy + 1) in blocked and sy < floor:
                sy += 1
                sx -= 1
            elif not (sx + 1, sy + 1) in blocked and sy < floor:
                sy += 1
                sx += 1
            else:
                blocked.add((sx, sy))
                total += 1
                break


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, void=False))
