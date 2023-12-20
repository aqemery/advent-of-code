import sys
from collections import defaultdict, deque
from itertools import count
from math import lcm
from contextlib import suppress


def solve(data):
    flips = {}
    connections = {}
    conjs = []
    low_pulse = 0
    high_pulse = 0
    
    for line in data:
        source, dest = line.replace(" ", "").split("->")
        dest = dest.split(",")
        if source != "broadcaster":
            t, *source = source
            source = "".join(source)
            if t == "%":
                flips[source] = False
            else:
                conjs.append(source)
        connections[source] = dest

    conj_mem = {c: {s: False for s, d in connections.items() if c in d} for c in conjs}
    find_items = []
    for k, v in connections.items():
        if "rx" in v:
            for k2, v2 in connections.items():
                if k in v2:
                    find_items.append(k2)
    found_values = defaultdict(list)

    for times in count():
        q = deque([("broadcaster", False, "button")])
        while q:
            source, pulse, prev = q.popleft()
            if pulse:
                high_pulse += 1
            else:
                low_pulse += 1
            if source in find_items and not pulse:
                found_values[source].append(times)
                if all(len(v) > 1 for v in found_values.values()):
                    return found_values
            if source == "output":
                continue
            if source in flips:
                if not pulse:
                    flips[source] = not flips[source]
                    for c in connections[source]:
                        q.append((c, flips[source], source))
            elif source in conjs:
                conj_mem[source][prev] = pulse
                signal = True
                if all(conj_mem[source].values()):
                    signal = False
                for c in connections[source]:
                    q.append((c, signal, source))
            else:
                with suppress(KeyError):
                    for c in connections[source]:
                        q.append((c, pulse, source))
        if times == 1000:
            print("part 1:", low_pulse * high_pulse)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    found_valus = solve(d)
    p2 = lcm(*(b - a for a, b in found_valus.values()))
    print("part 2:", p2)
