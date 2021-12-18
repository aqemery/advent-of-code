import itertools
import math

width = 0
height = -1
points = []
while True:
    try:
        height += 1
        line = input()
        width = len(line)
        for x in range(width):
            if line[x] == "#":
                points.append((x, height))
    except EOFError:
        break

station = (19, 14)
points.remove(station)

targets = {}
for p in points:
    dx = p[0] - station[0]
    dy = p[1] - station[1]
    dist = math.hypot(dx, dy)
    angle = math.atan2(dx, dy)

    if not angle in targets:
        targets[angle] = []
    targets[angle].append((p, dist))

sk = list(targets.keys())
sk.sort(reverse=True)

index = 0
count = 0
last_destroyed = None
while count < 200:
    if index >= len(sk):
        index = 0

    angle_targets = targets[sk[index]]
    least_at = angle_targets[0]
    for at in angle_targets[1:]:
        if at[1] < least_at[1]:
            least_at = at
    last_destroyed = least_at
    angle_targets.remove(least_at)
    count += 1
    if len(angle_targets) == 0:
        del targets[sk[index]]
        del sk[index]
    else:
        index += 1

ldp = last_destroyed[0]
print(ldp[0] * 100 + ldp[1])
