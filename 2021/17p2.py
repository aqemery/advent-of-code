dimensions = input().split(",")[-2:]
rx, ry = [map(int, dem.split("=")[1].split("..")) for dem in dimensions]
lx, mx = rx
ly, my = ry


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


found = set()
for vx in range(1, mx + 1):
    for vy in range(ly, -ly + 1):
        for x, y in step(vx, vy):
            if y < ly:
                break
            if ly <= y <= my and mx >= x >= lx:
                found.add((vx, vy))

print(len(found))
