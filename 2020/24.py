def parse(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def get_coords(path):
    # Hexagonal grid using cube coordinates (x, y)
    # e/w = +/-1 on x, ne/nw and se/sw move diagonally
    x, y = 0, 0
    i = 0
    while i < len(path):
        if path[i] == 'e':
            x += 1
            i += 1
        elif path[i] == 'w':
            x -= 1
            i += 1
        elif path[i:i+2] == 'ne':
            x += 1
            y += 1
            i += 2
        elif path[i:i+2] == 'nw':
            y += 1
            i += 2
        elif path[i:i+2] == 'se':
            y -= 1
            i += 2
        elif path[i:i+2] == 'sw':
            x -= 1
            y -= 1
            i += 2
    return (x, y)

def part1(paths):
    black = set()
    for path in paths:
        coord = get_coords(path)
        if coord in black:
            black.remove(coord)
        else:
            black.add(coord)
    return black

def neighbors(x, y):
    return [
        (x+1, y), (x-1, y),      # e, w
        (x+1, y+1), (x, y+1),    # ne, nw
        (x, y-1), (x-1, y-1)     # se, sw
    ]

def part2(black):
    for _ in range(100):
        # Count black neighbors for all relevant tiles
        neighbor_count = {}
        for (x, y) in black:
            for nx, ny in neighbors(x, y):
                neighbor_count[(nx, ny)] = neighbor_count.get((nx, ny), 0) + 1

        new_black = set()

        # Check all black tiles
        for tile in black:
            count = neighbor_count.get(tile, 0)
            if count == 1 or count == 2:
                new_black.add(tile)

        # Check all white tiles with black neighbors
        for tile, count in neighbor_count.items():
            if tile not in black and count == 2:
                new_black.add(tile)

        black = new_black

    return len(black)

if __name__ == '__main__':
    paths = parse('/Users/adamemery/advent-of-code/2020/input24')
    black = part1(paths)
    print(f"Part 1: {len(black)}")
    print(f"Part 2: {part2(black)}")
