import sys

map, instuctions = sys.stdin.read().split("\n\n")
map = map.split("\n")

instuctions = instuctions.replace("\n", "")
directions = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
walls = set()
rocks = set()
robot = None

for y, l in enumerate(map):
    for x, c in enumerate(l):
        if c == "#":
            walls.add((x, y))
        elif c == "@":
            robot = (x, y)
        elif c == "O":
            rocks.add((x, y))

for instuct in instuctions:
    next_rocks = rocks.copy()
    dx, dy = directions[instuct]
    new_pos = robot[0] + dx, robot[1] + dy
    if new_pos in walls:
        continue
    if new_pos in rocks:
        current_rock = new_pos
        next_rocks.remove(current_rock)
        while current_rock in rocks:
            current_rock = current_rock[0] + dx, current_rock[1] + dy
        if current_rock in walls:
            continue
        next_rocks.add(current_rock)
        rocks = next_rocks
        robot = new_pos
    else:
        robot = new_pos

print("p1:", sum(ry * 100 + rx for rx, ry in rocks))
