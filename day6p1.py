orbits = {}

def orbit_count(key, depth):
  if key in orbits:
    sub_orbits = orbits[key]
    count = len(sub_orbits)
    for so in sub_orbits:
      count += depth + orbit_count(so, depth + 1)
    return count
  return 0

while True:
  try:
    l = input().split(')')
    if l[0] in orbits:
      orbits[l[0]] += [l[1]]
    else:
      orbits[l[0]] = [l[1]]
  except EOFError:
    break

print(orbit_count('COM', 0))