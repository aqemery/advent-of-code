import math 
import itertools

def lcm(l):
    a,b,c = l
    first = abs(a*b) // math.gcd(a, b)
    return abs(first*c) // math.gcd(first, c)

moons = []
while True:
  try:
    list(map(exec, input().strip('<>').split(', ')))
    m = {'pos':[x,y,z], 'vel': [0]*3}
    moons.append(m)
  except EOFError:
    break

pairs = list(itertools.combinations(moons,2))

revs = [None, None, None]
count = 0
while not all(revs):
  for p in pairs:
    a,b = p
    for i in range(3):
      ap = a['pos'][i]
      bp = b['pos'][i]
      if ap > bp:
        a['vel'][i] -= 1
        b['vel'][i] += 1
      elif ap < bp:
        a['vel'][i] += 1
        b['vel'][i] -= 1
  for m in moons:
    m['pos'] = [sum(i) for i in zip(m['pos'], m['vel'])]

  count += 1

  for i in range(3):
    if not revs[i] and not any([m['vel'][i] for m in moons]):
      revs[i] = count
      
print(lcm(revs)*2)