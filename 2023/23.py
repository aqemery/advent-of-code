from collections import defaultdict

def parse(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def solve(grid, part2=False):
    rows, cols = len(grid), len(grid[0])
    start = (0, grid[0].index('.'))
    end = (rows - 1, grid[rows - 1].index('.'))

    # Build graph of junctions
    junctions = {start, end}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                continue
            neighbors = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                    neighbors += 1
            if neighbors > 2:
                junctions.add((r, c))

    # Build adjacency with distances
    def get_neighbors(r, c):
        if part2:
            return [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cell = grid[r][c]
        if cell == '^':
            return [(-1, 0)]
        elif cell == 'v':
            return [(1, 0)]
        elif cell == '<':
            return [(0, -1)]
        elif cell == '>':
            return [(0, 1)]
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]

    graph = defaultdict(dict)
    for jr, jc in junctions:
        stack = [(jr, jc, 0)]
        visited = {(jr, jc)}
        while stack:
            r, c, dist = stack.pop()
            if dist > 0 and (r, c) in junctions:
                graph[(jr, jc)][(r, c)] = dist
                continue
            for dr, dc in get_neighbors(r, c):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append((nr, nc, dist + 1))

    # DFS for longest path
    def dfs(node, visited):
        if node == end:
            return 0
        max_dist = float('-inf')
        visited.add(node)
        for next_node, dist in graph[node].items():
            if next_node not in visited:
                result = dfs(next_node, visited)
                if result != float('-inf'):
                    max_dist = max(max_dist, dist + result)
        visited.remove(node)
        return max_dist

    return dfs(start, set())

if __name__ == '__main__':
    grid = parse('/Users/adamemery/advent-of-code/2023/input23')
    print(f"Part 1: {solve(grid, part2=False)}")
    print(f"Part 2: {solve(grid, part2=True)}")
