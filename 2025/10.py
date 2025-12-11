import sys
import z3

lines = sys.stdin.read().split("\n")
p1 = 0
p2 = 0
for line in lines:
    indicator, *buttons, joltage = line.split()
    indicator = [c == "#" for c in indicator[1:-1]]
    buttons = [[int(v) for v in b[1:-1].split(",")] for b in buttons]
    joltage = [int(v) for v in joltage[1:-1].split(",")]

    button_presses = 0
    seen = set()

    possible_states = set([tuple([False] * len(indicator))])
    while True:
        button_presses += 1
        next_states = set()
        for state in possible_states:
            for button in buttons:
                new_state = list(state)
                for i in button:
                    new_state[i] = not new_state[i]
                new_state = tuple(new_state)
                next_states.add(new_state)

        possible_states = next_states

        for state in possible_states:
            if all(s == i for s, i in zip(state, indicator)):
                p1 += button_presses
                break
        else:
            continue
        break

    # Use Z3 to solve for minimum button presses

    s = z3.Optimize()

    # Create variables for how many times we press each button
    button_vars = [z3.Int(f"b{i}") for i in range(len(buttons))]

    # Each button must be pressed >= 0 times
    for bv in button_vars:
        s.add(bv >= 0)

    # For each position in joltage, sum of button presses must equal target
    for pos in range(len(joltage)):
        # Sum contributions from each button
        expr = z3.Sum(
            [button_vars[i] if pos in buttons[i] else 0 for i in range(len(buttons))]
        )
        s.add(expr == joltage[pos])

    # Minimize total button presses
    total_presses = z3.Sum(button_vars)
    s.minimize(total_presses)

    if s.check() == z3.sat:
        model = s.model()
        min_presses = model.eval(total_presses).as_long()
        p2 += min_presses
    else:
        print("No solution found!", file=sys.stderr)


print("part 1:", p1)
print("part 2:", p2)
