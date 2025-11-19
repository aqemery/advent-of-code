#!/usr/bin/env python3
"""Advent of Code 2018 Day 24: Immune System Simulator 20XX"""

import re
from copy import deepcopy

def parse_input(filename):
    with open(filename) as f:
        content = f.read().strip()

    immune_section, infection_section = content.split('\n\nInfection:\n')
    immune_section = immune_section.replace('Immune System:\n', '')

    def parse_group(line, army):
        # 4081 units each with 8009 hit points (immune to slashing, radiation; weak to bludgeoning, cold) with an attack that does 17 fire damage at initiative 7
        match = re.match(
            r'(\d+) units each with (\d+) hit points(?: \(([^)]+)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)',
            line
        )

        units = int(match.group(1))
        hp = int(match.group(2))
        modifiers = match.group(3)
        damage = int(match.group(4))
        attack_type = match.group(5)
        initiative = int(match.group(6))

        immunities = set()
        weaknesses = set()

        if modifiers:
            for part in modifiers.split('; '):
                if part.startswith('immune to '):
                    immunities = set(part[10:].split(', '))
                elif part.startswith('weak to '):
                    weaknesses = set(part[8:].split(', '))

        return {
            'army': army,
            'units': units,
            'hp': hp,
            'immunities': immunities,
            'weaknesses': weaknesses,
            'damage': damage,
            'attack_type': attack_type,
            'initiative': initiative
        }

    groups = []
    for line in immune_section.strip().split('\n'):
        groups.append(parse_group(line, 'immune'))
    for line in infection_section.strip().split('\n'):
        groups.append(parse_group(line, 'infection'))

    return groups

def effective_power(group):
    return group['units'] * group['damage']

def damage_to(attacker, defender):
    if attacker['attack_type'] in defender['immunities']:
        return 0
    damage = effective_power(attacker)
    if attacker['attack_type'] in defender['weaknesses']:
        damage *= 2
    return damage

def fight(groups):
    groups = deepcopy(groups)

    while True:
        # Remove dead groups
        groups = [g for g in groups if g['units'] > 0]

        # Check if battle is over
        immune = [g for g in groups if g['army'] == 'immune']
        infection = [g for g in groups if g['army'] == 'infection']

        if not immune or not infection:
            break

        # Target selection phase
        # Sort by effective power (desc), then initiative (desc)
        groups.sort(key=lambda g: (-effective_power(g), -g['initiative']))

        targets = {}  # attacker index -> defender index
        targeted = set()  # defender indices that are already targeted

        for i, attacker in enumerate(groups):
            best_target = None
            best_damage = 0
            best_power = 0
            best_initiative = 0

            for j, defender in enumerate(groups):
                if defender['army'] == attacker['army']:
                    continue
                if j in targeted:
                    continue

                dmg = damage_to(attacker, defender)
                if dmg == 0:
                    continue

                power = effective_power(defender)
                init = defender['initiative']

                if (dmg > best_damage or
                    (dmg == best_damage and power > best_power) or
                    (dmg == best_damage and power == best_power and init > best_initiative)):
                    best_target = j
                    best_damage = dmg
                    best_power = power
                    best_initiative = init

            if best_target is not None:
                targets[i] = best_target
                targeted.add(best_target)

        # Attack phase
        # Sort by initiative (desc)
        attack_order = sorted(range(len(groups)), key=lambda i: -groups[i]['initiative'])

        total_kills = 0
        for i in attack_order:
            if groups[i]['units'] <= 0:
                continue
            if i not in targets:
                continue

            attacker = groups[i]
            defender = groups[targets[i]]

            dmg = damage_to(attacker, defender)
            kills = min(dmg // defender['hp'], defender['units'])
            defender['units'] -= kills
            total_kills += kills

        # Stalemate detection
        if total_kills == 0:
            return None, groups

    # Return winning army and remaining groups
    if immune:
        return 'immune', groups
    else:
        return 'infection', groups

def solve(filename):
    groups = parse_input(filename)

    # Part 1: Run the battle
    winner, remaining = fight(groups)
    part1 = sum(g['units'] for g in remaining if g['units'] > 0)

    # Part 2: Find minimum boost for immune system to win
    boost = 0
    while True:
        boost += 1
        boosted_groups = deepcopy(groups)
        for g in boosted_groups:
            if g['army'] == 'immune':
                g['damage'] += boost

        winner, remaining = fight(boosted_groups)
        if winner == 'immune':
            part2 = sum(g['units'] for g in remaining if g['units'] > 0)
            break

    return part1, part2

if __name__ == '__main__':
    part1, part2 = solve('/Users/adamemery/advent-of-code/2018/input24')
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
