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
    registers = defaultdict(int)
    last_played = None
    index = 0

    def get(y):
        if y.isalpha():
            return registers[y]
        return int(y)
    
    while index < len(data):
        l = data[index]
        match l.split():
            case ["snd", x]:
                last_played = registers[x]
            case ["set", x, y]:
                registers[x] = get(y)
            case ["add", x, y]:
                registers[x] += get(y)
            case ["mul", x, y]:
                registers[x] *= get(y)
            case ["mod", x, y]:
                registers[x] %= get(y)
            case ["rcv", x]:
                if registers[x] != 0:
                    return last_played
                registers[x] = last_played
            case ["jgz", x, y]:
                if registers[x] > 0:
                    index += get(y)
                    continue
            case _:
                print(l)
        index += 1
    return last_played


def part2(data):
    return
    incoming = yield
    yield outgoing

if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
    # print("part 1:", solve(d, 1))
    # print("part 2:", solve(d, 2))
