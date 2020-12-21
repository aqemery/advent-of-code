memory = list(map(int, input().split(',')))
pointer = 0

def get_params(count,instruct):
  global pointer
  param_modes = list(map(int, instruct[:-2]))
  param_modes.reverse()
  params = [memory[pointer+i] for i in range(1,count+1)]
  for i in range(len(param_modes)):
    if param_modes[i] == 0 and len(params) > i:
      params[i] = memory[params[i]]
  pointer += count + 1
  return params

out = ''
while True:
  instruct = f'{memory[pointer]:04d}'
  opcode = int(instruct[-2:])
  if opcode in [1,2]:
    x,y,z = get_params(3, instruct)
    if opcode == 1:
      memory[z] = x + y
    elif opcode == 2:
      memory[z] = x * y
  elif opcode == 3:
    memory[memory[pointer+1]] = 1
    pointer += 2
  elif opcode == 4:
    x = get_params(1, instruct)
    out += str(x[0])
  elif opcode == 99:
    break
  else:
    print('opcode error', opcode)
    break
print(int(out))