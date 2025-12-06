import sys
from math import prod

lines = sys.stdin.read().split("\n")
lines_split = [l.split() for l in lines]
col = list(zip(*lines_split))

total = 0
for c in col:
    sign = c[-1]
    values = [int(x) for x in c[:-1]]
    if sign == "+":
        total += sum(values)
    elif sign == "*":
        total += prod(values)

print("part 1:", total)


zip_all = list(zip(*lines))
signs = [z[-1] for z in zip_all if z[-1] in "+*"]
numbers = ["".join(z[:-1]).strip() for z in zip_all]

total = 0
for s in signs:
    subtotal = int(numbers.pop(0))
    while value := numbers.pop(0):
        value = int(value)
        if s == "+":
            subtotal += value
        elif s == "*":
            subtotal *= value

        if not numbers:
            break
    total += subtotal

print("part 2:", total)
