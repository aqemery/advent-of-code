intcode = list(map(int, input().split(",")))


def get_positions(pos):
    return intcode[pos + 1 : pos + 4]


current_pos = 0
opcode = intcode[current_pos]

intcode[1] = 12
intcode[2] = 2

while opcode != 99:
    if opcode == 1:
        x, y, z = get_positions(current_pos)
        intcode[z] = intcode[x] + intcode[y]
    elif opcode == 2:
        x, y, z = get_positions(current_pos)
        intcode[z] = intcode[x] * intcode[y]
    else:
        print("opcode error")
        break
    current_pos += 4
    opcode = intcode[current_pos]

print(intcode)
