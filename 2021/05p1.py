import sys
import math

vents = [[list(map(int, c.split(','))) for c in l.split(' -> ')] for l in sys.stdin.read().split('\n')]
vent_map = {}

def add_coord(x,y):
  global vent_map
  try:
    vent_map[(x,y)] += 1
  except KeyError:
    vent_map[(x,y)] = 1
  
def get_step(v1, v2):
  angle = math.atan2(v2[1]-v1[1], v2[0]-v1[0])
  return int(math.cos(angle)), int(math.sin(angle))

for v in vents:
  step = get_step(*v)
  if any(step):
    current, end = v
    add_coord(*current)
    while current != end:
      current = list(map(sum,zip(current,step)))
      add_coord(*current)

print(len([v for v in vent_map.values() if v > 1]))
