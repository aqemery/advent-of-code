import sys
from collections import deque

lines = sys.stdin.read().splitlines()
trail_heads = []
map = {}

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == "0":
            trail_heads.append((x, y))
        map[(x, y)] = int(c)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

p1 = 0
p2 = 0
for current in trail_heads:
    trails = 0
    nines = set()

    q = deque([(*current, 0)])
    while q:
        x, y, height = q.popleft()
        if height == 9:
            p2 += 1
            nines.add((x, y))
            continue

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if map.get((new_x, new_y)) == height + 1:
                q.append((new_x, new_y, height + 1))
    p1 += len(nines)

print("p1:", p1)
print("p2:", p2)
