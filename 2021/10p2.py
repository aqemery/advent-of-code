import sys
from collections import deque

pop = {")": "(", "]": "[", "}": "{", ">": "<"}
close = {"(": 1, "[": 2, "{": 3, "<": 4}


def line_value(line):
    stack = deque()
    for c in line:
        if c in pop:
            if not stack or stack.pop() != pop[c]:
                return
        else:
            stack.append(c)
    score = 0
    while stack:
        score = score * 5 + close[stack.pop()]
    return score


lines = sys.stdin.read().split("\n")

values = [v for v in [line_value(l) for l in lines] if v]
values.sort()
print(values[len(values) // 2])
