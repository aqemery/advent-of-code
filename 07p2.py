import sys

bags = {}

def visit(b):
  count = 1
  for c in bags[b]:
    count += visit(c[0]) * c[1] 
  return count 

for l in sys.stdin.readlines():
  parent, children = l.split(' contain ')
  parent_bag = ' '.join(parent.split()[:-1])

  contained = []
  for c in children.split(', '):
    try:
      count = int(c[0])
      c_bag = ' '.join(c.split()[1:-1])
      contained.append((c_bag, count))
    except ValueError:
      break

  bags[parent_bag] = contained

print(visit('shiny gold')-1)