import sys
from math import prod
from dataclasses import dataclass
import re

check = r"Blueprint (.*): Each ore robot costs (.*) ore. Each clay robot costs (.*) ore. Each obsidian robot costs (.*) ore and (.*) clay. Each geode robot costs (.*) ore and (.*) obsidian."

@dataclass(frozen=True)
class Stash:
    bots: tuple = (1, 0, 0, 0)
    items: tuple = (0, 0, 0, 0)


def solve(data, times):
    totals = []
    for d in data:
        _, ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost = [int(x) for x in re.match(check, d).groups()]

        max_ore_botx = max(clay_cost, obs_ore_cost, geo_ore_cost)
        states = set([Stash()])
        for _ in range(times):
            ns = set()
            for s in states:
                next_items = tuple(a + b for a, b in zip(s.bots, s.items))
                current_ore = s.items[0]
                ns.add(Stash(s.bots, next_items))
                if current_ore >= ore_cost and max_ore_botx > s.bots[0]:
                    ni = tuple(a - b for a, b in zip(next_items, (ore_cost, 0, 0, 0)))
                    nb = tuple(a + b for a, b in zip(s.bots, (1, 0, 0, 0)))
                    ns.add(Stash(nb, ni))
                if current_ore >= clay_cost:
                    ni = tuple(a - b for a, b in zip(next_items, (clay_cost, 0, 0, 0)))
                    nb = tuple(a + b for a, b in zip(s.bots, (0, 1, 0, 0)))
                    ns.add(Stash(nb, ni))
                if current_ore >= obs_ore_cost and s.items[1] >= obs_clay_cost:
                    ni = tuple(a - b for a, b in zip(next_items, (obs_ore_cost, obs_clay_cost, 0, 0)))
                    nb = tuple(a + b for a, b in zip(s.bots, (0, 0, 1, 0)))
                    ns.add(Stash(nb, ni))
                if current_ore >= geo_ore_cost and s.items[2] >= geo_obs_cost:
                    ni = tuple(a - b for a, b in zip(next_items, (geo_ore_cost, 0, geo_obs_cost, 0)))
                    nb = tuple(a + b for a, b in zip(s.bots, (0, 0, 0, 1)))
                    ns.add(Stash(nb, ni))


            mx = max([s.items[3] for s in ns])
            states = set(x for x in ns if x.items[3] >= mx - max_ore_botx)
        mx = max([s.items[3] for s in states])
        totals.append(mx)
    return totals


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", sum((i + 1) * v for i, v in enumerate(solve(d, 24))))
    print("part 2:", prod(solve(d[:3], 32)))
