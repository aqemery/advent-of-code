import sys

search = [2, 3, 4, 7]
lines = [[s.split() for s in l.split('|')] for l in sys.stdin.readlines()] 
print(len([d for _, dg in lines for d in dg if len(d) in search]))
