from queue import Queue

from aoc import *


inp = read_lines()

n, m = len(inp), len(inp[0])
field = {V(x, y): val for x, y, val in cells(inp)}
start = next(V(x, y) for x, y, val in cells(inp) if val == "S")
finish = next(V(x, y) for x, y, val in cells(inp) if val == "E")


def get_level(v):
    if v == "S":
        return ch_to_int("a")
    if v == "E":
        return ch_to_int("z")
    return ch_to_int(v)


def bfs(start_points):
    q = Queue()
    dist = {}

    for v in start_points:
        q.put(v)
        dist[v] = 0

    while not q.empty():
        _from: V = q.get()
        for to in _from.neighbors_4_in_box(n, m):
            if get_level(field[to]) <= 1 + get_level(field[_from]) and dist.get(to) is None:
                dist[to] = dist[_from] + 1
                q.put(to)
    return dist[finish]


print("Part One", bfs([start]))
print("Part One", bfs([V(x, y) for x, y, val in cells(inp) if get_level(val) == 1]))
