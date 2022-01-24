def solve(data, times):
    for _ in range(times):
        next = ''
        char = data[0]
        count = 1
        for c in data[1:]:
            if c == char:
                count += 1
            else:
                next += f'{count}{char}'
                char = c
                count = 1
        data = next + f'{count}{char}'

    return len(data)


if __name__ == "__main__":
    d = '1321131112'
    print("part 1:", solve(d, 40))
    print("part 2:", solve(d, 50))
