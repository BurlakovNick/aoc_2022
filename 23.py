from collections import defaultdict
from aoc import *

inp = read_lines()
elves = set()
for x, row in enumerate(inp):
    for y, cell in enumerate(row):
        if cell == "#":
            elves.add(V(x, y))
round = 0

DIRECTIONS_4 = {
    "N": V(-1, 0),
    "S": V(1, 0),
    "W": V(0, -1),
    "E": V(0, 1),
}
DIRECTIONS_8 = DIRECTIONS_4 | {
    name_1 + name_2: DIRECTIONS_4[name_1] + DIRECTIONS_4[name_2] for name_1 in ("N", "S") for name_2 in ("E", "W")
}
MOVE_DIRECTIONS = [
    (("N", "NE", "NW"), "N"),
    (("S", "SE", "SW"), "S"),
    (("W", "NW", "SW"), "W"),
    (("E", "NE", "SE"), "E"),
]


def no_elves(pos: V, dirs) -> bool:
    return all(pos + DIRECTIONS_8[dir] not in elves for dir in dirs)


def get_next_pos(pos: V) -> V:
    if no_elves(pos, DIRECTIONS_8.keys()):
        return pos
    for i in range(4):
        adjacent, dir = MOVE_DIRECTIONS[(round + i) % 4]
        if no_elves(pos, adjacent):
            return pos + DIRECTIONS_8[dir]
    return pos


def simulate() -> set[V] | None:
    candidates = defaultdict(int)
    for elf in elves:
        candidates[get_next_pos(elf)] += 1

    new_elves = set()
    for elf in elves:
        next_pos = get_next_pos(elf)
        if candidates[next_pos] == 1:
            new_elves.add(next_pos)
        else:
            new_elves.add(elf)

    return new_elves if new_elves != elves else None


for round in range(10):
    elves = simulate()

lx, rx = min(v.x for v in elves), max(v.x for v in elves)
ly, ry = min(v.y for v in elves), max(v.y for v in elves)

print("Part One", (rx - lx + 1) * (ry - ly + 1) - len(elves))

for round in range(10, 100000000):
    if not (elves := simulate()):
        print("Part Two", round + 1)
        break
