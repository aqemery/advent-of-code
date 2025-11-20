def parse(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    program = list(map(int, lines[4].split(': ')[1].split(',')))
    return a, b, c, program

def run(a, b, c, program):
    output = []
    ip = 0

    def combo(op):
        if op <= 3: return op
        if op == 4: return a
        if op == 5: return b
        if op == 6: return c

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:  # adv
            a = a >> combo(operand)
        elif opcode == 1:  # bxl
            b = b ^ operand
        elif opcode == 2:  # bst
            b = combo(operand) % 8
        elif opcode == 3:  # jnz
            if a != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            b = b ^ c
        elif opcode == 5:  # out
            output.append(combo(operand) % 8)
        elif opcode == 6:  # bdv
            b = a >> combo(operand)
        elif opcode == 7:  # cdv
            c = a >> combo(operand)

        ip += 2

    return output

def part1(a, b, c, program):
    return ','.join(map(str, run(a, b, c, program)))

def part2(program):
    # Work backwards - each iteration outputs one value and divides A by 8
    def find(target, ans):
        if not target:
            return ans
        for t in range(8):
            a = ans << 3 | t
            # Run program and check if it produces the target suffix
            output = run(a, 0, 0, program)
            if output == list(target):
                result = find(target[:-1], a)
                if result is not None:
                    return result
            elif len(output) == len(target) and output[-1] == target[-1]:
                # Partial match, continue searching
                result = find(target[:-1], a)
                if result is not None:
                    return result
        return None

    # Try building the answer bit by bit
    def search(depth, val):
        if depth == len(program):
            return val
        for i in range(8):
            new_val = val * 8 + i
            output = run(new_val, 0, 0, program)
            if output == program[-depth-1:]:
                result = search(depth + 1, new_val)
                if result is not None:
                    return result
        return None

    return search(0, 0)

if __name__ == '__main__':
    a, b, c, program = parse('/Users/adamemery/advent-of-code/2024/input17')
    print(f"Part 1: {part1(a, b, c, program)}")
    print(f"Part 2: {part2(program)}")
