import sys
from math import prod, lcm
from dataclasses import dataclass


@dataclass
class Monkey():
    items: list = None
    operation: str = None
    test: int = None
    p: list = None
    count: int = 0

    def turn(self):
        self.items.append(self.items.popLeft())

    def inspect(self, mult, divide):
        out = []
        for old in self.items:
            self.count += 1
            new = eval(self.operation) // divide % mult
            out.append((new, self.p[new % self.test != 0]))
        self.items = []
        return out

def parseMonkey(data):
    items = [v.split(': ')[-1] for v in data.split('\n')[1:]]
    l = [int(i) for i in items[0].split(', ')]
    o = items[1].split('= ')[-1]
    t, p1, p2  = [int(i.split()[-1]) for i in items[2:]]
    return Monkey(items=l, operation=o, test=t, p=[p1, p2])
        

def solve(data, times, divide=3):
    monkeys = [parseMonkey(d) for d in data]
    mult = lcm(*[m.test for m in monkeys])
    for _ in range(times):
        for m in monkeys:
            pass_to = m.inspect(mult, divide)
            for v, t in pass_to:
                monkeys[t].items.append(v)

    out = [m.count for m in monkeys]
    out = sorted(out)
    return prod(out[-2:])


if __name__ == "__main__":
    data = sys.stdin.read().split("\n\n")
    print("Part 1: ", solve(data, 20))
    print("Part 2: ", solve(data, 10_000, 1))
