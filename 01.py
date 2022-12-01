from aoc import *

blocks = read_blocks(parse=parse_value)
sums = sorted(map(sum, blocks), reverse=True)

print("Part One", sums[0])
print("Part Two", sum(sums[:3]))
