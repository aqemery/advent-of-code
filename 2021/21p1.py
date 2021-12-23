import sys

pos = [int(l.split()[-1]) for l in sys.stdin.read().split("\n")]
score = [0, 0]
num_rolls = 0


while True:
    for i, space in enumerate(pos):
        move = 0
        for _ in range(3):
            move += 1 + num_rolls % 100
            num_rolls += 1

        land = 1 + (space + move - 1) % 10
        pos[i] = land
        score[i] += land
        if score[i] >= 1000:
            print(min(score) * num_rolls)
            quit()
