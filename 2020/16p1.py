import sys

fields, tickets, nearby = sys.stdin.read().split('\n\n')

locations = []
for l in fields.split('\n'):
  first = l.split(': ')
  name = first[0]
  ranges = []
  for r in first[1].split(' or '):
    args = list(map(int, r.split('-')) )
    ranges += [range(args[0], args[1]+1)]
  locations.append((name, ranges))

tickets = list(map(int, tickets.split()[-1].split(',')))
nearby = [map(int, n.split(',')) for n in nearby.split()[2:]]

def is_valid(n):
  for l in locations:
    if any([n in r for r in l[1]]):
      return True
  return False

error_rate = 0
for t in nearby:
  for n in t:
    if not is_valid(n):
      error_rate += n

print(error_rate)
