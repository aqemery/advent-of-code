from collections import deque

def parse(filename):
    with open(filename) as f:
        return [tuple(map(int, line.strip().split(','))) for line in f]

def bfs(blocked, size=70):
    start, end = (0, 0), (size, size)
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= size and 0 <= ny <= size and (nx, ny) not in blocked and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))
    return -1

def part1(coords):
    blocked = set(coords[:1024])
    return bfs(blocked)

def part2(coords):
    # Binary search for first blocking byte
    lo, hi = 0, len(coords)
    while lo < hi:
        mid = (lo + hi) // 2
        blocked = set(coords[:mid + 1])
        if bfs(blocked) == -1:
            hi = mid
        else:
            lo = mid + 1
    return f"{coords[lo][0]},{coords[lo][1]}"

if __name__ == '__main__':
    coords = parse('/Users/adamemery/advent-of-code/2024/input18')
    print(f"Part 1: {part1(coords)}")
    print(f"Part 2: {part2(coords)}")
