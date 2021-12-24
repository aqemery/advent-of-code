import sys

cubes = set()
for step in sys.stdin.read().split("\n"):
    on = "on" in step
    xr, yr, zr = [list(map(int, s.split("=")[-1].split(".."))) for s in step.split(",")]

    if any([abs(n) > 50 for n in xr + yr + zr]):
        continue

    for x in range(xr[0], xr[1] + 1):
        for y in range(yr[0], yr[1] + 1):
            for z in range(zr[0], zr[1] + 1):
                if on:
                    cubes.add((x, y, z))
                else:
                    try:
                        cubes.remove((x, y, z))
                    except KeyError:
                        pass

print(len(cubes))
