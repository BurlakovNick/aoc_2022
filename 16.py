from collections import defaultdict
from functools import cache
from aoc import *

INF = 10000000000000
tunnels: dict[str, list[str]] = {}
valves_with_rate: dict[str, int] = {}
valves_with_rate_index: dict[str, int] = {}
dist: dict[str, dict[str, int]] = {}


inp = read(trim=["Valve", "has flow rate=", ";", "tunnels", "tunnel", "leads to", "lead to ", "valves", "valve", ","])
for line in inp:
    valve = line[0]
    rate = line[1]
    if rate or valve == "AA":
        valves_with_rate_index[valve] = len(valves_with_rate)
        valves_with_rate[valve] = rate
    for to in line[2:]:
        tunnels[valve] = line[2:]

n = len(valves_with_rate)


for x in tunnels.keys():
    dist[x] = {}
    for y in tunnels.keys():
        dist[x][y] = 1000000000

for x, ys in tunnels.items():
    for y in ys:
        dist[x][y] = 1

for k in tunnels.keys():
    for x in tunnels.keys():
        for y in tunnels.keys():
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])


def get_total_rate(mask: int) -> int:
    total = 0
    for valve, rate in valves_with_rate.items():
        index = valves_with_rate_index[valve]
        if (1 << index) & mask:
            total += rate
    return total


# slow af but idk
@cache
def calc(mask: int, pos: str, minutes: int) -> int:
    if minutes == 1 and pos == "AA" and mask == 0:
        return 0
    if minutes <= 1:
        return -INF

    best = -INF
    delta = get_total_rate(mask)

    best = max(best, delta + calc(mask, pos, minutes - 1))

    for new_pos in valves_with_rate.keys():
        best = max(best, delta * dist[pos][new_pos] + calc(mask, new_pos, minutes - dist[pos][new_pos]))

    index = valves_with_rate_index.get(pos)
    if mask & (1 << index):
        best = max(best, delta + calc(mask - (1 << index), pos, minutes - 1))

    return best


def solve():
    best = -1
    for msk in range(0, (1 << n)):
        for pos in valves_with_rate.keys():
            best = max(best, calc(msk, pos, 30))
    return best


def solve_2():
    best = defaultdict(lambda: -INF)
    for msk in range(0, (1 << n)):
        for pos in valves_with_rate.keys():
            best[msk] = max(best[msk], calc(msk, pos, 26))

    answer = -INF
    for msk in range(0, (1 << n)):
        for msk_2 in get_submasks(((1 << n) - 1) - msk):
            answer = max(answer, best[msk] + best[msk_2])
    return answer


ans = measure("part one", solve)
print("Part One", ans)

ans = measure("part two", solve_2)
print("Part two", ans)
