import sys

alive = {(x,y,0) for y, l in enumerate(sys.stdin.readlines())
  for x, c in enumerate(l) if c == '#'}

def axis(v):
  return range(v-1,v+2)

def adjacent(cord):
  x,y,z = cord
  return [(nx,ny,nz) for nz in axis(z) for ny in axis(y) for nx in axis(x)]

def is_alive(cord):
  adj = adjacent(cord)
  count = 0
  for n in adj:
    if n in alive:
      count += 1
  if count == 3:
    return True
  return False

for _ in range(6):
  already_checked = set()
  new_alive = set()
  for a in alive:
    adj = adjacent(a)
    count = -1
    for n in adj: 
      if n in alive:
        count += 1
      elif not n in already_checked:
        already_checked.add(n)
        if is_alive(n):
          new_alive.add(n)
    if count in [2,3]:
      new_alive.add(a)
  alive = new_alive

print(len(alive))
