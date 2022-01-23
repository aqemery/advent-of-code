import sys

data = sys.stdin.read().split("\n")
all_char = sum([len(l) for l in data])
eval_char = sum([len(eval(l)) for l in data])
print("part 1:", all_char - eval_char)
encode_char = sum([2+len(l) + l.count('\\') + l.count('"') for l in data])
print("part 2:", encode_char - all_char)