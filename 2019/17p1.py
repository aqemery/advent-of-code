class Computer:
    def __init__(self, program):
        self.program = program
        self.memory = program.copy() + [0] * 10000
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


program = list(map(int, input().split(",")))
g = Computer(program).run()

print(chr(next(g)), end="")


points = {}
x = 0
y = 0
while True:
    try:
        c = chr(next(g))
        x += 1

        if c is "\n":
            x = 0
            y += 1
        elif c is "#":
            points[(x, y)] = True
        print(c, end="")
    except StopIteration:
        break

alignment = 0
for k in points.keys():
    x, y = k
    if {(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)}.issubset(points):
        alignment += (x - 1) * y
print(alignment)
