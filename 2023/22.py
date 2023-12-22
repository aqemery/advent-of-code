import sys
from collections import defaultdict, Counter, deque
from itertools import combinations, permutations, batched, chain
from math import prod
from dataclasses import dataclass
from functools import cache
from statistics import median
import re
import heapq


def get_block(line):
    # return a set of all the points in the block
    start, end = line.split("~")
    sx, sy, sz = [int(n) for n in start.split(",")]
    ex, ey, ez = [int(n) + 1 for n in end.split(",")]
    return set(
        (x, y, z) for x in range(sx, ex) for y in range(sy, ey) for z in range(sz, ez)
    )


def move_blocks(blocks):
    # attempt to move each block down one
    # return True if any block was moved
    # return the new blocks
    m_blocks = blocks.copy()
    moved = False
    for i, block in enumerate(m_blocks):
        test = set((x, y, z - 1) for x, y, z in block)
        if any(z < 0 for _, _, z in test):
            continue
        for j, other in enumerate(m_blocks):
            if i == j:
                continue
            if block & other:
                break
        else:
            m_blocks[i] = test
            moved = True
    return moved, m_blocks


def part1(data):
    # get all the blocks as sets of points
    blocks = [get_block(line) for line in data]

    # move the blocks down until they can't move any more
    moved = False
    while not moved:
        moved, blocks = move_blocks(blocks)

    # count the number of block removals that don't cause any other blocks to fall
    count = 0
    for block in blocks:
        # remove the current block and try to move the rest
        test_blocks = [b for b in blocks if b != block]
        moved, _ = move_blocks(test_blocks)
        if not moved:
            count += 1
    return count


def part2(data):
    return


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
