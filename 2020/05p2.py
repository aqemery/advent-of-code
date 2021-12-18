import sys

bi = {"B": "1", "F": "0", "L": "0", "R": "1"}
seats = ["".join(bi[c] for c in l) for l in sys.stdin.read().split()]
ids = [int(s[:7], 2) * 8 + int(s[7:], 2) for s in seats]
ids.sort()
last = ids[0]
for i in ids[1:]:
    if i > last + 1:
        print(last + 1)
    last = i
