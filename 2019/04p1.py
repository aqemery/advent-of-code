count = 0

for i in range(168630, 718098):
    number = [int(d) for d in str(i)]
    match = True
    for y in range(len(number) - 1):
        if number[y] > number[y + 1]:
            match = False

    if match:
        seen = set()
        for x in number:
            if x not in seen:
                seen.add(x)
            else:
                count += 1
                break

print(count)
