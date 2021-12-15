import sys
import heapq

lines = sys.stdin.read().split('\n')
grid = {(x,y):int(v) for y, row in enumerate(lines) for x, v in enumerate(row)}
around = [(1,0),(-1,0),(0,1),(0,-1)]

start = (0,0)
q = [(0,*start)]
max_risk = {start:0}
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

end = size*5 - 1
while q:
  risk, x, y = heapq.heappop(q)
  adj = [(x+ax, y+ay) for ax, ay in around]
  if x == y == end:
    print(risk)
    break
  for adj_pos in adj:
    if adj_risk := grid.get(adj_pos):
      next_risk = risk + adj_risk
      if current_risk := max_risk.get(adj_pos):
        if next_risk < current_risk:
          heapq.heappush(q, (next_risk, *adj_pos))
          max_risk[adj_pos] = next_risk
      else:
        heapq.heappush(q, (next_risk, *adj_pos))
        max_risk[adj_pos] = next_risk
