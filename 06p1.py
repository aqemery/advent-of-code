import sys


print(sum([len(set(s.replace('\n', ''))) for s in sys.stdin.read().split('\n\n')]))

