import sys
import math

raw_in = sys.stdin.read()
clean = ["Button A: X+", "Button B: X+", " Y+", "Prize: X=", " Y="]
for c in clean:
    raw_in = raw_in.replace(c, "")


def run(offset=0):
    machines = raw_in.split("\n\n")
    machines = [x.split("\n") for x in machines]
    total = 0
    for a, b, c in machines:
        ax, ay = [int(v) for v in a.split(",")]
        bx, by = [int(v) for v in b.split(",")]
        cx, cy = [int(v) + offset for v in c.split(",")]
        angle_c = math.atan2(cy, cx)
        angle_a = abs(math.atan2(ay, ax) - angle_c)
        angle_b = abs(angle_c - math.atan2(by, bx))
        angle_c = math.pi - angle_a - angle_b
        distance_c = math.sqrt(cx**2 + cy**2)
        distance_b = distance_c * math.sin(angle_a) / math.sin(angle_c)
        distance_a = distance_c * math.sin(angle_b) / math.sin(angle_c)
        a_count = distance_a / math.sqrt(ax**2 + ay**2)
        b_count = distance_b / math.sqrt(bx**2 + by**2)
        a_count = round(a_count, 2)
        b_count = round(b_count, 2)
        if a_count.is_integer() and b_count.is_integer():
            total += int(a_count) * 3 + int(b_count)
    return total


print("part 1:", run())
print("part 2:", run(10000000000000))
