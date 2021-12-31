def get_input():
    dimensions = input().split(",")[-2:]
    return [map(int, dem.split("=")[1].split("..")) for dem in dimensions]


def step(vx, vy):
    x, y = 0, 0
    while vx > 0:
        x += vx
        y += vy
        vx -= 1
        vy -= 1
        yield x, y
    while True:
        y += vy
        vy -= 1
        yield x, y


def main():
    rx, ry = get_input()
    lx, mx = rx
    ly, my = ry

    found = set()
    for vx in range(1, mx + 1):
        for vy in range(ly, -ly + 1):
            for x, y in step(vx, vy):
                if y < ly:
                    break
                if ly <= y <= my and mx >= x >= lx:
                    found.add((vx, vy))
    print(len(found))


if __name__ == "__main__":
    main()
