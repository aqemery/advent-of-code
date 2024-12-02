import sys
from heapq import heappush, heappop
import sys
from collections import deque
from itertools import permutations


def part1(grid, start, end):
    q = [(0, start, set())]
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    slopes = "^v<>"
    max_dist = 0
    while q:
        dist, pos, visited = heappop(q)
        dist *= -1
        visited = set(visited)
        if pos in visited:
            continue
        if pos == end:
            if dist > max_dist:
                max_dist = dist
            continue
        visited.add(pos)
        next_dirs = dirs
        if grid[pos] in slopes:
            next_dirs = [dirs[slopes.index(grid[pos])]]
        for dx, dy in next_dirs:
            next_pos = (pos[0] + dx, pos[1] + dy)
            if next_pos in grid:
                heappush(q, ((dist + 1) * -1, next_pos, visited))
    return max_dist


def next_pos(grid, pos, visited):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    x, y = pos
    return [
        (x + dx, y + dy)
        for dx, dy in dirs
        if (x + dx, y + dy) in grid and (x + dx, y + dy) not in visited
    ]


def get_junctions(grid, start):
    q = deque([(start)])
    junctions = []
    visited = set([start])
    while q:
        pos = q.popleft()
        nps = next_pos(grid, pos, visited)
        if len(nps) > 1:
            junctions.append(pos)
        for np in nps:
            q.append(np)
            visited.add(np)
    return junctions


def shortest_paths(grid, junctions):
    paths = []
    for j1, j2 in permutations(junctions, 2):
        print(j1, j2)
        q = deque([(0, j1)])
        visited = set([j1])
        while q:
            dist, pos = q.popleft()
            if pos in junctions and pos != j1 and pos != j2:
                break
            if pos == j2:
                paths.append((dist, j1, j2))
                break
            nps = next_pos(grid, pos, visited)
            for np in nps:
                q.append((dist + 1, np))
                visited.add(np)
    return paths


def part2(grid, start, end):
    junctions = get_junctions(grid, start)
    junctions.append(end)
    junctions.insert(0, start)
    

    # print(junctions)

    paths = shortest_paths(grid, junctions)

    # for dist, j1, j2 in paths:
    #     print(dist, j1, j2)
    # max distance using dir_graph start to end
    q = deque([(0, start, set())])
    max_dist = 0

    # while q:
    #     print(q)
    #     dist, pos, visited = q.popleft()
    #     if pos in visited:
    #         continue
    #     if pos == end:
    #         if dist > max_dist:
    #             max_dist = dist
    #         continue
    #     visited.add(pos)
    #     for p in paths:
    #         if p[1] == pos:
    #             q.append((dist + p[0], p[2], visited.copy()))
    #         elif p[2] == pos:
    #             q.append((dist + p[0], p[1], visited.copy()))
    # return max_dist


        # if pos == end:
        #     if dist > max_dist:
        #         max_dist = dist
        #     continue

        # for np in nps:
        #     q.append((dist + 1, np))
        #     visited.add(np)




    

    print(paths)



if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    grid = {
        (x, y): c for y, line in enumerate(d) for x, c in enumerate(line) if c != "#"
    }
    start = min(grid, key=lambda p: p[1])
    end = max(grid, key=lambda p: p[1])
    print("part 1:", part1(grid, start, end))
    print("part 2:", part2(grid, start, end))
