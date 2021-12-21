import sys
from collections import Counter, deque


scanners = [
    list(tuple(map(int, s.split(","))) for s in scan.split("\n")[1:])
    for scan in sys.stdin.read().split("\n\n")
]

axis_map = {
    0: lambda x, y, z: (x, -z, y),
    1: lambda x, y, z: (z, y, -x),
    2: lambda x, y, z: (-y, x, z),
}
axis = [a % 3 for a in range(24)]


def find_relative_scanner(rot_scanner):
    for k in scanner_locations.keys():
        for a in axis:
            counts = Counter()
            rot_scanner = set(axis_map[a](*v) for v in rot_scanner)
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
        print(scanner_locations)
    else:
        print(index)
        q.append(index)

print(len(beacons))
