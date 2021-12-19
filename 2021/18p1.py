import sys
import math


def explode(flat):
    for i, first in enumerate(flat):
        if first[0] == 5:
            if i > 0:
                d, left = flat[i - 1]
                flat[i - 1] = [d, left + first[1]]
            if i + 2 < len(flat):
                _, second = flat[i + 1]
                d, right = flat[i + 2]
                flat[i + 2] = [d, right + second]
            flat[i + 1] = [4, 0]
            del flat[i]
            return True
    return False


def split(flat):
    for i, dp in enumerate(flat):
        d, v = dp
        if v > 9:
            flat[i] = [d + 1, math.floor(v / 2)]
            flat.insert(i + 1, [d + 1, math.ceil(v / 2)])
            return True
    return False


def read_number(n):
    nl = list()
    depth = 0
    for c in n:
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        elif c.isnumeric():
            nl.append([depth, int(c)])
    return nl


lines = sys.stdin.read().split("\n")
num = read_number(lines[0])
for line in lines[1:]:
    num += read_number(line)
    for n in num:
        n[0] += 1
    while explode(num) or split(num):
        pass

for i in range(4, 0, -1):
    for j, first in enumerate(num):
        d, v = first
        if d == i:
            _, s = num[j + 1]
            num[j] = [i - 1, v * 3 + s * 2]
            del num[j + 1]

print(num[0][1])
