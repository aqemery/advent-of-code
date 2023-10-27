import sys
from collections import deque
from itertools import permutations
from math import inf

def solve(data, p2=False):
    nodes = {}
    floor = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c.isdigit():
                nodes[(x, y)] = int(c)
                floor.add((x, y))
            if c == ".":
                floor.add((x, y))


    paths = {}

    for key, node in nodes.items():
        bfs = deque([(0,*key)])
        visited = set([key])
        while bfs:
            steps, x, y = bfs.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in floor and (nx, ny) not in visited:
                    bfs.append((steps + 1, nx, ny))
                    if (nx, ny) in nodes:
                        found = nodes[(nx, ny)]
                        first = min(node, found)
                        second = max(node, found)
                        paths[(first, second)] = steps + 1
                    visited.add((nx, ny))


    not_0 = [v for v in nodes.values() if v != 0]

    min_steps = inf
    for p in permutations(not_0):
        current = 0
        steps = 0
        for n in p:
            first = min(current, n)
            second = max(current, n)
            steps += paths[(first, second)]
            current = n

        if p2:
            steps += paths[(0, current)]
        
        if steps < min_steps:
            min_steps = steps
        

    return min_steps

if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, p2=True))
