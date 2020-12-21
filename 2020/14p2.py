import sys

mask = None
final_mem = {}
mem = {}

def add_bit(addresses, bit):
  for i in range(len(addresses)):
    addresses[i] += bit

def apply_mask():
  global final_mem, mem 
  for k, v in mem.items():
    binary = f'{k:036b}'
    mask_applied = ''.join([b if m == '0' else m for b, m in zip(binary, mask)])
    addresses = ['']

    for ma in mask_applied:
      if ma == 'X':
        first = addresses[:]
        second = addresses[:]
        add_bit(first, '0')
        add_bit(second, '1')
        addresses = first + second
      else:
        add_bit(addresses, ma)

    addresses = [int(a, 2) for a in addresses]
    for a in addresses:
      final_mem[a] = v
  mem = {}

for l in sys.stdin.readlines():
  action = l.split(' = ')
  if action[0] == 'mask':
    apply_mask()
    
    mask = action[1]
  else: 
    exec(l)

apply_mask()
print(sum(final_mem.values()))