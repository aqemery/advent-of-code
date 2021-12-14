import sys
from collections import defaultdict, Counter
from functools import reduce
import math

polymer, pairs = sys.stdin.read().split('\n\n')
rules = {a:[a[0]+b,b+a[1]] for a, b in [p.split(' -> ') for p in pairs.split('\n')]}

counts = Counter(a+b for a, b in zip(polymer, polymer[1:]))
for _ in range(40):
  nc = Counter()
  for k, v in counts.items():
    nc.update({p:v for  p in rules[k]})
  counts = nc

letter_counts = defaultdict(int)
for k, v in counts.items():
  for l in k:
    letter_counts[l] += v

com = [math.ceil(v/2) for _,v in letter_counts.items()]
print(max(com) - min(com))