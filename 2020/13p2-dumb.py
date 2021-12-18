import math

input()

buses = [(int(v), i) for i, v in enumerate(input().split(",")) if v != "x"]

current = 0
step = 1
for value, offset in buses:
    while (current + offset) % value != 0:
        current += step
    step *= value

print(current)
