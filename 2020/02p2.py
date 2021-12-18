count = 0
while True:
    try:
        r, l, p = input().split()
        r_min, r_max = map(int, r.split("-"))
        if (p[r_min - 1] == l[0]) != (p[r_max - 1] == l[0]):
            count += 1
    except EOFError:
        break
print(count)
