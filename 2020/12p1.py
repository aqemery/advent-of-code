import sys
import math

ship = [0, 0]
ship_direction = 0
keys = ["E", "N", "W", "S"]
values = [math.radians(i * 90) for i in range(4)]
directions = dict(zip(keys, values))
quarter = math.pi / 4


def move(direct, amount):
    x = ship[0] + math.sin(direct) * amount
    y = ship[1] + math.cos(direct) * amount
    return [x, y]


for l in sys.stdin.readlines():
    d = l[:1]
    v = int(l[1:])
    if d in directions:
        ship = move(directions[d], v)
    elif d == "L":
        ship_direction += math.radians(v)
    elif d == "R":
        ship_direction -= math.radians(v)
    elif d == "F":
        ship = move(ship_direction, v)

print(int(abs(ship[0]) + abs(ship[1])))
