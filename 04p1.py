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

valid = 0
for r in records:
  count = len(r)
  if 'cid' in r:
    count -= 1
  if count == 7:
    valid += 1

print(valid)
