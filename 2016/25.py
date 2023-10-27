import sys
from collections import defaultdict


def run_transmiter(data, a=0):
    out_buffer = []
    index = 0
    registers = defaultdict(int)
    registers["a"] = a
    toggles = set()

    def cpy(value, register):
        if value.isalpha():
            registers[register] = registers[value]
        else:
            registers[register] = int(value)

    def inc(register):
        registers[register] += 1

    def dec(register):
        registers[register] -= 1

    def jnz(is_zero, value):
        if is_zero.isalpha():
            if registers[is_zero] != 0:
                return int(value)
        elif int(is_zero) != 0:
            if value.isalpha():
                return registers[value]
            return int(value)

    def out(value):
        if value.isalpha():
            return registers[value]
        return int(value)

    while index < len(data):
        toggled = index in toggles
        match data[index].split():
            case ["cpy", value, register]:
                if not toggled:
                    cpy(value, register)
                else:
                    index += jnz(value, register)
                    continue
            case ["inc", register]:
                if not toggled:
                    inc(register)
                else:
                    dec(register)
            case ["dec", register]:
                if not toggled:
                    dec(register)
                else:
                    inc(register)
            case ["jnz", is_zero, value]:
                if not toggled:
                    if jmp := jnz(is_zero, value):
                        index += jmp
                        continue
                else:
                    cpy(is_zero, value)
            case ["tgl", register]:
                if not toggled:
                    to_toggle = index + registers[register]
                    if to_toggle in toggles:
                        toggles.remove(to_toggle)
                    else:
                        toggles.add(index + registers[register])
                else:
                    inc(register)

            case ["out", register]:
                if not toggled:
                    out_buffer.append(out(register))
                    if len(out_buffer) == 10:
                        return out_buffer
                else:
                    inc(register)
        index += 1

    return registers["a"]


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    a = 0
    while True:
        if run_transmiter(d, a) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:
            print("Final:", a)
            exit()
        a += 1