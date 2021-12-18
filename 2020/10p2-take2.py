import sys

adapters = [0] + list(map(int, sys.stdin.readlines()))
adapters.sort(reverse=True)
path = {adapters[0]: 1}
for a in adapters[1:]:
    path[a] = sum([path[p] for p in range(a + 1, a + 4) if p in path])

print(path[0])
