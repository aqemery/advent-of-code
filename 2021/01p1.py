import sys

depths  = list(map(int, sys.stdin.readlines()))
out = [v for i, v in enumerate(depths) if v > depths[i-1]]
print(len(out))
