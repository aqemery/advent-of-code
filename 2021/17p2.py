rx, ry = [map(int, dem.split('=')[1].split('..')) for dem in input().split(',')[-2:]]
lx, mx = rx
ly, my = ry

def step_x(vx):
  x = 0
  while vx > 0:
    x += vx
    vx -= 1
    yield x

def step_both(vx,vy):
  y = 0
  endx = None
  for x in step_x(vx):
    y += vy
    vy -= 1
    endx = x
    yield x, y
  while True:
    y += vy
    vy -= 1
    yield endx, y

def solve_cord(l,m):
  vols = set()
  for v in range(1,m+1):
    for c in step_x(v):
      if m >= c >= l:
        vols.add(v)
        break
  return vols

x_vols = solve_cord(lx, mx)
found = set()
for vx in x_vols:
  for vy in range(ly, -ly+1):
    for x,y in step_both(vx, vy):
      if y < ly:
        break
      if y <= my and y >= ly and mx >= x >= lx:
        found.add((vx,vy))

print(len(found))
