def man_dist(a):
    return a[0] + a[1]


def parse(dir):
    return dir[0], int(dir[1:])


def get_points(wire):
    pos = [0, 0]
    points = []
    for l in wire:
        if l[0] == "U":
            points += [(pos[0], pos[1] + y) for y in range(1, l[1] + 1)]
            pos[1] += l[1]
        elif l[0] == "D":
            points += [(pos[0], pos[1] - y) for y in range(1, l[1] + 1)]
            pos[1] -= l[1]
        elif l[0] == "L":
            points += [(pos[0] - x, pos[1]) for x in range(1, l[1] + 1)]
            pos[0] -= l[1]
        elif l[0] == "R":
            points += [(pos[0] + x, pos[1]) for x in range(1, l[1] + 1)]
            pos[0] += l[1]
    return points


w1 = list(map(parse, input().split(",")))
w2 = list(map(parse, input().split(",")))

w1_points = set(get_points(w1))
w2_points = set(get_points(w2))

cross = list(w1_points.intersection(w2_points))
dist = man_dist(cross[0])
for p in cross:
    d = man_dist(p)
    if d < dist:
        dist = d
print(dist)
