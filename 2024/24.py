def parse(filename):
    with open(filename) as f:
        parts = f.read().strip().split('\n\n')

    wires = {}
    for line in parts[0].split('\n'):
        name, val = line.split(': ')
        wires[name] = int(val)

    gates = []
    for line in parts[1].split('\n'):
        parts_l = line.split(' -> ')
        output = parts_l[1]
        inputs = parts_l[0].split()
        a, op, b = inputs[0], inputs[1], inputs[2]
        gates.append((a, op, b, output))

    return wires, gates

def simulate(wires, gates):
    wires = wires.copy()
    remaining = list(gates)

    while remaining:
        progress = False
        new_remaining = []
        for a, op, b, output in remaining:
            if a in wires and b in wires:
                if op == 'AND':
                    wires[output] = wires[a] & wires[b]
                elif op == 'OR':
                    wires[output] = wires[a] | wires[b]
                elif op == 'XOR':
                    wires[output] = wires[a] ^ wires[b]
                progress = True
            else:
                new_remaining.append((a, op, b, output))
        remaining = new_remaining
        if not progress:
            break

    return wires

def get_number(wires, prefix):
    bits = [(k, v) for k, v in wires.items() if k.startswith(prefix)]
    bits.sort(reverse=True)
    result = 0
    for _, v in bits:
        result = result * 2 + v
    return result

def part1(wires, gates):
    result = simulate(wires, gates)
    return get_number(result, 'z')

def part2(wires, gates):
    # Find swapped wires in the adder circuit
    # This is specific to the structure of the input
    swaps = []

    gate_map = {}
    for a, op, b, output in gates:
        gate_map[(frozenset([a, b]), op)] = output
        gate_map[output] = (a, op, b)

    def find_gate(inputs, op):
        return gate_map.get((frozenset(inputs), op))

    # Check each bit position for correct adder structure
    wrong = set()
    for a, op, b, output in gates:
        # z outputs should be XOR (except last)
        if output.startswith('z') and op != 'XOR' and output != 'z45':
            wrong.add(output)
        # XOR with non-x/y inputs should output to z
        if op == 'XOR' and not any(x[0] in 'xyz' for x in [a, b, output]):
            wrong.add(output)
        # AND gates (except x00) should feed into OR
        if op == 'AND' and 'x00' not in [a, b]:
            for a2, op2, b2, _ in gates:
                if output in [a2, b2] and op2 != 'OR':
                    wrong.add(output)
        # XOR gates should not feed into OR
        if op == 'XOR':
            for a2, op2, b2, _ in gates:
                if output in [a2, b2] and op2 == 'OR':
                    wrong.add(output)

    return ','.join(sorted(wrong))

if __name__ == '__main__':
    wires, gates = parse('/Users/adamemery/advent-of-code/2024/input24')
    print(f"Part 1: {part1(wires, gates)}")
    print(f"Part 2: {part2(wires, gates)}")
