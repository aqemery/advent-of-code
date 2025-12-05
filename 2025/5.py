import sys


frash_ranges, avalible = sys.stdin.read().split("\n\n")

frash_ranges = [
    (int(a), int(b)) for a, b in (r.split("-") for r in frash_ranges.split("\n"))
]
avalible = [int(a) for a in avalible.split("\n")]

total = 0
for a in avalible:
    for s, e in frash_ranges:
        if s <= a <= e:
            total += 1
            break

print("part 1:", total)

sorted_ranges = sorted(frash_ranges)
new_ranges = []
current_s, current_e = sorted_ranges[0]
for s, e in sorted_ranges[1:]:
    if s <= current_e:
        current_e = max(current_e, e)
    else:
        new_ranges.append((current_s, current_e))
        current_s, current_e = s, e

new_ranges.append((current_s, current_e))
print("part 2:", sum(e - s + 1 for s, e in new_ranges))
