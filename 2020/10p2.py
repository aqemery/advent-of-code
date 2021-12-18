import sys

adapters = [0] + list(map(int, sys.stdin.readlines()))
adapters.sort()

max_adp = max(adapters)
cons = {}
memo = {}

for i, v in enumerate(adapters):
    for j, u in enumerate(adapters[i + 1 :]):
        if u > v + 3:
            break
        if v in cons:
            cons[v] += [u]
        else:
            cons[v] = [u]


def dfs(node):
    global memo
    if node in memo:
        return memo[node]
    if not node in cons:
        if node == max_adp:
            return 1
        return 0

    paths = sum([dfs(c) for c in cons[node]])
    memo[node] = paths

    return paths


print(dfs(0))
