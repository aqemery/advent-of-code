def parse(dir):
  return dir[0],int(dir[1:])

def map_steps(points):
  w_map = {}
  for p in points:
    w_map[p[:-1]] = p[-1]
  return w_map, set([p[:-1] for p in points])

def get_points(wire):
  pos = [0,0]
  points = []
  steps = 0
  for l in wire:
    if l[0] == 'U':
      points += [(pos[0], pos[1] + y, steps + y) for y in range(1,l[1]+1)]
      pos[1] += l[1]
    elif l[0] == 'D':
      points += [(pos[0], pos[1] - y, steps + y) for y in range(1,l[1]+1)]
      pos[1] -= l[1]
    elif l[0] == 'L':
      points += [(pos[0] - x, pos[1], steps + x) for x in range(1,l[1]+1)]
      pos[0] -= l[1]
    elif l[0] == 'R':
      points += [(pos[0] + x, pos[1], steps + x) for x in range(1,l[1]+1)]
      pos[0] += l[1]
    steps += l[1]
  return points

w1 = list(map(parse, input().split(',')))
w2 = list(map(parse, input().split(',')))
w1_map, w1_points = map_steps(get_points(w1))
w2_map, w2_points = map_steps(get_points(w2))
cross = list(w1_points.intersection(w2_points))

dist = w2_map[cross[0]] + w1_map[cross[0]]
for p in cross:
  d = w2_map[p] + w1_map[p]
  if(d < dist):
    dist = d
print(dist)
