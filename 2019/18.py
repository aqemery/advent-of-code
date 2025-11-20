#!/usr/bin/env python3
"""
Advent of Code 2019 - Day 18: Many-Worlds Interpretation
"""

from collections import deque
import heapq

def parse_input(filename):
    with open(filename) as f:
        return [list(line.rstrip('\n')) for line in f]

def find_points_of_interest(grid):
    """Find all keys, doors, and starting positions."""
    points = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@' or cell.islower():
                points[cell] = (x, y)
            elif cell.isupper():
                points[cell] = (x, y)
    return points

def bfs_from_point(grid, start_pos):
    """
    BFS from a starting position to find all reachable keys.
    Returns dict: key -> (distance, doors_needed)
    doors_needed is a bitmask of which doors are blocking the path.
    """
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([(start_pos[0], start_pos[1], 0, 0)])  # x, y, dist, doors
    visited = {(start_pos[0], start_pos[1]): 0}
    results = {}

    while queue:
        x, y, dist, doors = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < cols and 0 <= ny < rows:
                cell = grid[ny][nx]

                if cell == '#':
                    continue

                if (nx, ny) in visited:
                    continue

                visited[(nx, ny)] = dist + 1
                new_doors = doors

                # If it's a door, add to required doors
                if cell.isupper():
                    new_doors = doors | (1 << (ord(cell) - ord('A')))

                # If it's a key, record it
                if cell.islower():
                    results[cell] = (dist + 1, new_doors)

                queue.append((nx, ny, dist + 1, new_doors))

    return results

def build_graph(grid, starts):
    """
    Build a graph of distances between all keys and starting positions.
    Returns: dict mapping (source) -> dict of (target) -> (distance, doors_needed)
    """
    graph = {}

    # Find all keys
    keys = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.islower():
                keys[cell] = (x, y)

    # BFS from each starting position
    for i, start in enumerate(starts):
        graph[('@', i)] = bfs_from_point(grid, start)

    # BFS from each key
    for key, pos in keys.items():
        graph[key] = bfs_from_point(grid, pos)

    return graph, keys

def solve_part1(grid):
    """
    Solve part 1 using Dijkstra's algorithm.
    State: (current_position, keys_collected_bitmask)
    """
    # Find starting position
    start = None
    keys = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                start = (x, y)
            elif cell.islower():
                keys[cell] = (x, y)

    if not keys:
        return 0

    # Build graph
    graph, _ = build_graph(grid, [start])

    # Map keys to bit positions - use ord(key) - ord('a') for consistency with doors
    # doors_needed uses bit positions 0-25 for A-Z, so we use same for a-z
    key_to_bit = lambda k: ord(k) - ord('a')

    # Calculate all_keys_mask based on actual keys present
    all_keys_mask = 0
    for k in keys:
        all_keys_mask |= (1 << key_to_bit(k))

    # Dijkstra's algorithm
    # State: (distance, keys_collected_mask, current_key_or_start)
    # Using collected before pos to avoid comparison issues
    start_state = (0, 0, ('@', 0))
    heap = [start_state]
    visited = {}

    while heap:
        dist, collected, pos = heapq.heappop(heap)

        if collected == all_keys_mask:
            return dist

        state = (pos, collected)
        if state in visited:
            continue
        visited[state] = dist

        # Get neighbors from graph
        if pos in graph:
            neighbors = graph[pos]
        else:
            continue

        for next_key, (step_dist, doors_needed) in neighbors.items():
            # Check if we have all required keys for doors
            # doors_needed is a bitmask of door letters (A=0, B=1, etc.)
            # We need to check if we have those keys (a=0, b=1, etc.)
            if (doors_needed & collected) != doors_needed:
                continue

            # Collect the new key
            key_bit = key_to_bit(next_key)
            new_collected = collected | (1 << key_bit)
            new_dist = dist + step_dist

            new_state = (next_key, new_collected)
            if new_state not in visited:
                heapq.heappush(heap, (new_dist, new_collected, next_key))

    return -1  # No solution found

def solve_part2(grid):
    """
    Solve part 2 with 4 robots.
    Modify the grid first, then use Dijkstra with state = (4 positions, keys_collected)
    """
    # Find the original starting position
    start_x, start_y = None, None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                start_x, start_y = x, y
                break
        if start_x is not None:
            break

    # Modify the grid for part 2
    # Replace center 3x3 with walls and 4 new starts
    grid[start_y][start_x] = '#'
    grid[start_y - 1][start_x] = '#'
    grid[start_y + 1][start_x] = '#'
    grid[start_y][start_x - 1] = '#'
    grid[start_y][start_x + 1] = '#'
    grid[start_y - 1][start_x - 1] = '@'
    grid[start_y - 1][start_x + 1] = '@'
    grid[start_y + 1][start_x - 1] = '@'
    grid[start_y + 1][start_x + 1] = '@'

    # Find the 4 starting positions
    starts = [
        (start_x - 1, start_y - 1),
        (start_x + 1, start_y - 1),
        (start_x - 1, start_y + 1),
        (start_x + 1, start_y + 1)
    ]

    # Find all keys and which quadrant they're in
    keys = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.islower():
                keys[cell] = (x, y)

    if not keys:
        return 0

    # Map keys to bit positions - use ord(key) - ord('a') for consistency with doors
    key_to_bit = lambda k: ord(k) - ord('a')

    # Calculate all_keys_mask based on actual keys present
    all_keys_mask = 0
    for k in keys:
        all_keys_mask |= (1 << key_to_bit(k))

    # Build graphs from each starting position and each key
    graphs = [{} for _ in range(4)]

    # BFS from each starting position
    for i, start in enumerate(starts):
        graphs[i][('@', i)] = bfs_from_point(grid, start)

    # BFS from each key and determine which robot can reach it
    key_to_robot = {}
    for key, pos in keys.items():
        # Determine which robot can reach this key
        for i, start in enumerate(starts):
            reachable = bfs_from_point(grid, start)
            if key in reachable:
                key_to_robot[key] = i
                break

        # BFS from this key
        reachable_keys = bfs_from_point(grid, pos)
        graphs[key_to_robot[key]][key] = reachable_keys

    # Dijkstra's algorithm
    # State: (distance, keys_collected_mask, (pos0, pos1, pos2, pos3))
    initial_positions = tuple([('@', i) for i in range(4)])
    start_state = (0, 0, initial_positions)
    heap = [start_state]
    visited = {}

    while heap:
        dist, collected, positions = heapq.heappop(heap)

        if collected == all_keys_mask:
            return dist

        state = (positions, collected)
        if state in visited:
            continue
        visited[state] = dist

        # Try moving each robot
        for robot_idx in range(4):
            pos = positions[robot_idx]

            if pos not in graphs[robot_idx]:
                continue

            neighbors = graphs[robot_idx][pos]

            for next_key, (step_dist, doors_needed) in neighbors.items():
                # Check if we have all required keys for doors
                if (doors_needed & collected) != doors_needed:
                    continue

                # Check if we already have this key
                key_bit = key_to_bit(next_key)
                if collected & (1 << key_bit):
                    continue

                # Collect the new key
                new_collected = collected | (1 << key_bit)
                new_dist = dist + step_dist

                # Update positions
                new_positions = list(positions)
                new_positions[robot_idx] = next_key
                new_positions = tuple(new_positions)

                new_state = (new_positions, new_collected)
                if new_state not in visited:
                    heapq.heappush(heap, (new_dist, new_collected, new_positions))

    return -1  # No solution found

def main():
    grid = parse_input('/Users/adamemery/advent-of-code/2019/input18')

    # Make a copy for part 2
    grid_copy = [row[:] for row in grid]

    part1 = solve_part1(grid)
    part2 = solve_part2(grid_copy)

    print(f"Day 18: Part 1 = {part1}, Part 2 = {part2}")

if __name__ == "__main__":
    main()
