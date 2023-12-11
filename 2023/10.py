import sys
from collections import deque
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

d = sys.stdin.read().split("\n")
pipes = {}
start = None
for y, l in enumerate(d):
    for x, c in enumerate(l):
        if c == "S":
            start = (x, y)
        pipes[(x, y)] = c


p_types = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
    "S": [(0, -1), (0, 1), (-1, 0), (1, 0)],
}

connectors = {
    (0, -1): "F|7",
    (0, 1): "L|J",
    (-1, 0): "F-L",
    (1, 0): "7-J",
}


def next_pos(pos):
    x, y = pos
    pt = p_types[pipes[(x, y)]]
    for dx, dy in pt:
        delta = (x + dx, y + dy)
        if delta in pipes and pipes[delta] in connectors[(dx, dy)]:
            yield delta


visited = set()
q = deque([(start, [start])])
cycle = None
while q:
    pos, path = q.popleft()
    if pos in visited:
        continue
    visited.add(pos)
    for np in next_pos(pos):
        q.insert(0, (np, path + [np]))
    cycle = path
print("part 1:", len(cycle) // 2)


polygon = Polygon(cycle)
p2 = sum(
    polygon.contains(Point(x, y)) for y, l in enumerate(d) for x, c in enumerate(l)
)
print("part 2:", p2)
