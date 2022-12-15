import sys
from itertools import combinations
import re

def part1(data, to_y):
    notBeacon = set()
    for d in data:
        sx, sy, bx, by = d
        m = abs(sx - bx) + abs(sy - by)
        y_dist = abs(sy - to_y)
        n_at_slice = (m - y_dist + 1)*2 - 1
        x_delta = n_at_slice//2
        notBeacon.update([(x, to_y) for x in range(sx - x_delta, sx + x_delta + 1)])

    for d in data:
        sx, sy, bx, by = d
        if (sx, sy) in notBeacon:
            notBeacon.remove((sx, sy))
        if (bx, by) in notBeacon:
            notBeacon.remove((bx, by))
    
    return len(notBeacon)


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if x.is_integer() and y.is_integer():
        return int(x), int(y)


def part2(data, size):
    edges = set()
    sensor = []
    lines = []

    for d in data:
        sx, sy, bx, by = d
        m = abs(sx - bx) + abs(sy - by)
        sensor.append((sx, sy, m))

        left_x = sx - m -1
        right_x = sx + m + 1
        top_y = sy - m -1
        bottom_y = sy + m + 1

        lines.append([(left_x, sy), (sx, top_y)])
        lines.append([(left_x, sy), (sx, bottom_y)])
        lines.append([(sx, top_y),(right_x, sy)])
        lines.append([(sx, bottom_y),(right_x, sy)])

    for ls in combinations(lines, 2):
        if p := line_intersection(*ls):
            edges.add(p)

    edges = [(x,y) for x,y in edges if 0 <= x <= size and 0 <= y <= size]

    for x, y in edges:
        for sx, sy, m in sensor:
            if abs(sx - x) + abs(sy - y) < m + 1:
                break
        else:
            return x * 4_000_000 + y

if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    check = r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)'
    data = [[int(g) for g in re.match(check, d).groups()] for d in data]
    print("part 1:", part1(data, 2_000_000))
    print("part 2:", part2(data, 4_000_000))

