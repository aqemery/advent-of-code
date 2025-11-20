def parse(filename):
    with open(filename) as f:
        parts = f.read().split('\n\n')
    grid = [list(line) for line in parts[0].split('\n')]
    moves = parts[1].replace('\n', '')
    return grid, moves

def find_robot(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                return r, c

def part1(grid, moves):
    grid = [row[:] for row in grid]
    r, c = find_robot(grid)
    dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    for move in moves:
        dr, dc = dirs[move]
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == '#':
            continue
        elif grid[nr][nc] == '.':
            grid[r][c], grid[nr][nc] = '.', '@'
            r, c = nr, nc
        elif grid[nr][nc] == 'O':
            er, ec = nr, nc
            while grid[er][ec] == 'O':
                er, ec = er + dr, ec + dc
            if grid[er][ec] == '.':
                grid[er][ec], grid[nr][nc], grid[r][c] = 'O', '@', '.'
                r, c = nr, nc

    return sum(100 * r + c for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == 'O')

def part2(grid, moves):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == '#': new_row.extend(['#', '#'])
            elif cell == 'O': new_row.extend(['[', ']'])
            elif cell == '.': new_row.extend(['.', '.'])
            elif cell == '@': new_row.extend(['@', '.'])
        new_grid.append(new_row)
    grid = new_grid
    r, c = find_robot(grid)
    dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    for move in moves:
        dr, dc = dirs[move]
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == '#':
            continue
        elif grid[nr][nc] == '.':
            grid[r][c], grid[nr][nc] = '.', '@'
            r, c = nr, nc
        elif grid[nr][nc] in '[]':
            if dc != 0:
                ec = nc
                while grid[nr][ec] in '[]':
                    ec += dc
                if grid[nr][ec] == '.':
                    while ec != nc:
                        grid[nr][ec] = grid[nr][ec - dc]
                        ec -= dc
                    grid[nr][nc], grid[r][c] = '@', '.'
                    r, c = nr, nc
            else:
                to_move = []
                frontier = [(nr, nc)]
                if grid[nr][nc] == '[': frontier.append((nr, nc + 1))
                else: frontier.append((nr, nc - 1))
                can_move, seen = True, set()
                while frontier and can_move:
                    cr, cc = frontier.pop(0)
                    if (cr, cc) in seen: continue
                    seen.add((cr, cc))
                    if grid[cr][cc] == '#': can_move = False
                    elif grid[cr][cc] in '[]':
                        to_move.append((cr, cc))
                        nextr = cr + dr
                        frontier.append((nextr, cc))
                        if grid[nextr][cc] == '[': frontier.append((nextr, cc + 1))
                        elif grid[nextr][cc] == ']': frontier.append((nextr, cc - 1))
                if can_move:
                    to_move.sort(key=lambda x: -x[0] if dr > 0 else x[0])
                    for br, bc in to_move:
                        grid[br + dr][bc], grid[br][bc] = grid[br][bc], '.'
                    grid[r][c], grid[nr][nc] = '.', '@'
                    r, c = nr, nc

    return sum(100 * r + c for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == '[')

if __name__ == '__main__':
    grid, moves = parse('/Users/adamemery/advent-of-code/2024/input15')
    print(f"Part 1: {part1(grid, moves)}")
    print(f"Part 2: {part2(grid, moves)}")
