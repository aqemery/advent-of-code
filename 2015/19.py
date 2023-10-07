import sys


def part1(code, decoder):
    distinct = set()
    for k, v in decoder:
        strike_code = code.replace(k, "-")
        for i, c in enumerate(strike_code):
            if c == "-":
                mod_code = strike_code[:i] + v + strike_code[i + 1 :]
                mod_code = mod_code.replace("-", k)
                distinct.add(mod_code)
    return len(distinct)


def part2(code, decoder):
    reverse_decoder = {b: a for a, b in decoder}
    count = 0
    while len(code) > 1:
        for k, v in reverse_decoder.items():
            count += code.count(k)
            code = code.replace(k, v)
    return count


if __name__ == "__main__":
    keys, code = sys.stdin.read().split("\n\n")
    decoder = [tuple(k.split(" => ")) for k in keys.split("\n")]

    print("part 1:", part1(code, decoder))
    print("part 2:", part2(code, decoder))
