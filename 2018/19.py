def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    ip_reg = int(lines[0].split()[1])
    program = []
    for line in lines[1:]:
        parts = line.strip().split()
        if parts:
            op = parts[0]
            a, b, c = int(parts[1]), int(parts[2]), int(parts[3])
            program.append((op, a, b, c))

    return ip_reg, program

# Opcode implementations
def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]

def addi(regs, a, b, c):
    regs[c] = regs[a] + b

def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]

def muli(regs, a, b, c):
    regs[c] = regs[a] * b

def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]

def bani(regs, a, b, c):
    regs[c] = regs[a] & b

def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]

def bori(regs, a, b, c):
    regs[c] = regs[a] | b

def setr(regs, a, b, c):
    regs[c] = regs[a]

def seti(regs, a, b, c):
    regs[c] = a

def gtir(regs, a, b, c):
    regs[c] = 1 if a > regs[b] else 0

def gtri(regs, a, b, c):
    regs[c] = 1 if regs[a] > b else 0

def gtrr(regs, a, b, c):
    regs[c] = 1 if regs[a] > regs[b] else 0

def eqir(regs, a, b, c):
    regs[c] = 1 if a == regs[b] else 0

def eqri(regs, a, b, c):
    regs[c] = 1 if regs[a] == b else 0

def eqrr(regs, a, b, c):
    regs[c] = 1 if regs[a] == regs[b] else 0

OPCODES = {
    'addr': addr, 'addi': addi, 'mulr': mulr, 'muli': muli,
    'banr': banr, 'bani': bani, 'borr': borr, 'bori': bori,
    'setr': setr, 'seti': seti, 'gtir': gtir, 'gtri': gtri,
    'gtrr': gtrr, 'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr
}

def sum_of_divisors(n):
    """Calculate sum of all divisors of n"""
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

def run_with_optimization(ip_reg, program, initial_r0):
    """
    This program calculates sum of divisors of a number.
    We run until we detect the target number being set up,
    then calculate directly.
    """
    regs = [initial_r0, 0, 0, 0, 0, 0]
    ip = 0

    # Run until the setup is complete
    # The program sets up a number in one register, then loops to find divisors
    # We need to detect when the main loop starts

    steps = 0
    last_regs = None

    while 0 <= ip < len(program):
        regs[ip_reg] = ip
        op, a, b, c = program[ip]
        OPCODES[op](regs, a, b, c)
        ip = regs[ip_reg] + 1
        steps += 1

        # After initial setup (jump to end, then back), find the target
        # The target number will be the largest value in registers
        # Look for the pattern: when we return to instruction 1 after setup
        if ip == 1 and steps > 20:
            # Find which register has the target number (usually reg 2)
            target = max(regs)
            return sum_of_divisors(target)

        # Failsafe - if running too long, use direct calculation
        if steps > 10000:
            target = max(regs)
            return sum_of_divisors(target)

    return regs[0]

def part1(ip_reg, program):
    return run_with_optimization(ip_reg, program, 0)

def part2(ip_reg, program):
    return run_with_optimization(ip_reg, program, 1)

if __name__ == '__main__':
    ip_reg, program = parse_input('/Users/adamemery/advent-of-code/2018/input19')
    print(f"Part 1: {part1(ip_reg, program)}")
    print(f"Part 2: {part2(ip_reg, program)}")
