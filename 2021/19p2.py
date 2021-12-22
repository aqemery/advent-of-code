import sys
from collections import Counter, deque
from itertools import combinations


scanners = [
    list(tuple(map(int, s.split(","))) for s in scan.split("\n")[1:])
    for scan in sys.stdin.read().split("\n\n")
]

rotations = {
    0: lambda x, y, z: (x, y, z),
    1: lambda x, y, z: (x, -z, y),
    2: lambda x, y, z: (x, -y, -z),
    3: lambda x, y, z: (x, z, -y),
    4: lambda x, y, z: (-x, -y, z),
    5: lambda x, y, z: (-x, -z, -y),
    6: lambda x, y, z: (-x, y, -z),
    7: lambda x, y, z: (-x, z, y),
    8: lambda x, y, z: (y, -x, z),
    9: lambda x, y, z: (y, -z, -x),
    10: lambda x, y, z: (y, x, -z),
    11: lambda x, y, z: (y, z, x),
    12: lambda x, y, z: (-y, x, z),
    13: lambda x, y, z: (-y, -z, x),
    14: lambda x, y, z: (-y, -x, -z),
    15: lambda x, y, z: (-y, z, -x),
    16: lambda x, y, z: (z, y, -x),
    17: lambda x, y, z: (z, x, y),
    18: lambda x, y, z: (z, -y, x),
    19: lambda x, y, z: (z, -x, -y),
    20: lambda x, y, z: (-z, x, -y),
    21: lambda x, y, z: (-z, y, x),
    22: lambda x, y, z: (-z, -x, y),
    23: lambda x, y, z: (-z, -y, -x),
}


def find_relative_scanner(scan):
    for k in scanner_locations.keys():
        for rot in rotations.values():
            counts = Counter()
            rot_scanner = set(rot(*v) for v in scan)
            for s in rot_scanner:
                for b in scanners[k]:
                    found = tuple(i - j for i, j in zip(b, s))
                    counts[found] += 1

            offset, ocurrance = counts.most_common()[0]
            if ocurrance >= 12:
                vecs = [tuple(i + j for i, j in zip(s, offset)) for s in rot_scanner]
                return offset, vecs


scanner_locations = {0: (0, 0, 0)}

beacons = Counter(scanners[0])
q = deque(range(1, len(scanners)))
while q:
    index = q.popleft()
    if pos := find_relative_scanner(scanners[index]):
        scanner_locations[index] = pos[0]
        beacons.update(pos[1])
        scanners[index] = pos[1]
    else:
        q.append(index)

print(len(beacons))

print(max(sum([abs(j-i) for i,j in zip(s1,s2)]) for s1, s2 in combinations(scanner_locations.values(), 2)))
