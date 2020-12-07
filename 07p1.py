import sys

visited = {}
bags = {}
find = 'shiny gold'

def visit(b):
  global visited

  if b == find:
    return False 

  if b in visited:
    return visited[b]

  if find in bags[b]:
    visited[b] = True
    return True

  return any([visit(c) for c in bags[b]])
  

for l in sys.stdin.readlines():
  parent, children = l.split(' contain ')
  parent_bag = ' '.join(parent.split()[:-1])

  contained = []
  for c in children.split(', '):
    try:
      count = int(c[0])
      c_bag = ' '.join(c.split()[1:-1])
      contained.append(c_bag)
    except ValueError:
      break
    
  bags[parent_bag] = contained

print(sum(map(visit, bags.keys())))