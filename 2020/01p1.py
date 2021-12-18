def get_multiple(values):
    for i, v in enumerate(values):
        for j, u in enumerate(values, i + 1):
            if v + u == 2020:
                return v * u


values = []
while True:
    try:
        x = int(input())
        values.append(x)
    except EOFError:
        break

print(get_multiple(values))
