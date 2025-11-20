import math
from collections import defaultdict

def parse(filename):
    with open(filename) as f:
        blocks = f.read().strip().split('\n\n')

    tiles = {}
    for block in blocks:
        lines = block.split('\n')
        tile_id = int(lines[0].split()[1][:-1])
        grid = [list(line) for line in lines[1:]]
        tiles[tile_id] = grid
    return tiles

def get_edges(tile):
    top = ''.join(tile[0])
    bottom = ''.join(tile[-1])
    left = ''.join(row[0] for row in tile)
    right = ''.join(row[-1] for row in tile)
    return [top, right, bottom, left]

def rotate(tile):
    n = len(tile)
    return [[tile[n-1-j][i] for j in range(n)] for i in range(n)]

def flip(tile):
    return [row[::-1] for row in tile]

def get_all_orientations(tile):
    orientations = []
    t = tile
    for _ in range(4):
        orientations.append(t)
        orientations.append(flip(t))
        t = rotate(t)
    return orientations

def part1(tiles):
    # Find edges and their matches
    edge_count = defaultdict(list)
    for tile_id, tile in tiles.items():
        for edge in get_edges(tile):
            edge_count[edge].append(tile_id)
            edge_count[edge[::-1]].append(tile_id)

    # Corners have exactly 2 edges that don't match any other tile
    corners = []
    for tile_id, tile in tiles.items():
        edges = get_edges(tile)
        unmatched = sum(1 for e in edges if len(edge_count[e]) == 1)
        if unmatched == 2:
            corners.append(tile_id)

    result = 1
    for c in corners:
        result *= c
    return result, corners

def assemble(tiles, corners):
    n = int(math.sqrt(len(tiles)))

    # Build edge to tile mapping
    edge_to_tiles = defaultdict(list)
    for tile_id, tile in tiles.items():
        for edge in get_edges(tile):
            edge_to_tiles[edge].append(tile_id)
            edge_to_tiles[edge[::-1]].append(tile_id)

    # Start with a corner, oriented so unmatched edges are top and left
    grid = [[None] * n for _ in range(n)]
    used = set()

    # Find orientation for first corner
    corner_id = corners[0]
    for orient in get_all_orientations(tiles[corner_id]):
        edges = get_edges(orient)
        top_match = len(edge_to_tiles[edges[0]]) == 1
        left_match = len(edge_to_tiles[edges[3]]) == 1
        if top_match and left_match:
            grid[0][0] = (corner_id, orient)
            used.add(corner_id)
            break

    # Fill the grid
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                continue

            # Find matching tile
            if j > 0:
                left_tile = grid[i][j-1][1]
                need_left = ''.join(row[-1] for row in left_tile)
            else:
                need_left = None

            if i > 0:
                top_tile = grid[i-1][j][1]
                need_top = ''.join(top_tile[-1])
            else:
                need_top = None

            for tile_id, tile in tiles.items():
                if tile_id in used:
                    continue
                for orient in get_all_orientations(tile):
                    edges = get_edges(orient)
                    left_ok = need_left is None or edges[3] == need_left
                    top_ok = need_top is None or edges[0] == need_top
                    if left_ok and top_ok:
                        grid[i][j] = (tile_id, orient)
                        used.add(tile_id)
                        break
                if grid[i][j]:
                    break

    # Remove borders and combine
    tile_size = len(tiles[corners[0]]) - 2
    image_size = n * tile_size
    image = [['.' for _ in range(image_size)] for _ in range(image_size)]

    for i in range(n):
        for j in range(n):
            tile = grid[i][j][1]
            for ti in range(1, len(tile) - 1):
                for tj in range(1, len(tile[0]) - 1):
                    image[i * tile_size + ti - 1][j * tile_size + tj - 1] = tile[ti][tj]

    return image

def find_monsters(image):
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    monster_coords = []
    for i, row in enumerate(monster):
        for j, c in enumerate(row):
            if c == '#':
                monster_coords.append((i, j))

    height = len(image)
    width = len(image[0])
    monster_height = len(monster)
    monster_width = len(monster[0])

    for orient in get_all_orientations(image):
        count = 0
        for i in range(height - monster_height + 1):
            for j in range(width - monster_width + 1):
                if all(orient[i + di][j + dj] == '#' for di, dj in monster_coords):
                    count += 1
        if count > 0:
            total_hashes = sum(row.count('#') for row in orient)
            return total_hashes - count * len(monster_coords)

    return 0

def part2(tiles, corners):
    image = assemble(tiles, corners)
    return find_monsters(image)

if __name__ == '__main__':
    tiles = parse('/Users/adamemery/advent-of-code/2020/input20')
    p1, corners = part1(tiles)
    print(f"Part 1: {p1}")
    print(f"Part 2: {part2(tiles, corners)}")
