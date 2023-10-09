def run_battle(player_Damage, player_Armor):
    boss_hp = 109
    boss_Damage = 8
    boss_Armor = 2
    player_hp = 100
    while player_hp > 0:
        boss_hp -= max(1, player_Damage - boss_Armor)
        if boss_hp <= 0:
            return True
        player_hp -= max(1, boss_Damage - player_Armor)
    else:
        return False


def part1():
    print("player wins", run_battle(4, 7))
    return 40 + 31 + 40


def part2():
    for d in range(4, 13):
        for a in range(1, 10):
            if not run_battle(d, a):
                print(d, a)

    # 7 3

    return 100 + 80 + 8


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
