from functools import cache

favorite_number = 1364


@cache
def is_wall(x, y):
    s1 = x * x + 3 * x + 2 * x * y + y + y * y
    s2 = s1 + favorite_number
    return bin(s2).count("1") % 2 == 1


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def neighbors(x, y):
    for dx, dy in directions:
        if x + dx >= 0 and y + dy >= 0 and not is_wall(x + dx, y + dy):
            yield (x + dx, y + dy)


def bfs(current, goal):
    step = 0
    visited = set([current])
    positions = set([current])
    in_50 = 0
    while positions:
        step += 1
        next_positions = set()
        for pos in positions:
            for nx, dx in neighbors(*pos):
                if (nx, dx) == goal:
                    return step, in_50
                if (nx, dx) not in visited:
                    visited.add((nx, dx))
                    next_positions.add((nx, dx))
        positions = next_positions
        if step == 50:
            in_50 = len(visited)


start = (1, 1)
goal = (31, 39)

p1, p2 = bfs(start, goal)
print("part 1:", p1)
print("part 1:", p2)
