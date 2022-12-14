from collections import defaultdict
from aoc import *

inp = read(trim=[",", "-", ">"])
inp = [[V(x, y) for y, x in batch(line, 2)] for line in inp]
DOWN_DIRECTIONS = [V(1, 0), V(1, -1), V(1, 1)]


def solve(add_bottom: bool):
    field: dict[V, str] = {}
    for line in inp:
        cur = line[0]
        field[cur] = "#"
        for target in line:
            direction = (target - cur).dir()
            while cur != target:
                cur += direction
                field[cur] = "#"

    bottom = max(v.x for v in field.keys())
    if add_bottom:
        bottom += 2
        for y in range(-1000, 2000):
            field[V(bottom, y)] = "#"

    def fall(v: V):
        while True:
            if field.get(v) is not None or v.x > bottom:
                return None

            direction = next((d for d in DOWN_DIRECTIONS if field.get(v + d) is None), None)
            if not direction:
                return v
            v += direction

    while cur := fall(V(0, 500)):
        field[cur] = "o"

    return sum(1 for v in field.values() if v == "o")


print("Part One", solve(add_bottom=False))
print("Part Two", solve(add_bottom=True))
