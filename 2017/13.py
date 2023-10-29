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


def solve(data, delay=0):
    layers = {}
    for line in data:
        line = line.replace(":", "")
        rng, dpth = [int(n) for n in line.split()]
        layers[rng] = dpth

    max_rng = max(layers.keys())
    total = 0
    caught = False
    for i in range(max_rng + 1):
        if i in layers and (i+delay) % ((layers[i] - 1) * 2) == 0:
            caught = True
            total += i * layers[i]

    # 1 % 2

    return caught, total


def part2(data):
    delay = 0
    while True:
        caught, _ = solve(data, delay)
        if not caught:
            break
        delay += 1
    return delay


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    # print("part 1:", solve(d, delay=10))
    print("part 2:", part2(d))
    # print("part 1:", solve(d, 1))
    # print("part 2:", solve(d, 2))
