import sys
from collections import Counter

data = sys.stdin.read().split("\n")

word_len = len(data[0])
word_p1 = ""
word_p2 = ""
for i in range(word_len):
    c = Counter([d[i] for d in data])
    word_p1 += c.most_common(1)[0][0]
    word_p2 += c.most_common()[-1][0]


print("part 1:", word_p1)
print("part 2:", word_p2)
