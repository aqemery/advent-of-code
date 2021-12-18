import sys

print(
    sum(
        [
            len(set.intersection(*map(set, g.split())))
            for g in sys.stdin.read().split("\n\n")
        ]
    )
)
