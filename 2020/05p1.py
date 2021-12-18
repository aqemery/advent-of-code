import sys

bi = {"B": "1", "F": "0", "L": "0", "R": "1"}
greatest = max(["".join(bi[c] for c in l) for l in sys.stdin.read().split()])
row = int(greatest[:7], 2)
col = int(greatest[7:], 2)
print(row * 8 + col)
