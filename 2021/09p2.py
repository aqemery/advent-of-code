import sys
import math
from collections import deque

lines = sys.stdin.read().split("\n")
grid = {(x, y): int(v) for y, row in enumerate(lines) for x, v in enumerate(row)}
around = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = set([k for k, v in grid.items() if v == 9])

basins = []
for k in grid.keys():
    before = len(visited)
    q = deque([k])
    while q:
        pos = q.popleft()
        if not pos in visited:
            checks = [tuple(sum(z) for z in zip(pos, a)) for a in around]
            q.extend([c for c in checks if grid.get(c) != None])
            visited.add(pos)
    basins.append(len(visited) - before)

basins.sort()
print(math.prod(basins[-3:]))
