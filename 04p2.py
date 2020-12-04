import re

records = []
current = {}

while True:
  try:
    line = input()
    if line:
      for pair in line.split():
        k, v = pair.split(':')
        current[k] = v
    else:
      records.append(current)
      current = {}
      continue
  except EOFError:
    records.append(current)
    break

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid = 0
for r in records:
  count = len(r)
  if 'cid' in r:
    count -= 1
  if count == 7:
    if not int(r['byr']) in range(1920, 2003):
      continue
    if not int(r['iyr']) in range(2010, 2021):
      continue
    if not int(r['eyr']) in range(2020, 2031):
      continue
    if not re.search('^#[0-9a-f]{6}$', r['hcl']):
      continue
    if not r['ecl'] in eye_colors:
      continue
    if not re.search('^\d{9}$', r['pid']):
      continue

    h = r['hgt']
    end = h[-2:]
    amount = h[:-2]

    cm = end == 'cm' and int(amount) in range(150, 194)
    inch = end == 'in' and int(amount) in range(59, 77)

    if not (cm or inch):
      continue

    valid += 1

print(valid)
