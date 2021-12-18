import time


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
                self.memory[self.get_params(instruct, True)] = yield
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


class RepairDroid:
    def __init__(self, program):
        self.g = Computer(program).run()
        self.pos_x = 0
        self.pos_y = 0
        self.direction = 2
        self.direction_values = ((1, (0, -1)), (4, (1, 0)), (2, (0, 1)), (3, (-1, 0)))
        self.path = []

    def get_dir(self, d):
        tmp = self.direction
        tmp += d
        if tmp < 0:
            tmp += 4
        if tmp > 3:
            tmp -= 4
        return tmp

    def log_move(self, dp):
        dx, dy = dp
        self.pos_x += dx
        self.pos_y += dy
        pos = (self.pos_x, self.pos_y)
        self.path.append(pos)

    def move(self, d):
        dir_val = self.get_dir(d)
        dr = self.direction_values[dir_val]
        next(self.g)
        mr = self.g.send(dr[0])
        if mr:
            self.direction = dir_val
            self.log_move(dr[1])
            return mr
        else:
            return 0

    def step(self):
        for d in range(1, -3, -1):
            moved = self.move(d)
            if moved is 2:
                return True
                print("exit found")
            if moved:
                break
        return False


program = list(map(int, input().split(",")))
droid = RepairDroid(program)
droid.step()
end_x = None
end_y = None
while (droid.pos_x, droid.pos_y) != (0, 0):
    if droid.step():
        end_x = droid.pos_x
        end_y = droid.pos_y

oxygen_map = {}
for c in set(droid.path):
    oxygen_map[c] = False

oxygen_map[(end_x, end_y)] = True
count = 0
while not all(oxygen_map.values()):
    count += 1
    new_oxygen_map = {}
    for k in oxygen_map.keys():
        if oxygen_map[k]:
            new_oxygen_map[k] = True
            x, y = k
            ne = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for nk in ne:
                if nk in oxygen_map:
                    new_oxygen_map[nk] = True

    for k in oxygen_map.keys():
        if not k in new_oxygen_map:
            new_oxygen_map[k] = False
    oxygen_map = new_oxygen_map

print(count)
