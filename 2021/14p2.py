import sys
from collections import Counter, defaultdict
import math

polymer, pairs = sys.stdin.read().split('\n\n')
rules = {a:[a[0]+b,b+a[1]] for a, b in [p.split(' -> ') for p in pairs.split('\n')]}

counts = defaultdict(int)

for p in [polymer[i:i+2] for i in range(len(polymer)-1)]:
  counts[p] += 1

for i in range(40):
  nc = defaultdict(int)
  for k, v in counts.items():
    for p in rules[k]:
      nc[p] +=v
  counts = nc

letter_counts = defaultdict(int)
for k, v in counts.items():
  for l in k:
    letter_counts[l] += v

com = [math.ceil(v/2) for _,v in letter_counts.items()]
print(max(com) - min(com))
