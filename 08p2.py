import sys

ops = [l.split() for l in sys.stdin.readlines()]
end = len(ops)

def run(stack):
  visited = set()
  pointer = 0 
  accumulator = 0

  while not pointer in visited:
    if pointer == end:
      return accumulator
    visited.add(pointer)
    op = stack[pointer]
    f = op[0]
    
    if f == 'jmp':
      pointer += int(op[1])
    elif f == 'acc':
      accumulator += int(op[1])
      pointer += 1
    else:
      pointer += 1

for i, op in enumerate(ops):
  if op[0] == 'acc':
    continue

  f = 'jmp'
  if op[0] == 'jmp':
    f = 'nop'

  new_ops = ops[:]
  new_ops[i] = (f, op[1]) 

  acc = run(new_ops)
  if acc:
    print(acc)
    break
  