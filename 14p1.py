import sys

mask = None
final_mem = {}
mem = {}

def apply_mask():
  global final_mem, mem 
  for k, v in mem.items():
    binary = f'{v:036b}'
    mask_applied = ''.join([b if m == 'X' else m for b, m in zip(binary, mask)])
    final_mem[k]  = int(mask_applied, 2)
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