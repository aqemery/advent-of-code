import sys

grid = [[int(c) for c in l] for l in sys.stdin.read().split('\n')]
around = [(1,0),(-1,0),(0,1),(0,-1)]

def grid_check(v,x,y):
  if x < 0 or y < 0:
    return True
  try:
    return v < grid[y][x]
  except IndexError:
    return True

low_points = [v for y, row in enumerate(grid) for x, v in enumerate(row) if all([grid_check(v,x+i,y+j) for i,j in around])]
print(sum([1 + lp for lp in low_points]))