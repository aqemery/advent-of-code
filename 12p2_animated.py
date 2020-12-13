import sys
# pygame setup
import pygame

pygame.init()
size = 800, 600
center = size[0]/2, size[1]/2
screen = pygame.display.set_mode(size)
color = (255,255,0)


boat = pygame.Surface((42, 42))
boat = pygame.Surface((42, 42))
pygame.draw.circle(boat, color, [10, 12], 4,1)
pygame.draw.circle(boat, color, [10, 22], 4,1)
pygame.draw.circle(boat, color, [10, 32], 4,1)
poly = [(10,0), (0,10), (0,40), (20,40), (20, 10)]
pygame.draw.polygon(boat, color, poly, 1)
lines = [[0,0]]

# probelem start

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

  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  
  #pygame draw 
  lines += [(ship[0]-21, ship[1]-21 )]
  angle = math.degrees(waypoint_angle())
  screen.fill((0,0,0))

  offset = [(ship[0]+center[0]-x,ship[1]+center[1]-y) for x,y in lines]
  pygame.draw.lines(screen, (255, 255, 255), False, offset, 1)
  screen.blit(pygame.transform.rotate(boat, angle), center)

  
  pygame.display.flip()
  pygame.time.wait(100)

print(int(abs(ship[0]) + abs(ship[1])))