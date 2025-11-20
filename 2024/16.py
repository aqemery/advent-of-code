import heapq
from collections import defaultdict

def parse(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S': start = (r, c)
            if grid[r][c] == 'E': end = (r, c)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # E, S, W, N
    pq = [(0, start[0], start[1], 0, [(start[0], start[1])])]  # cost, r, c, dir, path
    best = defaultdict(lambda: float('inf'))
    best_cost = float('inf')
    best_tiles = set()

    while pq:
        cost, r, c, d, path = heapq.heappop(pq)
        if cost > best[(r, c, d)]:
            continue
        best[(r, c, d)] = cost

        if (r, c) == end:
            if cost < best_cost:
                best_cost = cost
                best_tiles = set(path)
            elif cost == best_cost:
                best_tiles.update(path)
            continue

        # Move forward
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if grid[nr][nc] != '#':
            new_cost = cost + 1
            if new_cost <= best[(nr, nc, d)]:
                heapq.heappush(pq, (new_cost, nr, nc, d, path + [(nr, nc)]))

        # Turn left/right
        for nd in [(d - 1) % 4, (d + 1) % 4]:
            new_cost = cost + 1000
            if new_cost <= best[(r, c, nd)]:
                heapq.heappush(pq, (new_cost, r, c, nd, path))

    return best_cost, len(best_tiles)

if __name__ == '__main__':
    grid = parse('/Users/adamemery/advent-of-code/2024/input16')
    p1, p2 = solve(grid)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
