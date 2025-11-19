import re

def parse_input(filename):
    with open(filename) as f:
        content = f.read()

    # Split into samples and program
    parts = content.split('\n\n\n')
    samples_text = parts[0]
    program_text = parts[1] if len(parts) > 1 else ""

    # Parse samples
    samples = []
    sample_pattern = re.compile(r'Before:\s*\[(\d+), (\d+), (\d+), (\d+)\]\n(\d+) (\d+) (\d+) (\d+)\nAfter:\s*\[(\d+), (\d+), (\d+), (\d+)\]')
    for match in sample_pattern.finditer(samples_text):
        groups = match.groups()
        before = [int(groups[i]) for i in range(4)]
        instruction = [int(groups[i]) for i in range(4, 8)]
        after = [int(groups[i]) for i in range(8, 12)]
        samples.append((before, instruction, after))

    # Parse program
    program = []
    for line in program_text.strip().split('\n'):
        if line.strip():
            program.append([int(x) for x in line.split()])

    return samples, program

# Define all opcodes
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

OPCODES = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def test_opcode(before, instruction, after, opcode_func):
    regs = before[:]
    _, a, b, c = instruction
    opcode_func(regs, a, b, c)
    return regs == after

def part1(samples):
    count = 0
    for before, instruction, after in samples:
        matches = sum(1 for op in OPCODES if test_opcode(before, instruction, after, op))
        if matches >= 3:
            count += 1
    return count

def part2(samples, program):
    # Find possible opcodes for each opcode number
    possible = {i: set(OPCODES) for i in range(16)}

    for before, instruction, after in samples:
        opcode_num = instruction[0]
        for op in OPCODES:
            if not test_opcode(before, instruction, after, op):
                possible[opcode_num].discard(op)

    # Determine exact mapping
    opcode_map = {}
    while len(opcode_map) < 16:
        for num, ops in possible.items():
            if num not in opcode_map and len(ops) == 1:
                op = list(ops)[0]
                opcode_map[num] = op
                # Remove this op from all other possibilities
                for other_num in possible:
                    possible[other_num].discard(op)
                break

    # Run program
    regs = [0, 0, 0, 0]
    for instruction in program:
        opcode_num, a, b, c = instruction
        opcode_map[opcode_num](regs, a, b, c)

    return regs[0]

if __name__ == '__main__':
    samples, program = parse_input('/Users/adamemery/advent-of-code/2018/input16')
    print(f"Part 1: {part1(samples)}")
    print(f"Part 2: {part2(samples, program)}")
