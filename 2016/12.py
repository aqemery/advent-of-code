import sys
from collections import defaultdict


def solve(data, c=0):
    index = 0
    registers = defaultdict(int)
    registers["c"] = c
    while index < len(data):
        match data[index].split():
            case ["cpy", value, register]:
                if value.isalpha():
                    registers[register] = registers[value]
                else:
                    registers[register] = int(value)
            case ["inc", register]:
                registers[register] += 1
            case ["dec", register]:
                registers[register] -= 1
            case ["jnz", is_zero, value]:
                if is_zero.isalpha():
                    if registers[is_zero] != 0:
                        index += int(value)
                        continue
                elif int(is_zero) != 0:
                    index += int(value)
                    continue
        index += 1

    return registers["a"]


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")

    print("part 1:", solve(d))
    print("part 2:", solve(d, 1))
