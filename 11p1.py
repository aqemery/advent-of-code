import sys

grid = {(x,y):c
  for y, l in enumerate(sys.stdin.readlines())
  for x, c in enumerate(l.strip())
  if c != '.'
}

around =[(x,y) for x in range(-1,2) for y in range(-1,2)]
around.remove((0,0))

def run():
  new_grid = {}
  for t in grid:
    keys = [tuple(sum(z) for z in zip(a,t)) for a in around]
    count = sum([1 for k in keys if grid.get(k) == '#'])

    v = grid[t]
    if v == 'L' and count == 0:
      new_grid[t] = '#'
    elif v == '#' and count >= 4:
      new_grid[t] = 'L'
    else:
      new_grid[t] = v
  return new_grid


last = run()
while  last != grid:
  grid = last
  last = run()

print(list(grid.values()).count('#'))
