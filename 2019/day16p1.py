import math

fft = list(map(int, list(input())))
pattern = [0, 1, 0, -1]

patterns = []
for i in range(len(fft)):
  out = []
  for p in pattern:
    out += [p] * (i + 1)
  out *= math.ceil((len(fft)+1)/len(out))
  out = out[1:len(fft)+1]
  patterns.append(out)

for x in range(100):
  fft = [int(str(sum([i[0] * i[1] for i in zip(fft, p)]))[-1]) for p in patterns]

print(''.join(map(str, fft[:8])))