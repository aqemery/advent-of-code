import sys

def solve(data, inital_a=0):
    registers = {"a": inital_a, "b": 0}
    instructions = [l.replace(",", "").split() for l in data]
    i = 0

    while i < len(instructions):
        op = instructions[i]
        match op:
            case ["hlf", register]:
                registers[register] //= 2
            case ["tpl", register]:
                registers[register] *= 3
            case ["inc", register]:
                registers[register] += 1
            case ["jmp", offset]:
                offset = int(offset)
                i += offset
                continue
            case ["jie", register, offset]:
                offset = int(offset)
                if registers[register] % 2 == 0:
                    i += offset
                    continue
            case ["jio", register, offset]:
                offset = int(offset)
                if registers[register] == 1:
                    i += offset
                    continue
        i += 1

    return registers["b"]


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, inital_a=1))
