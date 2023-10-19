import sys

screen_x = 50
screen_y = 6


def print_screen(pixels):
    for y in range(screen_y):
        for x in range(screen_x):
            if (x, y) in pixels:
                print("#", end="")
            else:
                print(".", end="")
        print()


data = sys.stdin.read().split("\n")
pixels = set()
for line in data:
    op = line.split()
    match op:
        case ["rect", demensions]:
            dx, dy = [int(d) for d in demensions.split("x")]
            for y in range(dy):
                for x in range(dx):
                    pixels.add((x, y))
        case ["rotate", "column", col, "by", shift]:
            col_index = int(col.split("=")[1])
            shift_amount = int(shift)

            on = set()
            for y in range(screen_y):
                if (col_index, y) in pixels:
                    pixels.remove((col_index, y))
                    on.add((col_index, y))

            for x, y in on:
                pixels.add((x, (y + shift_amount) % screen_y))

        case ["rotate", "row", row, "by", shift]:
            row_index = int(row.split("=")[1])
            shift_amount = int(shift)

            on = set()
            for x in range(screen_x):
                if (x, row_index) in pixels:
                    pixels.remove((x, row_index))
                    on.add((x, row_index))

            for x, y in on:
                pixels.add(((x + shift_amount) % screen_x, y))


print("part 1:", len(pixels))
print("part 2:")
for y in range(screen_y):
    for x in range(screen_x):
        if (x, y) in pixels:
            print("#", end="")
        else:
            print(" ", end="")
    print()
