import re
from collections import defaultdict


def parse(filename):
    particles = []
    with open(filename) as f:
        for line in f:
            nums = list(map(int, re.findall(r'-?\d+', line)))
            p = (nums[0], nums[1], nums[2])
            v = (nums[3], nums[4], nums[5])
            a = (nums[6], nums[7], nums[8])
            particles.append([p, v, a])
    return particles


def manhattan(vec):
    return abs(vec[0]) + abs(vec[1]) + abs(vec[2])


def part1(particles):
    # Simulate to find which particle stays closest long-term
    # Deep copy particles
    particles = [[list(p), list(v), list(a)] for p, v, a in particles]

    # Run simulation for many ticks
    for _ in range(1000):
        for p, v, a in particles:
            v[0] += a[0]
            v[1] += a[1]
            v[2] += a[2]
            p[0] += v[0]
            p[1] += v[1]
            p[2] += v[2]

    # Find closest to origin
    closest = min(
        range(len(particles)),
        key=lambda i: manhattan(particles[i][0])
    )
    return closest


def part2(particles):
    # Deep copy particles
    particles = [[list(p), list(v), list(a)] for p, v, a in particles]

    # Run simulation until no collisions for a while
    no_collision_count = 0

    while no_collision_count < 50:  # If no collisions for 50 ticks, we're done
        # Update velocities and positions
        for p, v, a in particles:
            v[0] += a[0]
            v[1] += a[1]
            v[2] += a[2]
            p[0] += v[0]
            p[1] += v[1]
            p[2] += v[2]

        # Find collisions
        positions = defaultdict(list)
        for i, (p, v, a) in enumerate(particles):
            positions[tuple(p)].append(i)

        # Remove colliding particles
        to_remove = set()
        for pos, indices in positions.items():
            if len(indices) > 1:
                to_remove.update(indices)

        if to_remove:
            particles = [p for i, p in enumerate(particles) if i not in to_remove]
            no_collision_count = 0
        else:
            no_collision_count += 1

    return len(particles)


if __name__ == '__main__':
    particles = parse('2017/input')

    print(f"Part 1: {part1(particles)}")
    print(f"Part 2: {part2(particles)}")
