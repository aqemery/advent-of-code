import sys

dots, folds = sys.stdin.read().split("\n\n")
dots = set(tuple(int(c) for c in d.split(",")) for d in dots.split("\n"))

for f in folds.split("\n"):
    v = int(f.split("=")[-1])
    if "x" in f:
        dots = set((i - (i - v) * 2, j) if i >= v else (i, j) for i, j in dots)
    else:
        dots = set((i, j - (j - v) * 2) if j >= v else (i, j) for i, j in dots)
    break

print(len(dots))
