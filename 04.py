from aoc import *

inp = read_lines()

sets = []
for line in inp:
    lx, rx, ly, ry = [int(x) for x in re.split(",|-", line)]
    sets.append([set(range(lx, rx + 1)), set(range(ly, ry + 1))])

print("Part One", sum(1 for x, y in sets if x.issuperset(y) or y.issuperset(x)))
print("Part Two", sum(1 for x, y in sets if x & y))
