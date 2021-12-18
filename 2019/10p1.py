import itertools
import math

points = {}
y = -1
while True:
    try:
        y += 1
        line = input()
        for x in range(len(line)):
            if line[x] == "#":
                points[(x, y)] = 0
    except EOFError:
        break

slight_lines = list(itertools.combinations(points.keys(), 2))

for sl in slight_lines:
    x1, y1 = sl[0]
    x2, y2 = sl[1]
    dx = x2 - x1
    dy = y2 - y1
    div = math.gcd(dx, dy)
    sx = dx // div
    sy = dy // div
    sight = True
    tmp_x = x1 + sx
    tmp_y = y1 + sy

    while tmp_x != x2 or tmp_y != y2:
        if (tmp_x, tmp_y) in points.keys():
            sight = False
            break
        tmp_x = tmp_x + sx
        tmp_y = tmp_y + sy
    if sight:
        for p in sl:
            points[p] += 1

max_value = 0
max_key = None

for k in points.keys():
    if points[k] > max_value:
        max_value = points[k]
        max_key = k

print(max_value, max_key)
