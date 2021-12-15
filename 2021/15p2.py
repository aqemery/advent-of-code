import sys
from collections import deque

lines = sys.stdin.read().split('\n')
grid = {(x,y):int(v) for y, row in enumerate(lines) for x, v in enumerate(row)}
around = [(1,0),(-1,0),(0,1),(0,-1)]

start = (0,0)
max_risk = {start:0}
q = deque([start])

big_grid = {}
size = max(grid)[0] + 1

for x in range(5):
  for y in range(5):
    for k, v in grid.items():
      new_risk = v + x + y
      while new_risk > 9:
        new_risk -= 9
      ox, oy = k
      big_grid[(ox+size*x,oy+size*y)] = new_risk
grid = big_grid

while q:
  pos = q.popleft()
  adj = [tuple(sum(z) for z in zip(pos, a)) for a in around]
  risk = max_risk.get(pos) 
  for adj_pos in adj:
    if adj_risk := grid.get(adj_pos):
      next_risk = risk + adj_risk
      if current_risk := max_risk.get(adj_pos):
        if next_risk < current_risk:
          q.append(adj_pos)
          max_risk[adj_pos] = next_risk
      else:
        q.append(adj_pos)
        max_risk[adj_pos] = next_risk

print(max_risk[max(max_risk)])
