from collections import deque

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()

def build_map(regex):
    """Build a map of rooms from the regex, returning distances from start."""
    # Directions
    dirs = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}

    # Map of positions to set of adjacent positions (doors)
    doors = {}  # (x, y) -> set of (nx, ny)

    # Current positions and stack for branches
    positions = {(0, 0)}  # Start position
    stack = []  # Stack of (positions at branch start, positions at ends of previous options)

    for char in regex:
        if char == '^' or char == '$':
            continue
        elif char == '(':
            # Start of group - save current positions
            stack.append((positions, set()))
        elif char == '|':
            # End of option - save current positions as ends, restore to branch start
            start_positions, end_positions = stack[-1]
            end_positions.update(positions)
            stack[-1] = (start_positions, end_positions)
            positions = start_positions.copy()
        elif char == ')':
            # End of group - merge all end positions
            start_positions, end_positions = stack.pop()
            positions.update(end_positions)
        else:
            # Direction - move all current positions
            dx, dy = dirs[char]
            new_positions = set()
            for x, y in positions:
                nx, ny = x + dx, y + dy
                # Add door between (x, y) and (nx, ny)
                if (x, y) not in doors:
                    doors[(x, y)] = set()
                if (nx, ny) not in doors:
                    doors[(nx, ny)] = set()
                doors[(x, y)].add((nx, ny))
                doors[(nx, ny)].add((x, y))
                new_positions.add((nx, ny))
            positions = new_positions

    # BFS to find distances from start
    distances = {(0, 0): 0}
    queue = deque([(0, 0)])

    while queue:
        pos = queue.popleft()
        if pos not in doors:
            continue
        for neighbor in doors[pos]:
            if neighbor not in distances:
                distances[neighbor] = distances[pos] + 1
                queue.append(neighbor)

    return distances

def solve(regex):
    distances = build_map(regex)

    # Part 1: Maximum distance
    part1 = max(distances.values())

    # Part 2: Rooms with distance >= 1000
    part2 = sum(1 for d in distances.values() if d >= 1000)

    return part1, part2

if __name__ == '__main__':
    regex = parse_input('/Users/adamemery/advent-of-code/2018/input20')
    part1, part2 = solve(regex)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
