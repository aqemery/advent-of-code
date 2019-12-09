from itertools import permutations 

data = input()

width = 25
height = 6
total_pixels = width * height
min_layer_count = None
min_layer = None

layers = []
for i in range(len(data)//total_pixels):
  start = i * total_pixels
  stop = (i+1) * total_pixels
  layers.insert(0, data[start:stop]) 

merge = [0] * total_pixels

for l in layers:
  for i in range(len(l)):
    if l[i] != '2':
      merge[i] = l[i]

for y in range(height):
  for x in range(width):
    value = merge[y*width+x]
    if value == '1':
      print('*', end='')
    else:
      print(' ', end='')
  print('')