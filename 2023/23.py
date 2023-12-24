import sys
from heapq import heappush, heappop


def solve(grid, start, end, slippery=True):
    q = [(0, start, set())]
    paths = []
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
                print(max_dist)
            continue
        visited.add(pos)
        next_dirs = dirs
        if slippery and grid[pos] in slopes:
            next_dirs = [dirs[slopes.index(grid[pos])]]
        for dx, dy in next_dirs:
            next_pos = (pos[0] + dx, pos[1] + dy)
            if next_pos in grid:
                heappush(q, ((dist + 1) * -1, next_pos, visited))
    return max_dist


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    grid = {
        (x, y): c for y, line in enumerate(d) for x, c in enumerate(line) if c != "#"
    }
    start = min(grid, key=lambda p: p[1])
    end = max(grid, key=lambda p: p[1])
    print("part 1:", solve(grid, start, end))
    print("part 2:", solve(grid, start, end, slippery=False))
