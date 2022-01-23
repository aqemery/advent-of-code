import sys
from itertools import permutations


weights = {}
nodes = set()
d = sys.stdin.read().split("\n")
for l in d:
    start, _, end, _, dist = l.split()
    nodes.add(start)
    nodes.add(end)
    weights[(start, end)] = int(dist)
    weights[(end, start)] = int(dist)

paths = [sum([weights[(n1,n2)] for n1, n2 in zip(p,p[1:])]) for p in  permutations(nodes)]

print("part 1:", min(paths))
print("part 2:", max(paths))
