import sys

lines = sys.stdin.read().split('\n')
grid = {(x,y):int(v) for y, row in enumerate(lines) for x, v in enumerate(row)}
around = [(1,0),(-1,0),(0,1),(0,-1)]

def grid_check(v, pos):
  try:
    return v < grid[pos]
  except KeyError:
    return True

out = 0
for k, v in grid.items():
  checks = [tuple(sum(z) for z in zip(k, a)) for a in around]
  if all([grid_check(v, c) for c in checks]):
    out += 1 + v
print(out)
