def parse_input(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f if line.strip()]

def count_adjacent(grid, x, y):
    trees = 0
    lumberyards = 0
    height = len(grid)
    width = len(grid[0])

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] == '|':
                    trees += 1
                elif grid[ny][nx] == '#':
                    lumberyards += 1

    return trees, lumberyards

def step(grid):
    height = len(grid)
    width = len(grid[0])
    new_grid = [row[:] for row in grid]

    for y in range(height):
        for x in range(width):
            trees, lumberyards = count_adjacent(grid, x, y)
            cell = grid[y][x]

            if cell == '.':
                # Open becomes trees if 3+ adjacent trees
                if trees >= 3:
                    new_grid[y][x] = '|'
            elif cell == '|':
                # Trees become lumberyard if 3+ adjacent lumberyards
                if lumberyards >= 3:
                    new_grid[y][x] = '#'
            elif cell == '#':
                # Lumberyard stays if 1+ adjacent lumberyard and 1+ adjacent trees
                if lumberyards >= 1 and trees >= 1:
                    new_grid[y][x] = '#'
                else:
                    new_grid[y][x] = '.'

    return new_grid

def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)

def count_resources(grid):
    trees = sum(row.count('|') for row in grid)
    lumberyards = sum(row.count('#') for row in grid)
    return trees * lumberyards

def part1(grid):
    grid = [row[:] for row in grid]
    for _ in range(10):
        grid = step(grid)
    return count_resources(grid)

def part2(grid):
    grid = [row[:] for row in grid]
    seen = {}
    target = 1000000000

    minute = 0
    while minute < target:
        state = grid_to_tuple(grid)
        if state in seen:
            cycle_start = seen[state]
            cycle_length = minute - cycle_start
            # Fast forward
            remaining = (target - minute) % cycle_length
            for _ in range(remaining):
                grid = step(grid)
            return count_resources(grid)

        seen[state] = minute
        grid = step(grid)
        minute += 1

    return count_resources(grid)

if __name__ == '__main__':
    grid = parse_input('/Users/adamemery/advent-of-code/2018/input18')
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
