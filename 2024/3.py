import sys
import re

lines = sys.stdin.readlines()


def mul(x, y):
    return x * y


p1 = 0
for l in lines:
    matches = re.findall(r"mul\(\d+,\d+\)", l)
    p1 += sum(eval(m) for m in matches)

print("p1:", p1)


p2 = 0
enabled = True
for l in lines:
    matches = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", l)
    for m in matches:
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            p2 += eval(m)

print("p2:", p2)
