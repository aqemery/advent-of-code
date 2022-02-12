import re
import json


def step(data):
    match data:
        case list():
            return sum(step(x) for x in data)
        case dict():
            vals = data.values()
            if "red" in vals:
                return 0
            return sum(step(x) for x in vals)
        case int():
            return data
        case _:
            return 0


if __name__ == "__main__":
    d = input()
    print("part 1:", sum(int(x) for x in re.findall("-?\d+", d)))
    d = json.loads(d)
    print("part 2:", step(d))
