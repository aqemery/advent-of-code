import sys
from collections import deque
from math import prod


def next_rule(rule, vars):
    for r in rule[:-1]:
        cond, dest = r.split(":")
        if eval(cond, vars):
            return dest
    return rule[-1]


def part1(rules, values):
    vars = {}
    total = 0
    for part in values:
        current = "in"
        [exec(p, vars) for p in part]
        while True:
            current = next_rule(rules[current], vars)
            if current == "A":
                total += sum(vars[v] for v in "xmas")
                break
            elif current == "R":
                break
    return total


def next_range(ranges, rule, split_char):
    rule_check, next_name = rule.split(":")
    var, val = rule_check.split(split_char)
    index = "xmas".index(var)
    n_min = min(ranges[index][1], int(val))
    n_max = max(ranges[index][0], int(val))
    new_ranges = []
    leftover_ranges = []
    for i, (low, high) in enumerate(ranges):
        if i == index:
            if split_char == "<":
                new_ranges.append((low, n_min - 1))
                leftover_ranges.append((n_min, high))
            else:
                new_ranges.append((n_max + 1, high))
                leftover_ranges.append((low, n_max))
        else:
            new_ranges.append((low, high))
            leftover_ranges.append((low, high))
    ranges = tuple(leftover_ranges)
    return ranges, (next_name, tuple(new_ranges))


def part2(rules):
    total = 0
    q = deque([("in", ((1, 4000),) * 4)])
    while q:
        name, ranges = q.popleft()
        if name == "A":
            total += prod(h - l + 1 for l, h in ranges)
            continue
        if name == "R":
            continue
        for r in rules[name]:
            for c in "<>":
                if c in r:
                    ranges, new_range = next_range(ranges, r, c)
                    q.append(new_range)
                    break
            else:
                q.append((r, ranges))
    return total


if __name__ == "__main__":
    rules, values = sys.stdin.read().split("\n\n")
    rules = rules.replace("{", " ").replace("}", "").replace(",", " ").split("\n")
    rules = {l.split()[0]: l.split()[1:] for l in rules}
    values = values.replace("{", "").replace("}", "").split("\n")
    values = [v.split(",") for v in values]
    print("part 1:", part1(rules, values))
    print("part 2:", part2(rules))
