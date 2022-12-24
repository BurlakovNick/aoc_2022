from collections import defaultdict
from queue import Queue
from aoc import *

inp = read_lines()
dirs = {">": V(0, 1), "<": V(0, -1), "v": V(1, 0), "^": V(-1, 0)}
blizzards_x, blizzards_y = defaultdict(list), defaultdict(list)
n = len(inp) - 2
m = len(inp[0]) - 2
START, FINISH = V(-1, 0), V(n, m - 1)

for x, row in enumerate(inp[1:-1]):
    for y, cell in enumerate(row[1:-1]):
        if cell == ".":
            continue
        blizzard = (V(x, y), dirs[cell])
        if dirs[cell].x == 0:
            blizzards_x[x].append(blizzard)
        else:
            blizzards_y[y].append(blizzard)


def has_blizzard(pos: V, time: int) -> bool:
    for v, dir in [*blizzards_x[pos.x], *blizzards_y[pos.y]]:
        nx = (v.x + dir.x * time) % n
        ny = (v.y + dir.y * time) % m
        if pos == V(nx, ny):
            return True
    return False


def bfs(start, finish, start_time) -> int:
    q = Queue()
    visited = set()

    def add_to_queue(v):
        if v not in visited:
            q.put(v)
            visited.add(v)

    add_to_queue((start, start_time))

    while not q.empty():
        pos, time = q.get()
        if pos == finish:
            return time

        for to in pos.neighbors_4():
            in_box = (0 <= to.x < n and 0 <= to.y < m) or to == finish
            if in_box and not has_blizzard(to, time + 1):
                add_to_queue((to, time + 1))

        if not has_blizzard(pos, time + 1):
            add_to_queue((pos, time + 1))


time_1 = measure("one", lambda: bfs(START, FINISH, 0))
time_2 = measure("two", lambda: bfs(FINISH, START, time_1))
time_3 = measure("three", lambda: bfs(START, FINISH, time_2))

print("Part One", time_1)
print("Part Two", time_3)
