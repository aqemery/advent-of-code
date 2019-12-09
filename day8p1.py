from itertools import permutations 

data = input()

width = 25
height = 6
total_pixels = width * height
min_layer_count = None
min_layer = None

for i in range(len(data)//total_pixels):
  start = i * total_pixels
  stop = (i+1) * total_pixels
  layer = data[start:stop]
  count = layer.count('0')
  if min_layer_count == None or count < min_layer_count:
    min_layer_count = count
    min_layer = layer

print(min_layer.count('1') * min_layer.count('2'))