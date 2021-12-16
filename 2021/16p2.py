import math
bits = ''.join([f'{int(c,16):04b}' for c in input()])
p = 0

ops = {
  0: lambda x: sum(x),
  1: lambda x: math.prod(x),
  2: lambda x: min(x),
  3: lambda x: max(x),
  5: lambda x: 1 if x[0] > x[1] else 0,
  6: lambda x: 1 if x[0] < x[1] else 0,
  7: lambda x: 1 if x[0] == x[1] else 0
}

def read_bits(x):
  global p
  p += x
  return bits[p-x:p]

def read_int(x):
  return int(read_bits(x), 2)

def read_packet():
  read_int(3)
  id = read_int(3)
  if id == 4:
    return read_literal()
  else:
    return read_operator(id)

def read_literal():
  packet = ''
  while read_int(1):
    packet += read_bits(4)
  packet += read_bits(4)
  return int(packet, 2)

def read_operator(op):
  if read_int(1):
    paks = [read_packet() for _ in range(read_int(11))]
  else:
    length = read_int(15)
    cp = p
    paks = []
    while p - cp < length:
      paks.append(read_packet())
  return ops[op](paks)

print(read_packet())
