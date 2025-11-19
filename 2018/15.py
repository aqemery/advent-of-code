#!/usr/bin/env python3
"""Advent of Code 2018 Day 15: Beverage Bandits"""

from collections import deque

def parse_input(data):
    lines = data.strip().split('\n')
    grid = [list(line) for line in lines]
    return grid

def find_units(grid):
    units = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c in 'EG':
                units.append({'type': c, 'x': x, 'y': y, 'hp': 200, 'attack': 3})
    return units

def get_adjacent(x, y):
    """Return adjacent squares in reading order (up, left, right, down)"""
    return [(x, y-1), (x-1, y), (x+1, y), (y, x+1)]

def in_range_squares(grid, units, enemy_type):
    """Find all open squares adjacent to enemies"""
    squares = set()
    for unit in units:
        if unit['type'] == enemy_type and unit['hp'] > 0:
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx, ny = unit['x'] + dx, unit['y'] + dy
                if grid[ny][nx] == '.':
                    squares.add((nx, ny))
    return squares

def bfs_shortest_path(grid, start_x, start_y, targets, units):
    """BFS to find shortest path to any target"""
    if not targets:
        return None, None

    if (start_x, start_y) in targets:
        return 0, (start_x, start_y)

    # Get positions of all units
    unit_positions = {(u['x'], u['y']) for u in units if u['hp'] > 0}
    unit_positions.discard((start_x, start_y))

    visited = {(start_x, start_y)}
    queue = deque()

    # Add initial moves in reading order
    for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        nx, ny = start_x + dx, start_y + dy
        if grid[ny][nx] == '.' and (nx, ny) not in unit_positions:
            queue.append((nx, ny, 1, (nx, ny)))  # pos_x, pos_y, distance, first_step
            visited.add((nx, ny))

    # Find all shortest paths
    found_dist = None
    found_targets = []

    while queue:
        x, y, dist, first_step = queue.popleft()

        if found_dist is not None and dist > found_dist:
            break

        if (x, y) in targets:
            found_dist = dist
            found_targets.append((x, y, first_step))
            continue

        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and grid[ny][nx] == '.' and (nx, ny) not in unit_positions:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1, first_step))

    if not found_targets:
        return None, None

    # Choose target in reading order, then first step in reading order
    found_targets.sort(key=lambda t: (t[1], t[0]))  # Sort by y, then x for target
    target = (found_targets[0][0], found_targets[0][1])

    # Get all first steps that lead to this target
    first_steps = [t[2] for t in found_targets if (t[0], t[1]) == target]
    first_steps.sort(key=lambda s: (s[1], s[0]))  # Sort by y, then x

    return found_dist, first_steps[0]

def simulate_combat(grid, elf_attack=3, stop_on_elf_death=False):
    grid = [row[:] for row in grid]  # Deep copy
    units = find_units(grid)

    # Set elf attack power
    for unit in units:
        if unit['type'] == 'E':
            unit['attack'] = elf_attack

    initial_elves = sum(1 for u in units if u['type'] == 'E')

    rounds = 0

    while True:
        # Sort units by reading order
        units.sort(key=lambda u: (u['y'], u['x']))

        for unit in units:
            if unit['hp'] <= 0:
                continue

            # Identify targets
            enemy_type = 'G' if unit['type'] == 'E' else 'E'
            enemies = [u for u in units if u['type'] == enemy_type and u['hp'] > 0]

            if not enemies:
                # Combat ends
                total_hp = sum(u['hp'] for u in units if u['hp'] > 0)
                return rounds * total_hp, sum(1 for u in units if u['type'] == 'E' and u['hp'] > 0) == initial_elves

            # Check if already in range to attack
            adjacent_enemies = []
            for enemy in enemies:
                if abs(unit['x'] - enemy['x']) + abs(unit['y'] - enemy['y']) == 1:
                    adjacent_enemies.append(enemy)

            # If not in range, move
            if not adjacent_enemies:
                # Find target squares (open squares adjacent to enemies)
                targets = in_range_squares(grid, units, enemy_type)

                if targets:
                    dist, next_step = bfs_shortest_path(grid, unit['x'], unit['y'], targets, units)

                    if next_step:
                        # Move
                        grid[unit['y']][unit['x']] = '.'
                        unit['x'], unit['y'] = next_step
                        grid[unit['y']][unit['x']] = unit['type']

                        # Recheck for adjacent enemies after moving
                        adjacent_enemies = []
                        for enemy in enemies:
                            if abs(unit['x'] - enemy['x']) + abs(unit['y'] - enemy['y']) == 1:
                                adjacent_enemies.append(enemy)

            # Attack if in range
            if adjacent_enemies:
                # Choose target with lowest HP, ties broken by reading order
                adjacent_enemies.sort(key=lambda e: (e['hp'], e['y'], e['x']))
                target = adjacent_enemies[0]
                target['hp'] -= unit['attack']

                if target['hp'] <= 0:
                    grid[target['y']][target['x']] = '.'

                    if stop_on_elf_death and target['type'] == 'E':
                        return 0, False

        rounds += 1

def solve(data):
    grid = parse_input(data)

    # Part 1: Regular combat
    part1, _ = simulate_combat(grid)

    # Part 2: Find minimum elf attack where no elves die
    elf_attack = 4
    while True:
        result, no_elf_deaths = simulate_combat(grid, elf_attack, stop_on_elf_death=True)
        if no_elf_deaths:
            part2 = result
            break
        elf_attack += 1

    return part1, part2

if __name__ == "__main__":
    with open("/Users/adamemery/advent-of-code/2018/input15") as f:
        data = f.read()

    part1, part2 = solve(data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
