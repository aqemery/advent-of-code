from itertools import combinations

def parse(filename):
    with open(filename) as f:
        data = []
        for line in f:
            if line.strip():
                parts = line.strip().replace('@', ',').split(',')
                data.append([int(x.strip()) for x in parts])
        return data

def part1(data):
    min_v = 200000000000000
    max_v = 400000000000000

    total = 0
    for a, b in combinations(data, 2):
        ax, ay, _, avx, avy, _ = a
        bx, by, _, bvx, bvy, _ = b

        # Find intersection of two lines
        # Line a: (ax + t*avx, ay + t*avy)
        # Line b: (bx + s*bvx, by + s*bvy)
        det = avx * (-bvy) - avy * (-bvx)
        if det == 0:
            continue

        t = ((bx - ax) * (-bvy) - (by - ay) * (-bvx)) / det
        s = ((bx - ax) * (-avy) - (by - ay) * (-avx)) / det

        if t < 0 or s < 0:
            continue

        xint = ax + t * avx
        yint = ay + t * avy

        if min_v <= xint <= max_v and min_v <= yint <= max_v:
            total += 1

    return total

def part2(data):
    # Use Z3 solver for the system of equations
    try:
        from z3 import Int, Solver, sat

        x, y, z = Int('x'), Int('y'), Int('z')
        vx, vy, vz = Int('vx'), Int('vy'), Int('vz')

        solver = Solver()

        # For each hailstone, there exists a time t >= 0 where they meet
        for i, (hx, hy, hz, hvx, hvy, hvz) in enumerate(data[:3]):  # Only need 3 hailstones
            t = Int(f't{i}')
            solver.add(t >= 0)
            solver.add(x + vx * t == hx + hvx * t)
            solver.add(y + vy * t == hy + hvy * t)
            solver.add(z + vz * t == hz + hvz * t)

        if solver.check() == sat:
            model = solver.model()
            return model.eval(x + y + z).as_long()
    except ImportError:
        pass

    # Fallback: mathematical approach
    # Find rock velocity by looking for common differences
    from collections import defaultdict

    def find_velocity(pos_vel_pairs, coord_idx):
        # Group hailstones by velocity
        by_vel = defaultdict(list)
        for h in data:
            by_vel[h[3 + coord_idx]].append(h[coord_idx])

        possible = None
        for vel, positions in by_vel.items():
            if len(positions) < 2:
                continue
            positions = sorted(positions)
            for i in range(len(positions) - 1):
                diff = positions[i + 1] - positions[i]
                candidates = set()
                for rv in range(-500, 501):
                    if rv != vel and diff % (rv - vel) == 0:
                        candidates.add(rv)
                if possible is None:
                    possible = candidates
                else:
                    possible &= candidates

        return possible.pop() if possible and len(possible) == 1 else None

    rvx = find_velocity(data, 0)
    rvy = find_velocity(data, 1)
    rvz = find_velocity(data, 2)

    if rvx is None or rvy is None or rvz is None:
        return "Could not solve - install z3-solver"

    # Find position using first two hailstones
    h0 = data[0]
    h1 = data[1]

    # Solve for intersection time
    # h0x + t * h0vx = rx + t * rvx
    # t = (rx - h0x) / (h0vx - rvx)
    ma = (h0[4] - rvy) / (h0[3] - rvx)
    mb = (h1[4] - rvy) / (h1[3] - rvx)
    ca = h0[1] - ma * h0[0]
    cb = h1[1] - mb * h1[0]

    rx = int((cb - ca) / (ma - mb))
    ry = int(ma * rx + ca)
    t = (rx - h0[0]) // (h0[3] - rvx)
    rz = h0[2] + (h0[5] - rvz) * t

    return rx + ry + rz

if __name__ == '__main__':
    data = parse('/Users/adamemery/advent-of-code/2023/input24')
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
