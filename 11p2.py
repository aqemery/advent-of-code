import sys

empty = set()
filled = {(x,y) 
  for y, l in enumerate(sys.stdin.readlines())
  for x, c in enumerate(l.strip())
  if c == 'L'
}

max_x, max_y = max(filled)
around = [(x,y) for x in range(-1,2) for y in range(-1,2)]
around.remove((0,0))

def add(a, b):
  return tuple(sum(z) for z in zip(a,b)) 

def in_bounds(check):
  return 0 <= check[0] <= max_x and 0 <= check[1] <= max_y

def test_sit(t):
  for a in around:
    check = add(t, a)
    while in_bounds(check):
      if check in filled:
        return False
      elif check in empty:
        break
      check = add(check, a)
  return True

def test_empty(t):
  count = 0
  for a in around:
    if count == 5:
      return True
    check = add(t, a)
    while in_bounds(check):
      if check in filled:
        count += 1
        break
      elif check in empty:
        break
      check = add(check, a)
  if count > 4:
    return True
  return False 

def run():
  new_empty = set()
  new_filled = set()

  for t in empty:
    if test_sit(t):
      new_filled.add(t)
    else: 
      new_empty.add(t)

  for t in filled:
    if test_empty(t):
      new_empty.add(t)
    else: 
      new_filled.add(t)

  return new_empty, new_filled

last = empty
empty, filled = run()

while last != empty:
  last = empty
  empty, filled = run()

print(len(filled))
