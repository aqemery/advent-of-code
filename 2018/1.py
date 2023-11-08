import sys


data = sys.stdin.read().split('\n')

out = sum(int(n) for n in data)




print("part1:", out)