from collections import defaultdict
from aoc import *

inp = read(trim=[",", "-", ">"])
inp = [[V(x, y) for y, x in batch(line, 2)] for line in inp]
DOWN_DIRECTIONS = [V(1, 0), V(1, -1), V(1, 1)]


def solve(add_bottom: bool):
    field: dict[V, str] = {}
    lowest_rock_x: dict[int, int] = defaultdict(lambda: -1)

    def put_rock(r):
        field[r] = "#"
        lowest_rock_x[r.y] = max(lowest_rock_x[r.y], r.x)

    for line in inp:
        cur = line[0]
        put_rock(cur)
        for target in line:
            direction = (target - cur).dir()
            while cur != target:
                cur += direction
                put_rock(cur)

    if add_bottom:
        bottom = max(lowest_rock_x.values()) + 2
        for y in range(-1000, 2000):
            put_rock(V(bottom, y))

    def fall(v: V):
        while True:
            if field.get(v) is not None or v.x > lowest_rock_x[v.y]:
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
