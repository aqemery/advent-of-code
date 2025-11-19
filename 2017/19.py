def solve(filename):
    with open(filename) as f:
        # Don't strip - we need to preserve spaces for the grid
        grid = [line.rstrip('\n') for line in f.readlines()]

    # Pad all rows to the same length
    max_len = max(len(row) for row in grid)
    grid = [row.ljust(max_len) for row in grid]

    # Find starting position (the | in the first row)
    x = grid[0].index('|')
    y = 0

    # Direction: down initially
    dx, dy = 0, 1

    letters = []
    steps = 0

    while True:
        # Move to next position
        x += dx
        y += dy
        steps += 1

        # Check bounds
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
            break

        char = grid[y][x]

        if char == ' ':
            # End of path
            break
        elif char == '+':
            # Turn - find the new direction (perpendicular to current)
            if dx == 0:  # Moving vertically, need to turn horizontal
                if x > 0 and grid[y][x-1] != ' ':
                    dx, dy = -1, 0
                else:
                    dx, dy = 1, 0
            else:  # Moving horizontally, need to turn vertical
                if y > 0 and grid[y-1][x] != ' ':
                    dx, dy = 0, -1
                else:
                    dx, dy = 0, 1
        elif char.isalpha():
            letters.append(char)
        # For | and - we just continue in same direction

    return ''.join(letters), steps


if __name__ == '__main__':
    # Test with example
    example = """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
"""

    # Write example to temp file for testing
    with open('/tmp/day19_example.txt', 'w') as f:
        f.write(example)

    letters, steps = solve('/tmp/day19_example.txt')
    print(f"Example - Part 1: {letters} (expected: ABCDEF)")
    print(f"Example - Part 2: {steps} (expected: 38)")

    # Solve actual input
    letters, steps = solve('2017/input')
    print(f"\nPart 1: {letters}")
    print(f"Part 2: {steps}")
