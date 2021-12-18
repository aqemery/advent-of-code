def get_multiple(values):
    for i, v in enumerate(values):
        for j, u in enumerate(values, i + 1):
            s = v + u
            if s < 2020:
                last = 2020 - s
                if 2020 - s in values:
                    return v * u * last


values = []
while True:
    try:
        x = int(input())
        values.append(x)
    except EOFError:
        break

print(get_multiple(values))
