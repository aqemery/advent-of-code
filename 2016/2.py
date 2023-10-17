import sys

directions = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def solve(data, code, start):
    keypad = {}

    code = code.split("\n")

    for y, line in enumerate(code):
        for x, c in enumerate(line):
            if c != " ":
                keypad[(x, y)] = c

    current_pos = start
    code = ""

    for line in data:
        for c in line:
            dx, dy = directions[c]
            x, y = current_pos
            x += dx
            y += dy
            next_pos = (x, y)
            if next_pos in keypad:
                current_pos = next_pos
        code += str(keypad[current_pos])

    return code


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    code = "123\n456\n789"

    print("part 1:", solve(d, code, (1, 1)))
    code = "  1  \n 234 \n56789\n ABC \n  D  "
    print("part 2:", solve(d, code, (0, 2)))
