from collections import deque

def parse(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def find_path(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S': start = (r, c)
            if grid[r][c] == 'E': end = (r, c)

    # BFS to find distances from start
    dist = {start: 0}
    queue = deque([start])
    path = [start]

    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            break
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))
                path.append((nr, nc))

    return path, dist

def count_cheats(path, dist, max_cheat, min_save=100):
    count = 0
    for i, (r1, c1) in enumerate(path):
        for j in range(i + min_save, len(path)):
            r2, c2 = path[j]
            cheat_dist = abs(r1 - r2) + abs(c1 - c2)
            if cheat_dist <= max_cheat:
                saved = dist[(r2, c2)] - dist[(r1, c1)] - cheat_dist
                if saved >= min_save:
                    count += 1
    return count

if __name__ == '__main__':
    grid = parse('/Users/adamemery/advent-of-code/2024/input20')
    path, dist = find_path(grid)
    print(f"Part 1: {count_cheats(path, dist, 2)}")
    print(f"Part 2: {count_cheats(path, dist, 20)}")
