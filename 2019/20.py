from collections import deque, defaultdict

def parse(filename):
    with open(filename) as f:
        grid = [line.rstrip('\n') for line in f]

    # Pad grid to uniform width
    max_width = max(len(row) for row in grid)
    grid = [row.ljust(max_width) for row in grid]

    height = len(grid)
    width = len(grid[0])

    # Find all portals
    portals = defaultdict(list)

    for y in range(height):
        for x in range(width):
            if grid[y][x].isupper():
                # Check if this is the start of a portal label
                # Horizontal label
                if x + 1 < width and grid[y][x + 1].isupper():
                    label = grid[y][x] + grid[y][x + 1]
                    # Find adjacent passage
                    if x + 2 < width and grid[y][x + 2] == '.':
                        portals[label].append((x + 2, y))
                    elif x - 1 >= 0 and grid[y][x - 1] == '.':
                        portals[label].append((x - 1, y))
                # Vertical label
                if y + 1 < height and grid[y + 1][x].isupper():
                    label = grid[y][x] + grid[y + 1][x]
                    # Find adjacent passage
                    if y + 2 < height and grid[y + 2][x] == '.':
                        portals[label].append((x, y + 2))
                    elif y - 1 >= 0 and grid[y - 1][x] == '.':
                        portals[label].append((x, y - 1))

    # Build portal connections
    portal_map = {}
    for label, positions in portals.items():
        if len(positions) == 2:
            portal_map[positions[0]] = positions[1]
            portal_map[positions[1]] = positions[0]

    # Determine which portals are outer (on edge) vs inner
    # Find the bounds of the actual maze
    min_x = min(x for label, positions in portals.items() for x, y in positions)
    max_x = max(x for label, positions in portals.items() for x, y in positions)
    min_y = min(y for label, positions in portals.items() for x, y in positions)
    max_y = max(y for label, positions in portals.items() for x, y in positions)

    outer = set()
    for pos in portal_map:
        x, y = pos
        if x == min_x or x == max_x or y == min_y or y == max_y:
            outer.add(pos)

    start = portals['AA'][0]
    end = portals['ZZ'][0]

    return grid, portal_map, outer, start, end

def part1(grid, portal_map, start, end):
    height = len(grid)
    width = len(grid[0])

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == end:
            return dist

        # Normal moves
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

        # Portal
        if (x, y) in portal_map:
            dest = portal_map[(x, y)]
            if dest not in visited:
                visited.add(dest)
                queue.append((dest, dist + 1))

    return -1

def part2(grid, portal_map, outer, start, end):
    height = len(grid)
    width = len(grid[0])

    # BFS with state = (x, y, level)
    queue = deque([(start[0], start[1], 0, 0)])  # x, y, level, dist
    visited = {(start[0], start[1], 0)}

    while queue:
        x, y, level, dist = queue.popleft()

        if (x, y) == end and level == 0:
            return dist

        # Normal moves
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '.' and (nx, ny, level) not in visited:
                visited.add((nx, ny, level))
                queue.append((nx, ny, level, dist + 1))

        # Portal
        if (x, y) in portal_map:
            dest = portal_map[(x, y)]
            if (x, y) in outer:
                # Outer portal goes up (level - 1), but can't go above 0
                if level > 0:
                    new_level = level - 1
                    if (dest[0], dest[1], new_level) not in visited:
                        visited.add((dest[0], dest[1], new_level))
                        queue.append((dest[0], dest[1], new_level, dist + 1))
            else:
                # Inner portal goes down (level + 1)
                new_level = level + 1
                if new_level <= 100 and (dest[0], dest[1], new_level) not in visited:  # Limit depth
                    visited.add((dest[0], dest[1], new_level))
                    queue.append((dest[0], dest[1], new_level, dist + 1))

    return -1

if __name__ == '__main__':
    grid, portal_map, outer, start, end = parse('/Users/adamemery/advent-of-code/2019/input20')
    print(f"Part 1: {part1(grid, portal_map, start, end)}")
    print(f"Part 2: {part2(grid, portal_map, outer, start, end)}")
