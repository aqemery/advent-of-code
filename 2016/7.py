import sys


def part1(data):
    count = 0
    for line in data:
        tls = False
        hypernet = False
        for i, c in enumerate(line):
            if c == "[":
                hypernet = True
            elif c == "]":
                hypernet = False
            else:
                sequence = line[i - 3 : i + 1]
                if len(sequence) < 4 or "]" in sequence or "[" in sequence:
                    continue

                if (
                    sequence[0] == sequence[3]
                    and sequence[1] == sequence[2]
                    and sequence[0] != sequence[1]
                ):
                    if hypernet:
                        tls = False
                        break
                    else:
                        tls = True
        if tls:
            count += 1
    return count


def part2(data):
    count = 0
    for line in data:
        tls = False
        hypernet = False
        aba = set()
        bab = set()
        for i, c in enumerate(line):
            if c == "[":
                hypernet = True
            elif c == "]":
                hypernet = False
            else:
                sequence = line[i - 2 : i + 1]
                if len(sequence) < 3 or "]" in sequence or "[" in sequence:
                    continue

                if sequence[0] == sequence[-1] and sequence[0] != sequence[1]:
                    if hypernet:
                        bab.add("".join(sequence))
                    else:
                        aba.add("".join(sequence))

        aba_shift = set("".join([b, a, b]) for a, b, _ in aba)

        if aba_shift & bab:
            count += 1
    return count


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
