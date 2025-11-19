#!/usr/bin/env python3
"""Advent of Code 2018 Day 12: Subterranean Sustainability"""

def parse_input(data):
    lines = data.strip().split('\n')
    initial = lines[0].split(': ')[1]

    rules = {}
    for line in lines[2:]:
        if line:
            pattern, result = line.split(' => ')
            rules[pattern] = result

    return initial, rules

def simulate(state, rules, offset):
    """Simulate one generation and return new state and offset"""
    # Pad the state with empty pots
    state = '....' + state + '....'
    offset -= 4

    new_state = ''
    for i in range(2, len(state) - 2):
        pattern = state[i-2:i+3]
        new_state += rules.get(pattern, '.')

    # Trim leading and trailing dots
    first_plant = new_state.find('#')
    last_plant = new_state.rfind('#')

    if first_plant == -1:
        return '', 0

    new_state = new_state[first_plant:last_plant + 1]
    offset += first_plant + 2

    return new_state, offset

def sum_pots(state, offset):
    """Sum the indices of pots containing plants"""
    total = 0
    for i, c in enumerate(state):
        if c == '#':
            total += i + offset
    return total

def solve(data):
    initial, rules = parse_input(data)

    state = initial
    offset = 0

    # Part 1: After 20 generations
    for _ in range(20):
        state, offset = simulate(state, rules, offset)

    part1 = sum_pots(state, offset)

    # Continue for Part 2
    # Reset and look for a pattern
    state = initial
    offset = 0

    prev_state = state
    prev_sum = sum_pots(state, offset)

    for gen in range(1, 1001):
        state, offset = simulate(state, rules, offset)
        current_sum = sum_pots(state, offset)

        if state == prev_state:
            # Pattern found - state is the same, just shifted
            diff = current_sum - prev_sum
            # Calculate sum at 50 billion generations
            part2 = current_sum + (50_000_000_000 - gen) * diff
            break

        prev_state = state
        prev_sum = current_sum
    else:
        # If no pattern found within 1000 generations, continue manually
        part2 = current_sum

    return part1, part2

if __name__ == "__main__":
    with open("/Users/adamemery/advent-of-code/2018/input12") as f:
        data = f.read()

    part1, part2 = solve(data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
