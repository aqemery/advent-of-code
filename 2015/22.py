from dataclasses import dataclass
import random


class YoureAWizardHarry:
    def __init__(self):
        self.hp = 50
        self.mana = 500
        self.effects = {}
        self.spent = 0
        self.armor = 0

    def pay_mana(self, cost):
        self.mana -= cost
        self.spent += cost

    def cast(self, spell, boss):
        if spell == "magic_missile":
            self.pay_mana(53)
            boss.hp -= 4
        elif spell == "drain":
            self.pay_mana(73)
            boss.hp -= 2
            self.hp += 2
        elif spell == "shield":
            self.pay_mana(113)
            self.effects["shield"] = 6
        elif spell == "poison":
            self.pay_mana(173)
            self.effects["poison"] = 6
        elif spell == "recharge":
            self.pay_mana(229)
            self.effects["recharge"] = 5

    def take_damage(self, damage):
        self.hp -= max(1, damage - self.armor)

    def tick(self, boss):
        self.armor = 0
        if "poison" in self.effects:
            boss.hp -= 3
        if "recharge" in self.effects:
            self.mana += 101
        if "shield" in self.effects:
            self.armor = 7
        self.effects = {k: v - 1 for k, v in self.effects.items() if v > 1}


@dataclass
class Boss:
    hp: int = 58
    damage: int = 9


spells = ["magic_missile", "drain", "shield", "poison", "recharge"]


def run_battle(player, hard):
    boss = Boss()

    while player.hp > 0:
        player.tick(boss)
        if hard:
            player.take_damage(1)
            if player.hp <= 0:
                return False

        if boss.hp <= 0:
            return True

        spell = random.choice(spells)
        while spell in player.effects:
            spell = random.choice(spells)
        player.cast(spell, boss)

        if player.mana < 0:
            return False

        if boss.hp <= 0:
            return True

        player.tick(boss)
        player.take_damage(boss.damage)

    return False


def solve(hard=False, runs=100_000):
    spent = []
    for _ in range(runs):
        player = YoureAWizardHarry()
        if run_battle(player, hard):
            spent.append(player.spent)

    return min(spent)


if __name__ == "__main__":
    print("part 1:", solve())
    print("part 2:", solve(hard=True, runs=500_000))
