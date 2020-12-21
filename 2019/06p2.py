orbits = {}

def orbit_list(key):
  ol = [key]
  if key in orbits:
    ol += orbit_list(orbits[key])
  return ol

while True:
  try:
    l = input().split(')')
    orbits[l[1]] = l[0]
  except EOFError:
    break

youl = orbit_list('YOU')
sanl = tuple(orbit_list('SAN'))

count = -2
for o in youl:
  count += 1
  if o in sanl:
    count += sanl.index(o) - 1 
    break

print(count)
