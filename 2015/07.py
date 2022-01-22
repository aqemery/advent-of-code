import sys
from functools import cache

@cache
def val(v):
    if v.isnumeric():
        return int(v)
    else:
        return wires[v]()

def add_line(s):
    match s.split():
        case [source, 'LSHIFT', times, '->', dest]:
            wires[dest] = lambda: val(source) << int(times)
        case [source, 'RSHIFT', times, '->', dest]:
            wires[dest] = lambda: val(source) >> int(times) 
        case [left, 'OR', right, '->', dest]:
            wires[dest] = lambda: val(left) | val(right) 
        case [left, 'AND', right, '->', dest]:
            wires[dest] = lambda: val(left) & val(right)
        case ['NOT', source, '->', dest]:
            wires[dest] = lambda: ~val(source)
        case [source, '->', dest]:
            wires[dest] = lambda: val(source)


if __name__ == "__main__":
    wires = {}
    data = sys.stdin.read().split("\n")
    [add_line(l) for l in data]
    p1 = wires['a']()
    print("part 1:", p1)
    wires['b'] = lambda: val(str(p1))
    val.cache_clear()
    print("part 2:", wires['a']())
