from collections import defaultdict
from typing import Tuple

from aoc import *

BOTTOM_WALL_X = 0
LEFT_WALL_Y = -1
RIGHT_WALL_Y = 7
MAX_X = 0

gas = read_lines()[0]
figures = [
    [V(0, 0), V(0, 1), V(0, 2), V(0, 3)],
    [V(0, 1), V(1, 0), V(1, 1), V(1, 2), V(2, 1)],
    [V(0, 0), V(0, 1), V(0, 2), V(1, 2), V(2, 2)],
    [V(0, 0), V(1, 0), V(2, 0), V(3, 0)],
    [V(0, 0), V(0, 1), V(1, 0), V(1, 1)]
]
field: dict[V, str] = dict()


def can_move(s: V, figure: list[V], delta: V) -> bool:
    for v in figure:
        cur = s + v + delta
        if cur.y <= LEFT_WALL_Y or cur.y >= RIGHT_WALL_Y:
            return False
        if cur.x <= BOTTOM_WALL_X:
            return False
        if field.get(cur):
            return False
    return True


def cycled(heights_deltas: list[int]) -> Tuple[int, list[int]]:
    def is_valid_len(cycle_len: int) -> bool:
        for i in range(cycle_len):
            x = len(heights_deltas) - cycle_len * 2 + i
            y = len(heights_deltas) - cycle_len + i
            if heights_deltas[x] != heights_deltas[y]:
                return False
        return True

    for cycle_len in range(len(figures) * 5, len(heights_deltas) // len(figures), len(figures)):
        if is_valid_len(cycle_len):
            cycle_deltas = []
            for i in range(cycle_len):
                x = len(heights_deltas) - cycle_len + i
                cycle_deltas.append(heights_deltas[x])
            return cycle_len, cycle_deltas

    return -1, []


rocks_stop_simulation = 100000
time = 0
heights_deltas: list[int] = []

for rock_id in range(rocks_stop_simulation):
    figure = figures[rock_id % len(figures)]
    s = V(MAX_X + 4, 2)
    start = s
    while True:
        delta = V(0, 1 if gas[time % len(gas)] == ">" else -1)
        if can_move(s, figure, delta):
            s = s + delta
        delta = V(-1, 0)
        time += 1
        if not can_move(s, figure, delta):
            break
        s = s + delta

    MAX_X_BEFORE = MAX_X
    for v in figure:
        field[s + v] = "#"
        MAX_X = max(MAX_X, (s + v).x)
    heights_deltas.append(MAX_X - MAX_X_BEFORE)

    if rock_id == 2021:
        print("Part One", MAX_X)

cycle_len, cycle_deltas = cycled(heights_deltas)
assert cycle_len >= 0

full_cycles = (1000000000000 - rocks_stop_simulation) // cycle_len
MAX_X += sum(cycle_deltas) * full_cycles
rocks_stop_simulation += full_cycles * cycle_len

cycle_index = 0
for rock_id in range(rocks_stop_simulation, 1000000000000):
    MAX_X += cycle_deltas[cycle_index % cycle_len]
    cycle_index += 1

print("Part Two", MAX_X)
