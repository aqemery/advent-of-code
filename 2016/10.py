import sys
from collections import defaultdict


class Bot:
    def __init__(self):
        self.chips = []
        self.low_num = None
        self.low_dest = None
        self.high_num = None
        self.high_dest = None


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    outputs = defaultdict(list[int])
    bots = defaultdict(Bot)
    for line in data:
        match line.split():
            case ["value", chip, "goes", "to", "bot", bot_num]:
                bot_num = int(bot_num)
                chip = int(chip)
                bots[bot_num].chips.append(chip)

            case [
                "bot",
                bot_num,
                "gives",
                "low",
                "to",
                low_dest,
                low_num,
                "and",
                "high",
                "to",
                high_dest,
                high_num,
            ]:
                bot_num = int(bot_num)
                low_num = int(low_num)
                high_num = int(high_num)
                bot = bots[bot_num]
                bot.low_num = low_num
                bot.low_dest = low_dest
                bot.high_num = high_num
                bot.high_dest = high_dest

    while True:
        for k, b in bots.items():
            if len(b.chips) == 2:
                low, high = sorted(b.chips)
                if low == 17 and high == 61:
                    print("part 1:", k)
                if b.low_dest == "bot":
                    bots[b.low_num].chips.append(low)
                else:
                    outputs[b.low_num].append(low)
                if b.high_dest == "bot":
                    bots[b.high_num].chips.append(high)
                else:
                    outputs[b.high_num].append(high)
                b.chips = []
                break
        else:
            break

    p2 = 1
    for i in range(3):
        p2 *= outputs[i][0]
    print("part 2:", p2)
