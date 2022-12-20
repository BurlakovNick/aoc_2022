from aoc import *

inp = read(parse=parse_value)
n = len(inp)


def simulate_round(lst):
    for id_ in range(0, n):
        pos = next(i for i, x in enumerate(lst) if x[0] == id_)
        delta = lst[pos][1]
        if delta == 0:
            continue
        x = lst.pop(pos)
        new_pos = (pos + delta) % (n - 1)
        lst.insert(new_pos, x)


def get_answer(lst):
    zero_index = next(i for i, x in enumerate(lst) if x[1] == 0)
    return lst[(zero_index + 1000) % n][1] + lst[(zero_index + 2000) % n][1] + lst[(zero_index + 3000) % n][1]


lst = [(i, x) for i, x in enumerate(inp)]
simulate_round(lst)
print("Part One", get_answer(lst))

lst = [(i, x * 811589153) for i, x in enumerate(inp)]
for _ in range(10):
    simulate_round(lst)

print("Part Two", get_answer(lst))
