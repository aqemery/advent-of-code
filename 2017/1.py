import sys
from collections import defaultdict, Counter, deque
from itertools import combinations, permutations, batched, chain
from math import prod
from dataclasses import dataclass
from functools import cache
from statistics import median
import re
import heapq


def solve(data, times):
    return


def part1(data):
    total = 0
    size = len(data)
    for i, v in enumerate(data):
        if v == data[(i+1) % size]:
            total += int(v)
    return total


def part2(data):
    total = 0
    size = len(data)
    halfway = size // 2
    for i, v in enumerate(data):
        if v == data[(i+halfway) % size]:
            total += int(v)
    return total

if __name__ == "__main__":
    d = input()
    
    print("part 1:", part1(d))
    print("part 2:", part2(d))
    # print("part 1:", solve(d, 1))
    # print("part 2:", solve(d, 2))
