import sys
import math

waypoint = [-10,1] 
ship = [0,0]
keys = ['N', 'W', 'S', 'E']
values = [math.radians(i*90) for i in range(4)]
directions = dict(zip(keys, values))

def rotate(rads, dist):
  x = round(math.sin(rads) * dist)
  y = round(math.cos(rads) * dist)
  return [x,y]

def waypoint_dist():
  return math.sqrt(waypoint[0]**2 + waypoint[1]**2)

def waypoint_angle():
  return math.atan2(*waypoint)

def move_thing(thing, rads, dist):
  return [sum(z) for z in zip(thing, rotate(rads, dist))]

def rotate_waypoint(amount):
  rads = waypoint_angle() + math.radians(amount)
  return rotate(rads, waypoint_dist())

for l in sys.stdin.readlines():
  d = l[:1]
  v = int(l[1:])
  if d in directions:
    waypoint = move_thing(waypoint, directions[d], v)
  elif d == 'L':
    waypoint = rotate_waypoint(v)
  elif d == 'R':
    waypoint = rotate_waypoint(-v)
  elif d == 'F':
    ship = move_thing(ship, waypoint_angle(), waypoint_dist() * v)

print(int(abs(ship[0]) + abs(ship[1])))
