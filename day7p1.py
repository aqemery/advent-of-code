from itertools import permutations 

class Computer:
  def __init__(self, program):
    self.program = program
    self.input = []

  def reset(self):
    self.memory = program.copy()
    self.pointer = 0

  def get_params(self, count,instruct):
    param_modes = list(map(int, instruct[:-2]))
    param_modes.reverse()
    params = [self.memory[self.pointer+i] for i in range(1,count+1)]
    for i in range(len(param_modes)):
      if param_modes[i] == 0 and len(params) > i:
        params[i] = self.memory[params[i]]
    self.pointer += count + 1
    return params

  def set_input(self, iv):
    self.input = iv

  def read_input(self):
    out = self.input[0]
    self.input = self.input[1:]
    return out

  def run(self, iv):
    self.set_input(iv)
    self.reset()
    out = ''
    while True:
      instruct = f'{self.memory[self.pointer]:04d}'
      opcode = int(instruct[-2:])
      if opcode in [1,2,7,8]:
        x,y,z = self.get_params(3, instruct)
        if opcode == 1:
          self.memory[z] = x + y
        elif opcode == 2:
          self.memory[z] = x * y
        elif opcode == 7:
          self.memory[z] = 1 if x < y else 0
        elif opcode == 8:
          self.memory[z] = 1 if x == y else 0
      elif opcode == 3:
        self.memory[self.memory[self.pointer+1]] = self.read_input()
        self.pointer += 2
      elif opcode == 4:
        x = self.get_params(1, instruct)
        print("OUT", x[0])
        out += str(x[0])
      elif opcode in [5, 6]:
        x,y = self.get_params(2, instruct)
        if x != 0 and opcode == 5:
          self.pointer = y
        elif x == 0 and opcode == 6:
          self.pointer = y
      elif opcode == 99:
        break
      else:
        print('opcode error', opcode)
        break
    return int(out)

program = list(map(int, input().split(',')))
c = Computer(program)   

signal = 0
for order in permutations(range(0, 5)):

  input_value = 0
  for p in order:
    print("------")
    input_value = c.run([p, input_value])
  if input_value > signal:
    signal = input_value

print(signal)
