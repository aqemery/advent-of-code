directions = {
    "n": (0, 1),
    "ne": (-.5, .5),
    "nw": (.5, .5),
    "s": (0, -1),
    "se": (-.5, -.5),
    "sw": (.5, -.5),
}


def get_steps(x, y):
    x = abs(x)
    y = abs(y)
   
    x_steps = x // .5
    y_steps = abs(abs(y) - x)

    return int(x_steps + y_steps)

if __name__ == "__main__":
    d = input()
    max_steps = 0
    x, y = 0, 0
    for direction in d.split(","):
        dx, dy = directions[direction]
        x += dx
        y += dy
        steps = get_steps(x, y)
        if steps > max_steps:
            max_steps = steps


    print("part 1:", steps)
    print("part 2:", max_steps)