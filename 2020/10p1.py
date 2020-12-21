import sys

diffs = [0]*3
adapters = list(map(int, sys.stdin.readlines()))
adapters.sort()

last = 0
for a in adapters:
  diffs[a-last-1] += 1
  last = a

print(diffs[0] * (diffs[2]+1))
