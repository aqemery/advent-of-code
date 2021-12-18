width = 40
height = 20
tiles = [[0] * height for _ in range(width)]
types = [" ", "|", "B", "_", "o"]


def draw():
    print("-" * width)
    for y in range(height):
        for x in range(width):
            print(types[tiles[x][y]], end="")
        print()


def get_joystick():
    draw()
    i = input("a: left enter: stay d: right")

    if i is "a":
        return -1
    if i is "":
        return 0
    if i is "d":
        return 1


class Computer:
    def __init__(self, program):
        self.program = program
        self.memory = program.copy() + [0] * 1000
        self.pointer = 0
        self.relative = 0

    def get_params(self, instruct, *rw):
        param_modes = list(map(int, instruct[:-2]))
        param_modes.reverse()
        count = len(rw)
        params = [self.memory[self.pointer + i] for i in range(1, count + 1)]
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
            instruct = f"{self.memory[self.pointer]:04d}"
            opcode = int(instruct[-2:])
            if opcode in [1, 2, 7, 8]:
                x, y, z = self.get_params(instruct, False, False, True)
                if opcode == 1:
                    self.memory[z] = x + y
                elif opcode == 2:
                    self.memory[z] = x * y
                elif opcode == 7:
                    self.memory[z] = 1 if x < y else 0
                elif opcode == 8:
                    self.memory[z] = 1 if x == y else 0
            elif opcode == 3:
                self.memory[self.get_params(instruct, True)] = get_joystick()
            elif opcode == 4:
                yield self.get_params(instruct, False)
            elif opcode == 9:
                self.relative += self.get_params(instruct, False)
            elif opcode in [5, 6]:
                x, y = self.get_params(instruct, False, False)
                if x != 0 and opcode == 5:
                    self.pointer = y
                elif x == 0 and opcode == 6:
                    self.pointer = y
            elif opcode == 99:
                break
            else:
                print("opcode error", opcode)
                break


with open("input.txt") as f:
    program = list(map(int, f.readline().split(",")))
program[0] = 2
g = Computer(program).run()


score = 0
while True:
    try:
        x = next(g)
        y = next(g)
        t = next(g)
        if x == -1 and y == 0:
            score = t
        else:
            tiles[x][y] = t
    except StopIteration:
        break

print(score)
