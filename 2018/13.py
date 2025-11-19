#!/usr/bin/env python3
"""Advent of Code 2018 Day 13: Mine Cart Madness"""

def parse_input(data):
    lines = data.split('\n')
    # Remove trailing empty lines
    while lines and not lines[-1]:
        lines.pop()

    # Pad lines to same length
    max_len = max(len(line) for line in lines)
    grid = [list(line.ljust(max_len)) for line in lines]

    # Find carts and replace with track
    carts = []
    cart_chars = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c in cart_chars:
                dx, dy = cart_chars[c]
                carts.append([x, y, dx, dy, 0])  # x, y, dx, dy, turn_counter

                # Replace cart with underlying track
                if c in '^v':
                    grid[y][x] = '|'
                else:
                    grid[y][x] = '-'

    return grid, carts

def turn_left(dx, dy):
    return (dy, -dx)

def turn_right(dx, dy):
    return (-dy, dx)

def move_cart(cart, grid):
    x, y, dx, dy, turns = cart

    # Move forward
    x += dx
    y += dy

    # Handle track
    c = grid[y][x]

    if c == '+':
        # Intersection: turn left, go straight, turn right
        if turns % 3 == 0:
            dx, dy = turn_left(dx, dy)
        elif turns % 3 == 2:
            dx, dy = turn_right(dx, dy)
        turns += 1
    elif c == '/':
        if dx == 0:  # Moving vertically
            dx, dy = turn_right(dx, dy)
        else:  # Moving horizontally
            dx, dy = turn_left(dx, dy)
    elif c == '\\':
        if dx == 0:  # Moving vertically
            dx, dy = turn_left(dx, dy)
        else:  # Moving horizontally
            dx, dy = turn_right(dx, dy)

    cart[:] = [x, y, dx, dy, turns]

def solve(data):
    grid, carts = parse_input(data)

    first_crash = None

    while len(carts) > 1:
        # Sort carts by position (y, then x)
        carts.sort(key=lambda c: (c[1], c[0]))

        crashed = set()

        for i, cart in enumerate(carts):
            if i in crashed:
                continue

            move_cart(cart, grid)

            # Check for collision
            for j, other in enumerate(carts):
                if i != j and j not in crashed:
                    if cart[0] == other[0] and cart[1] == other[1]:
                        if first_crash is None:
                            first_crash = (cart[0], cart[1])
                        crashed.add(i)
                        crashed.add(j)
                        break

        # Remove crashed carts
        carts = [c for i, c in enumerate(carts) if i not in crashed]

    if carts:
        last_cart = (carts[0][0], carts[0][1])
    else:
        last_cart = None

    return first_crash, last_cart

if __name__ == "__main__":
    with open("/Users/adamemery/advent-of-code/2018/input13") as f:
        data = f.read()

    part1, part2 = solve(data)
    print(f"Part 1: {part1[0]},{part1[1]}")
    print(f"Part 2: {part2[0]},{part2[1]}")
