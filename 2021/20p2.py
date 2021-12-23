import sys

algo, lines = sys.stdin.read().split("\n\n")


image = [[1 if c == "#" else 0 for c in l] for l in lines.split("\n")]
rev = algo[0] == "#"


def step_range():
    return range(-1, len(image) + 1)


def bounds_value(step):
    if rev and step % 2:
        return "1"
    return "0"


for step in range(50):
    next_image = []
    for y in step_range():
        line = []
        for x in step_range():
            bits = ""
            for i in range(-1, 2):
                for j in range(-1, 2):
                    ax = x + j
                    ay = y + i
                    if ax < 0 or ay < 0:
                        bits += bounds_value(step)
                    else:
                        try:
                            if image[ay][ax]:
                                bits += "1"
                            else:
                                bits += "0"
                        except IndexError:
                            bits += bounds_value(step)
            line.append(int(algo[int(bits, 2)] == "#"))
        next_image.append(line)
    image = next_image

print(sum(lit for l in image for lit in l))
