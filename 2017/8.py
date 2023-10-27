import sys
from collections import defaultdict

def get_ints(ws):
    return [v for v in  ws.values() if isinstance(v, int)]

if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    ws = defaultdict(int)
    largest = 0
    for line in data:
        var, func, val, _, *code= line.split()

        code = " ".join(code)
        if eval(code, ws):
            if func == "inc":
                ws[var] += int(val)
            else:
                ws[var] -= int(val)

        larger = max(largest, max(get_ints(ws)))
        if larger > largest:
            largest = larger

    print("part 1:", max(get_ints(ws)))
    print("part 2:", largest)
   