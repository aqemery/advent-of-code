#!/usr/bin/env python3
"""Advent of Code 2018 Day 21: Chronal Conversion"""

def parse_input(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')

    ip_reg = int(lines[0].split()[1])
    program = []
    for line in lines[1:]:
        parts = line.split()
        op = parts[0]
        args = list(map(int, parts[1:]))
        program.append((op, args))

    return ip_reg, program

def execute_op(op, args, regs):
    a, b, c = args
    if op == 'addr':
        regs[c] = regs[a] + regs[b]
    elif op == 'addi':
        regs[c] = regs[a] + b
    elif op == 'mulr':
        regs[c] = regs[a] * regs[b]
    elif op == 'muli':
        regs[c] = regs[a] * b
    elif op == 'banr':
        regs[c] = regs[a] & regs[b]
    elif op == 'bani':
        regs[c] = regs[a] & b
    elif op == 'borr':
        regs[c] = regs[a] | regs[b]
    elif op == 'bori':
        regs[c] = regs[a] | b
    elif op == 'setr':
        regs[c] = regs[a]
    elif op == 'seti':
        regs[c] = a
    elif op == 'gtir':
        regs[c] = 1 if a > regs[b] else 0
    elif op == 'gtri':
        regs[c] = 1 if regs[a] > b else 0
    elif op == 'gtrr':
        regs[c] = 1 if regs[a] > regs[b] else 0
    elif op == 'eqir':
        regs[c] = 1 if a == regs[b] else 0
    elif op == 'eqri':
        regs[c] = 1 if regs[a] == b else 0
    elif op == 'eqrr':
        regs[c] = 1 if regs[a] == regs[b] else 0

def solve(filename):
    ip_reg, program = parse_input(filename)

    # Analyze the program - it has a check at line 28: eqrr 3 0 4
    # The program halts when reg[3] == reg[0]
    # Part 1: Find the first value reg[3] has at line 28
    # Part 2: Find the last unique value before cycle repeats

    # Reverse engineer the algorithm
    # The program computes a sequence of values in reg[3]
    # We need to simulate just the inner loop

    seen = []
    seen_set = set()

    # Simulate the computation
    r3 = 0

    while True:
        r1 = r3 | 65536
        r3 = 14906355  # This is from line 8: seti 14906355 8 3

        while True:
            r4 = r1 & 255
            r3 = r3 + r4
            r3 = r3 & 16777215
            r3 = r3 * 65899
            r3 = r3 & 16777215

            if 256 > r1:
                break

            # Find r4 such that (r4+1)*256 > r1
            r4 = r1 // 256
            r1 = r4

        # At this point, r3 is the value that would be compared to r0
        if r3 in seen_set:
            break

        seen.append(r3)
        seen_set.add(r3)

    part1 = seen[0]
    part2 = seen[-1]

    return part1, part2

if __name__ == '__main__':
    part1, part2 = solve('/Users/adamemery/advent-of-code/2018/input21')
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
