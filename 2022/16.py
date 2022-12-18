import sys
from collections import deque
import re


def next_options(tunnels, valves_left, current, time_left):
    valves_off = valves_left.copy()
    visited = set()
    q = deque([(current, time_left)])
    found = []
    while q:
        current, time = q.popleft()
        if current in visited or time - 1 == 0:
            continue

        visited.add(current)
        for t in tunnels[current]:
            q.append((t, time - 1))

        if current in valves_off:
            valves_off.remove(current)
            nt = time - 1
            vl = valves_left.copy()
            vl.remove(current)
            found.append((flows[current] * nt, current, nt, vl))

    return found


def part1(tunnels, flows):
    q = deque([("AA", 30, set(flows.keys()), 0)])
    pressures = []
    while q:
        current, time_left, valves_left, total = q.popleft()
        for no in next_options(tunnels, valves_left, current, time_left):
            score, c, tl, vl = no
            q.append((c, tl, vl, total + score))
        else:
            pressures.append(total)

    return max(pressures)


def part2(tunnels, flows):
    start = ("AA", 26)
    q = deque([((start, start), set(flows.keys()), 0)])
    pressure = 0
    while q:
        pos, valves_left, total = q.popleft()
        for i, p in enumerate(pos):
            current, time_left = list(p)
            for no in next_options(tunnels, valves_left, current, time_left):
                score, c, tl, vl = no
                new_pos = list(pos)
                new_pos[i] = (c, tl)
                max_p = max([flows[v] for v in vl]) * (tl - 1)
                if max_p + total + score > pressure:
                    q.append((tuple(new_pos), vl, total + score))
            else:
                if pressure < total:
                    pressure = total
    return pressure


if __name__ == "__main__":
    data = sys.stdin.read()
    data = data.replace("tunnel leads to valve", "tunnels lead to valves")
    data = data.split("\n")
    check = r"Valve (.*) has flow rate=(.*); tunnels lead to valves (.*)"
    tunnels = {}
    flows = {}
    for d in data:
        t, f, to = re.match(check, d).groups()
        flow = int(f)
        if flow > 0:
            flows[t] = flow
        tunnels[t] = to.split(", ")

    print("part 1:", part1(tunnels, flows))
    # print("part 2:", part2(tunnels, flows))
