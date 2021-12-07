import sys

depths = list(map(int, sys.stdin.readlines()))
threesum = [sum(depths[i:i+3]) for i in range(0,len(depths[:-2]))]
out = [v for i, v in enumerate(threesum) if v > threesum[i-1]]
print(len(out))
