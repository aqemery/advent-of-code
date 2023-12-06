from math import prod


def race(t):
    for hold in range(t + 1):
        yield (t - hold) * hold


if __name__ == "__main__":
    times = input().split()[1:]
    records = input().split()[1:]

    races = zip(map(int, times), map(int, records))
    p1 = prod(len([dist for dist in race(t) if dist > r]) for t, r in races)
    print("part 1:", p1)

    one_time = int("".join(times))
    one_record = int("".join(records))
    p2 = len([d for d in race(one_time) if d > one_record])
    print("part 2:", p2)
