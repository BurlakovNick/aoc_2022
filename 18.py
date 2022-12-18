from queue import Queue
from aoc import *

inp = [V3(x, y, z) for x, y, z in read(trim=",")]

points = set(inp)
ans = 0
for v in inp:
    for v2 in v.neighbors_6():
        if v2 not in points:
            ans += 1

print("Part One", ans)

lx, rx = -10, 30
q = Queue()
steam = {(V3(0, 0, 0))}
q.put(V3(0, 0, 0))
ans = 0
while not q.empty():
    cur: V3 = q.get()
    for to in cur.neighbors_6_in_box(lx, rx, lx, rx, lx, rx):
        if to in points:
            ans += 1
        elif to not in steam:
            steam.add(to)
            q.put(to)

print("Part Two", ans)  # not 542, 2041
