import sys

lines = sys.stdin.read().splitlines()
bounds = (len(lines[0]), len(lines))
walls = set()


def walk(walls):
    player = None
    visited = set()
    loop = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x, y))
            elif c == "^":
                player = (x, y)

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current = 0

    while (
        player[0] >= 0
        and player[0] < bounds[0]
        and player[1] >= 0
        and player[1] < bounds[1]
    ):
        if (current, *player) in loop:
            return False
        loop.add((current, *player))
        visited.add(player)

        nx, ny = player[0] + directions[current][0], player[1] + directions[current][1]
        if (nx, ny) in walls:
            current = (current + 1) % 4
            continue
        player = (nx, ny)

    return len(visited)


print("p1:", walk(walls))

p2 = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ".":
            new_wall = walls.copy()
            new_wall.add((x, y))
            if not walk(new_wall):
                p2 += 1

print("p2:", p2)
