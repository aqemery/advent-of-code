import sys


def get_block(line):
    start, end = line.split("~")
    sx, sy, sz = [int(n) for n in start.split(",")]
    ex, ey, ez = [int(n) + 1 for n in end.split(",")]
    return set(
        (x, y, z) for x in range(sx, ex) for y in range(sy, ey) for z in range(sz, ez)
    )


def move_blocks(blocks):
    m_blocks = blocks.copy()
    moved = False
    did_move = []
    for i, block in enumerate(m_blocks):
        test = set((x, y, z - 1) for x, y, z in block)
        if any(z < 0 for _, _, z in test):
            continue
        for j, other in enumerate(m_blocks):
            if i == j:
                continue
            if test & other:
                break
        else:
            m_blocks[i] = test
            moved = True
            did_move.append(i)
    return moved, m_blocks, did_move


def drop_all(blocks):
    all_moved = set()
    moved = True
    while moved:
        moved, blocks, did_move = move_blocks(blocks)
        all_moved.update(did_move)
    return blocks, len(all_moved)


def part1(blocks):
    count = 0
    for block in blocks:
        test_blocks = [b for b in blocks if b != block]
        moved, _, _ = move_blocks(test_blocks)
        if not moved:
            count += 1
    return count


def part2(blocks):
    count = 0
    for block in blocks:
        test_blocks = [b for b in blocks if b != block]
        all_moved = set()
        moved = True
        while moved:
            moved, test_blocks, did_move = move_blocks(test_blocks)
            all_moved.update(did_move)
        count += len(all_moved)
    return count


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    blocks = [get_block(line) for line in d]
    blocks, _ = drop_all(blocks)
    print("part 1:", part1(blocks))
    print("part 2:", part2(blocks))
