bits = ''.join([f'{int(c,16):04b}' for c in input()])
p = 0
total = 0

def read_bits(x):
  global p
  p += x
  return bits[p-x:p]

def read_int(x):
  return int(read_bits(x), 2)

def read_packet():
  global total
  ver = read_int(3)
  total += ver
  id = read_int(3)
  if id == 4:
    read_literal()
  else:
    read_operator()

def read_literal():
  packet = ''
  while read_int(1):
    packet += read_bits(4)
  packet += read_bits(4)
  return int(packet, 2)

def read_operator():
  if read_int(1):
    for _ in range(read_int(11)):
      read_packet()
  else:
    length = read_int(15)
    cp = p
    while p - cp < length:
      read_packet()
    
read_packet()
print(total)
