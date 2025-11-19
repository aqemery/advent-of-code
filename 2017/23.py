def parse(filename):
    with open(filename) as f:
        return [line.strip().split() for line in f]


def get_value(registers, x):
    try:
        return int(x)
    except ValueError:
        return registers.get(x, 0)


def part1(instructions):
    registers = {}
    ip = 0
    mul_count = 0

    while 0 <= ip < len(instructions):
        instr = instructions[ip]
        op = instr[0]

        if op == 'set':
            registers[instr[1]] = get_value(registers, instr[2])
        elif op == 'sub':
            registers[instr[1]] = get_value(registers, instr[1]) - get_value(registers, instr[2])
        elif op == 'mul':
            registers[instr[1]] = get_value(registers, instr[1]) * get_value(registers, instr[2])
            mul_count += 1
        elif op == 'jnz':
            if get_value(registers, instr[1]) != 0:
                ip += get_value(registers, instr[2])
                continue

        ip += 1

    return mul_count


def part2(instructions):
    # Analyze the code to find initial values
    # Typically: b = first set value, then b = b * 100 + 100000, c = b + 17000
    # The code counts composite numbers from b to c stepping by 17

    # Extract initial b value from first instruction
    b = int(instructions[0][2])

    # When a=1, the initialization does:
    # b = b * 100 + 100000
    # c = b + 17000
    b = b * 100 + 100000
    c = b + 17000

    # Count composite numbers from b to c, stepping by 17
    h = 0
    for n in range(b, c + 1, 17):
        if not is_prime(n):
            h += 1

    return h


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    instructions = parse('2017/input')

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
