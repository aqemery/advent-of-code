from collections import deque


class Computer:
    def __init__(self, program, address):
        self.memory = program.copy() + [0] * 10000
        self.pointer = 0
        self.relative = 0
        self.input_queue = deque([address])
        self.output_buffer = []
        self.halted = False
        self.idle_count = 0

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

    def step(self):
        """Run one instruction. Returns list of outputs if any, or empty list."""
        if self.halted:
            return []

        outputs = []
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
            addr = self.get_params(instruct, True)
            if self.input_queue:
                self.memory[addr] = self.input_queue.popleft()
                self.idle_count = 0
            else:
                self.memory[addr] = -1
                self.idle_count += 1
        elif opcode == 4:
            val = self.get_params(instruct, False)
            self.output_buffer.append(val)
            self.idle_count = 0
            if len(self.output_buffer) == 3:
                outputs = self.output_buffer.copy()
                self.output_buffer = []
        elif opcode == 9:
            self.relative += self.get_params(instruct, False)
        elif opcode in [5, 6]:
            x, y = self.get_params(instruct, False, False)
            if x != 0 and opcode == 5:
                self.pointer = y
            elif x == 0 and opcode == 6:
                self.pointer = y
        elif opcode == 99:
            self.halted = True

        return outputs


def solve(program):
    # Part 1: Find Y value of first packet sent to address 255
    computers = [Computer(program, i) for i in range(50)]
    part1 = None

    while part1 is None:
        for i in range(50):
            outputs = computers[i].step()
            if outputs:
                dest, x, y = outputs
                if dest == 255:
                    part1 = y
                    break
                elif 0 <= dest < 50:
                    computers[dest].input_queue.append(x)
                    computers[dest].input_queue.append(y)

    # Part 2: Implement NAT and find first Y delivered twice in a row
    computers = [Computer(program, i) for i in range(50)]
    nat_packet = None
    last_nat_y = None
    part2 = None

    while part2 is None:
        # Run all computers for a batch of cycles
        any_activity = False

        for _ in range(1000):  # Run a batch of cycles
            for i in range(50):
                outputs = computers[i].step()
                if outputs:
                    any_activity = True
                    dest, x, y = outputs
                    if dest == 255:
                        nat_packet = (x, y)
                    elif 0 <= dest < 50:
                        computers[dest].input_queue.append(x)
                        computers[dest].input_queue.append(y)

        # Check if network is idle
        # Network is idle if all computers have empty input queues and high idle counts
        is_idle = all(
            len(c.input_queue) == 0 and c.idle_count > 10
            for c in computers
        )

        if is_idle and nat_packet is not None:
            x, y = nat_packet
            if y == last_nat_y:
                part2 = y
                break
            last_nat_y = y
            computers[0].input_queue.append(x)
            computers[0].input_queue.append(y)
            # Reset idle counts
            for c in computers:
                c.idle_count = 0

    return part1, part2


if __name__ == "__main__":
    with open("/Users/adamemery/advent-of-code/2019/input23") as f:
        program = list(map(int, f.read().strip().split(",")))

    part1, part2 = solve(program)
    print(f"Day 23: Part 1 = {part1}, Part 2 = {part2}")
