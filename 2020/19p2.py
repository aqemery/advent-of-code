import sys
import re

r, m = sys.stdin.read().split("\n\n")
rules = r.replace('"', "").split("\n")
messages = m.split("\n")

tree = {}
for r in rules:
    k, v = r.split(": ")
    tree[k] = "+".join(
        ['"' + s + '"' if s == "|" else f'sub("{s}")' for s in v.split()]
    )

depth = 10


def sub(k):
    global depth
    try:
        if k == "8":
            return "(" + sub("42") + "+)"
        elif k == "11" and depth > 0:
            depth -= 1
            return "(" + sub("42") + "(" + sub("11") + "?)" + sub("31") + ")"
        return "(" + eval(tree[k]) + ")"
    except KeyError:
        return k


rex = "^" + eval(tree["0"]) + "$"
print(len([1 for m in messages if re.match(rex, m)]))
