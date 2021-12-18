import sys


def to_int(x):
    return int("".join(x), 2)


bits = None
lines = sys.stdin.readlines()
bits = [0] * (len(lines[0]) - 1)
half = len(lines) / 2

for l in lines:
    for i, c in enumerate(l):
        if c == "1":
            bits[i] += 1

gamma = ["1" if b > half else "0" for b in bits]
epsilon = ["1" if b == "0" else "0" for b in gamma]

print(to_int(gamma) * to_int(epsilon))
