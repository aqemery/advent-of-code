import re
from collections import defaultdict

def parse_input(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Parse starting state
    start_match = re.search(r'Begin in state (\w+)', content)
    start_state = start_match.group(1)

    # Parse number of steps
    steps_match = re.search(r'after (\d+) steps', content)
    num_steps = int(steps_match.group(1))

    # Parse state transitions
    states = {}
    state_blocks = re.split(r'In state (\w+):', content)[1:]  # Skip first empty part

    for i in range(0, len(state_blocks), 2):
        state_name = state_blocks[i]
        state_content = state_blocks[i + 1]

        # Parse rules for current value 0 and 1
        rules = {}

        # Find both "If the current value is X:" blocks
        value_blocks = re.split(r'If the current value is (\d):', state_content)[1:]

        for j in range(0, len(value_blocks), 2):
            current_value = int(value_blocks[j])
            rule_content = value_blocks[j + 1]

            # Parse write value
            write_match = re.search(r'Write the value (\d)', rule_content)
            write_value = int(write_match.group(1))

            # Parse move direction
            move_match = re.search(r'Move one slot to the (left|right)', rule_content)
            direction = 1 if move_match.group(1) == 'right' else -1

            # Parse next state
            next_match = re.search(r'Continue with state (\w+)', rule_content)
            next_state = next_match.group(1)

            rules[current_value] = (write_value, direction, next_state)

        states[state_name] = rules

    return start_state, num_steps, states

def simulate_turing_machine(start_state, num_steps, states):
    tape = defaultdict(int)  # Default value is 0
    cursor = 0
    state = start_state

    for _ in range(num_steps):
        current_value = tape[cursor]
        write_value, direction, next_state = states[state][current_value]

        tape[cursor] = write_value
        cursor += direction
        state = next_state

    # Checksum is number of 1s on the tape
    return sum(tape.values())

def solve(filename):
    start_state, num_steps, states = parse_input(filename)

    # Part 1: Run the Turing machine
    part1 = simulate_turing_machine(start_state, num_steps, states)

    # Part 2: Free star (no computation needed)
    part2 = "(free star)"

    return part1, part2

if __name__ == "__main__":
    part1, part2 = solve("/Users/adamemery/advent-of-code/2017/input25")
    print(f"Day 25: Part 1 = {part1}, Part 2 = {part2}")
