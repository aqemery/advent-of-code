def parse(filename):
    rules = {}
    with open(filename) as f:
        for line in f:
            left, right = line.strip().split(' => ')
            pattern = tuple(left.split('/'))
            result = tuple(right.split('/'))
            # Add all rotations and flips
            for variant in get_variants(pattern):
                rules[variant] = result
    return rules


def get_variants(pattern):
    """Get all 8 rotations and flips of a pattern."""
    variants = []
    p = pattern
    for _ in range(4):
        variants.append(p)
        variants.append(flip(p))
        p = rotate(p)
    return variants


def rotate(pattern):
    """Rotate 90 degrees clockwise."""
    n = len(pattern)
    return tuple(
        ''.join(pattern[n - 1 - j][i] for j in range(n))
        for i in range(n)
    )


def flip(pattern):
    """Flip horizontally."""
    return tuple(row[::-1] for row in pattern)


def grid_to_blocks(grid, size):
    """Split grid into blocks of given size."""
    n = len(grid)
    blocks = []
    for i in range(0, n, size):
        row_blocks = []
        for j in range(0, n, size):
            block = tuple(grid[i + di][j:j + size] for di in range(size))
            row_blocks.append(block)
        blocks.append(row_blocks)
    return blocks


def blocks_to_grid(blocks):
    """Reassemble blocks into grid."""
    grid = []
    for block_row in blocks:
        block_size = len(block_row[0])
        for i in range(block_size):
            row = ''.join(block[i] for block in block_row)
            grid.append(row)
    return grid


def enhance(grid, rules):
    """Apply one enhancement iteration."""
    n = len(grid)
    if n % 2 == 0:
        size = 2
    else:
        size = 3

    blocks = grid_to_blocks(grid, size)

    # Transform each block
    new_blocks = []
    for block_row in blocks:
        new_row = []
        for block in block_row:
            new_row.append(rules[block])
        new_blocks.append(new_row)

    return blocks_to_grid(new_blocks)


def count_on(grid):
    return sum(row.count('#') for row in grid)


def solve(rules, iterations):
    grid = ['.#.', '..#', '###']

    for _ in range(iterations):
        grid = enhance(grid, rules)

    return count_on(grid)


if __name__ == '__main__':
    rules = parse('2017/input')

    print(f"Part 1: {solve(rules, 5)}")
    print(f"Part 2: {solve(rules, 18)}")
