from functools import cache


@cache
def dance(data):
    programs = list(data)
    for i, step in enumerate(steps):
        move = step[0]
        args = step[1:]
        if move == "s":
            n = int(args)
            programs = programs[-n:] + programs[:-n]
        elif move == "x":
            a, b = [int(n) for n in args.split("/")]
            programs[a], programs[b] = programs[b], programs[a]
        elif move == "p":
            a, b = step[1:].split("/")
            ia = programs.index(a)
            ib = programs.index(b)
            programs[ia], programs[ib] = programs[ib], programs[ia]

    return "".join(programs)


if __name__ == "__main__":
    steps = input().split(",")
    start_value = "".join([chr(c) for c in range(ord("a"), ord("p") + 1)])
    print("part 1:", dance(start_value))

    current = start_value
    for _ in range(1_000_000_000):
        current = dance(current)
    print("part 2:", current)
