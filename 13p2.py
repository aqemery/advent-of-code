import math
input()

# chinese remainder theorem

buses = [(int(v),i) for i, v in enumerate(input().split(',')) if v != 'x']

times = [b[0] for b in buses]
times_prod = math.prod(times)

somethings = []
for t in times:
  div = times_prod // t
  mod_inverse = pow(div, -1, t)
  something = (mod_inverse * div) % times_prod
  somethings.append(something)

offset_times = [b[0]-b[1] for b in buses]

somthings_offset_multiplied = [a*w for a,w in zip(offset_times, somethings)]
answer = sum(somthings_offset_multiplied) % times_prod
print(answer)
