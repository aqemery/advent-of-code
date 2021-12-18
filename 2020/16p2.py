import sys
from collections import Counter

fields, ticket, nearby = sys.stdin.read().split("\n\n")

locations = []
for l in fields.split("\n"):
    first = l.split(": ")
    name = first[0]
    ranges = []
    for r in first[1].split(" or "):
        args = list(map(int, r.split("-")))
        ranges += [range(args[0], args[1] + 1)]
    locations.append((name, ranges))

ticket = list(map(int, ticket.split()[-1].split(",")))
nearby = [list(map(int, n.split(","))) for n in nearby.split()[2:]]
valid_tickets = []


def is_valid(n):
    for l in locations:
        if any([n in r for r in l[1]]):
            return True
    return False


valid_tickets = [t for t in nearby if all([is_valid(n) for n in t])]
valid_locations = []
for i in range(len(ticket)):
    col_locations = {l[0] for l in locations}
    col = [t[i] for t in valid_tickets]

    for l in locations:
        for c in col:
            if not any([c in r for r in l[1]]):
                col_locations.remove(l[0])
                break
    valid_locations.append((len(col_locations), i, col_locations))

valid_locations.sort()

out = 1
locations_found = set()
for _, i, l in valid_locations:
    not_found = l - locations_found

    if "departure" in list(not_found)[0]:
        out *= ticket[i]
    locations_found |= not_found

print(out)
