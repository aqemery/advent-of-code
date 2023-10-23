from itertools import combinations

def valid(step):
    _, floors = step
    return all(valid_floors(f) for f in floors)
        
    
def valid_floors(floor):
    if len(floor) == 0:
        return True
    
    for item in floor:
        element, element_type = item
        if element_type == "m":
            if element + "g" in floor:
                continue
            else:
                for e, t in floor:
                    if t == "g" and e != element:
                        return False
    return True


# sample

# start = (0,
#     (
#         ("hm", "lm"),
#         ("hg",),
#         ("lg",),
#         (),
#     )
# )

# part 1

# start = (0,
#     (
#         ("pg", "tg", "tm", "qg", "rg", "rm", "cg", "cm"),
#         ("pm", "qm"),
#         (),
#         (),
#     )
# )

# part 2

start = (0,
    (
        ("pg", "tg", "tm", "qg", "rg", "rm", "cg", "cm", "em", "eg", "dm", "dg"),
        ("pm", "qm"),
        (),
        (),
    )
)

states = set([start])

count = 0
while states:
    next_states = set()
    for s in states:
        elevator, floors = s
        current_floor = floors[elevator]
        if elevator > 0:
            # all move down states
            for item in current_floor:
                next_state = [set(f) for f in floors]
                next_state[elevator].remove(item)
                next_state[elevator - 1].add(item)
                next_states.add((elevator - 1, tuple(tuple(f) for f in next_state)))

        if elevator < 3:
            # all move up states
            for a, b in combinations(current_floor, 2):
                next_state = [set(f) for f in floors]
                next_state[elevator].remove(a)
                next_state[elevator].remove(b)
                next_state[elevator + 1].add(a)
                next_state[elevator + 1].add(b)

                next_states.add((elevator + 1, tuple(tuple(f) for f in next_state)))

            # for item in current_floor: # only needed for sample
            #     next_state = [list(f) for f in floors]
            #     next_state[elevator].remove(item)
            #     next_state[elevator + 1].append(item)
            #     next_states.add((elevator + 1, tuple(tuple(f) for f in next_state)))
    count += 1

    next_states = set(s for s in next_states if valid(s))

    for s in next_states:
        elevator, floors = s
        if not floors[0] and not floors[1] and not floors[2]:
            print(count)
            exit()
    states = next_states

