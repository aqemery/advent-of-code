count = 0
while True:
  try:
    r, l, p = input().split()
    r_min, r_max = map(int, r.split('-'))
    if p.count(l[0]) in range(r_min, r_max+1):
      count += 1
  except EOFError:
    break
print(count)