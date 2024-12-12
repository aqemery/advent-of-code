import sys
from collections import deque

lines = sys.stdin.read().splitlines()
map = {}
visited = set()

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        map[(x, y)] = c

directions = [(0, 1, 1), (1, 0, 2), (0, -1, 3), (-1, 0, 4)]


def flood_fill(x, y):
    fences = []
    loc = 1
    q = deque([(x, y)])
    value = map[(x, y)]
    visited.add((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy, dval in directions:
            new_x, new_y = x + dx, y + dy
            if map.get((new_x, new_y)) == value:
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y))
                    loc += 1
            else:
                fences.append((new_x, new_y, dval))

    visited_fence = set()
    sides = 0

    for fx, fy, fdval in fences:
        if (fx, fy, fdval) in visited_fence:
            continue
        sides += 1
        q = deque([(fx, fy, fdval)])
        while q:
            x, y, dval = q.popleft()
            visited_fence.add((x, y, dval))
            for dx, dy, _ in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y, dval) in fences:
                    if (new_x, new_y, dval) not in visited_fence:
                        visited_fence.add((new_x, new_y, dval))
                        q.append((new_x, new_y, dval))

    return loc, len(fences), sides


p1 = 0
p2 = 0
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if (x, y) not in visited:
            l, f, s = flood_fill(x, y)
            p1 += l * f
            p2 += l * s
print("p1:", p1)
print("p2:", p2)
