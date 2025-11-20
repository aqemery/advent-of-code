from functools import cache

def parse(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

NUM_PAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

DIR_PAD = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

def get_moves(pad, start, end):
    sr, sc = pad[start]
    er, ec = pad[end]
    dr, dc = er - sr, ec - sc

    vert = ('^' * -dr if dr < 0 else 'v' * dr)
    horiz = ('<' * -dc if dc < 0 else '>' * dc)

    # Check which order is valid (avoid gap)
    moves = []
    gap = (3, 0) if pad == NUM_PAD else (0, 0)

    # Try horizontal first
    if (sr, ec) != gap:
        moves.append(horiz + vert + 'A')
    # Try vertical first
    if (er, sc) != gap:
        moves.append(vert + horiz + 'A')

    return moves if moves else [horiz + vert + 'A']

@cache
def min_presses(seq, depth, is_num=False):
    pad = NUM_PAD if is_num else DIR_PAD
    total = 0
    pos = 'A'

    for char in seq:
        moves = get_moves(pad, pos, char)
        if depth == 0:
            total += min(len(m) for m in moves)
        else:
            total += min(min_presses(m, depth - 1) for m in moves)
        pos = char

    return total

def solve(codes, robots):
    total = 0
    for code in codes:
        presses = min_presses(code, robots, is_num=True)
        num = int(code[:-1])
        total += presses * num
    return total

if __name__ == '__main__':
    codes = parse('/Users/adamemery/advent-of-code/2024/input21')
    print(f"Part 1: {solve(codes, 2)}")
    print(f"Part 2: {solve(codes, 25)}")
