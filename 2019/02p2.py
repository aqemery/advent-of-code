in_memory = list(map(int, input().split(",")))
memory = list(in_memory)


def get_params(pos):
    return memory[pos + 1 : pos + 4]


for noun in range(0, 99):
    for verb in range(1, 99):
        memory = list(in_memory)
        pointer = 0
        opcode = memory[pointer]

        memory[1] = noun
        memory[2] = verb

        while opcode != 99:
            if opcode == 1:
                x, y, z = get_params(pointer)
                memory[z] = memory[x] + memory[y]
            elif opcode == 2:
                x, y, z = get_params(pointer)
                memory[z] = memory[x] * memory[y]
            else:
                print("opcode error")
                break
            pointer += 4
            opcode = memory[pointer]

        if memory[0] == 19690720:
            print(f"{noun:2.0f}{verb:2.0f}")
            exit()
