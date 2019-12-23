import math
class Computer:
  def __init__(self, program):
    self.program = program
    self.memory = program.copy() +[0]*10000
    self.pointer = 0
    self.relative = 0
    self.waiting = False

  def get_params(self, instruct, *rw):
    param_modes = list(map(int, instruct[:-2]))
    param_modes.reverse()
    count = len(rw)
    params = [self.memory[self.pointer+i] for i in range(1,count+1)]
    for i in range(len(param_modes)):
      if i >= count:
        break
      if rw[i]:
        if param_modes[i] == 0 and len(params) > i:
          params[i] = params[i]
        elif param_modes[i] == 2 and len(params) > i: 
          params[i] = params[i] + self.relative
      else:
        if param_modes[i] == 0 and len(params) > i:
          params[i] = self.memory[params[i]]
        elif param_modes[i] == 2 and len(params) > i: 
          params[i] = self.memory[params[i] + self.relative]
    self.pointer += count + 1
    if count == 1:
      return params[0]
    return params

  def set_input(self, iv):
    self.input = iv

  def run(self):
    while True:
      instruct = f'{self.memory[self.pointer]:04d}'
      opcode = int(instruct[-2:])
      if opcode in [1,2,7,8]:
        x,y,z = self.get_params(instruct, False, False, True)
        if opcode == 1:
          self.memory[z] = x + y
        elif opcode == 2:
          self.memory[z] = x * y
        elif opcode == 7:
          self.memory[z] = 1 if x < y else 0
        elif opcode == 8:
          self.memory[z] = 1 if x == y else 0
      elif opcode == 3:
        self.waiting = True
        self.memory[self.get_params(instruct, True)] = yield
        self.waiting = False
      elif opcode == 4:
        yield self.get_params(instruct, False)
      elif opcode == 9:
        self.relative += self.get_params(instruct, False)
      elif opcode in [5, 6]:
        x,y = self.get_params(instruct, False, False)
        if x != 0 and opcode == 5:
          self.pointer = y
        elif x == 0 and opcode == 6:
          self.pointer = y
      elif opcode == 99:
        break
      else:
        print('opcode error', opcode)
        break

program = list(map(int, input().split(',')))

comp = Computer(program)
g = comp.run()

def print_out(o):
  if o != None:
    try:
      print(chr(o),end='')
    except ValueError:
      print('Damage', o)
    

def move_to_next_input():
  while not comp.waiting:
    try:
      print_out(next(g))
    except StopIteration:
      break

commands = '''NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
'''

move_to_next_input()

for c in list(map(ord, list(commands))):
  out = g.send(c)
  print_out(out)
  move_to_next_input()
