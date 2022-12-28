import sys
from collections import deque


def cubeWrap(x, y, direction):
    match direction:
        case 0:  # right
            if y <= 50:
                return 100, 151 - y, 2
            elif y <= 100:
                return y + 50, 50, -1
            elif y <= 150:
                return 150, 151 - y, 2
            elif y <= 200:
                return y - 100, 150, -1
        case 1:  # down
            if x <= 50:
                return x + 100, 1, 0
            elif x <= 100:
                return 50, x + 100, 1
            elif x <= 150:
                return 100, x - 50, 1
        case 2:  # left
            if y <= 50:
                return 1, 151 - y, 2
            elif y <= 100:
                return y - 50, 101, -1
            elif y <= 150:
                return 51, 151 - y, 2
            elif y <= 200:
                return y - 100, 1, -1

        case 3:  # up
            if x <= 50:
                return 51, x + 50, 1
            elif x <= 100:
                return 1, x + 100, 1
            elif x <= 150:
                return x - 100, 200, 0


def solve(walls, floor, directions, is_cube=False):
    facing = deque([(1, 0, 0), (0, -1, 3), (-1, 0, 2), (0, 1, 1)])
    cx, cy = min([p for p in floor if p[1] == 1])

    current_path = 0
    for d in directions:
        if d == "L":
            facing.rotate(-1)
        elif d == "R":
            facing.rotate(1)
        elif type(d) == int:
            for _ in range(d):
                x, y, s = facing[0]
                next_pos = (cx + x, cy + y)
                if next_pos in walls:
                    break
                elif next_pos in floor:
                    cx, cy = next_pos
                elif is_cube:
                    nx, ny, r = cubeWrap(cx, cy, s)
                    if (nx, ny) in walls:
                        break
                    cx, cy = nx, ny
                    facing.rotate(r)
                else:
                    nx, ny = cx, cy
                    while (nx, ny) in floor or (nx, ny) in walls:
                        nx -= x
                        ny -= y

                    next_pos = (nx + x, ny + y)
                    if next_pos in walls:
                        break
                    cx, cy = next_pos
            current_path += 1
    return 1000 * cy + 4 * cx + facing[0][2]


if __name__ == "__main__":
    board, data = sys.stdin.read().split("\n\n")

    walls = set()
    floor = set()

    for y, line in enumerate(board.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x + 1, y + 1))
            elif c == ".":
                floor.add((x + 1, y + 1))

    directions = []
    next = []
    for c in data:
        if c in ["L", "R"]:
            directions.append(int("".join(next)))
            directions.append(c)
            next = []
        else:
            next.append(c)

    directions.append(int("".join(next)))

    print("part 1:", solve(walls, floor, directions))
    print("part 2:", solve(walls, floor, directions, True))
