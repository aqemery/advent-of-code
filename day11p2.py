from itertools import permutations 
import math 

class Computer:
  def __init__(self, program):
    self.program = program
    self.memory = program.copy() +[0]*1000
    self.pointer = 0
    self.relative = 0

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
        self.memory[self.get_params(instruct, True)] = yield
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

class Robot():
  def __init__(self):
    self.angle = 0
    self.pos_x = 0
    self.pos_y = 0
    self.panels = {(0,0): 1}


  def read_panel(self):
    pos = (self.pos_x, self.pos_y)
    if pos in self.panels:
      return self.panels[pos]
    return 0

  def paint(self, color):
    self.panels[(self.pos_x, self.pos_y)] = color

  def turn_and_move(self, dir):
    value = math.pi/2
    if dir == 0:
      value *= -1
    self.angle += value
    self.pos_x += int(-math.cos(self.angle))
    self.pos_y += int(math.sin(self.angle))


program = list(map(int, input().split(',')))
brains = Computer(program).run()
mr_robot = Robot()

g = Computer(program).run()
next(g)
while True:
  try:
    color = g.send(mr_robot.read_panel())
    mr_robot.paint(color)
    direction = next(g)
    mr_robot.turn_and_move(direction)
    next(g)
  except StopIteration:
    break

max_x = 0
max_y = 0

for p in mr_robot.panels.keys():
  if p[0] > max_x:
    max_x = p[0]
  if p[1] > max_y:
    max_y = p[1]

image = []
for i in range(max_x+1):
  image.append([' ']*(max_y+1))

for p in mr_robot.panels.keys():
  if mr_robot.panels[p] == 1:
    image[p[0]][p[1]] = '*'

for i in image:
  print(''.join(i))
