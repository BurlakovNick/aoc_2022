from aoc import *

blocks = read_blocks(parse=parse_value)
sums = sorted(map(sum, blocks), reverse=True)

print("Part One", sums[0])
print("Part Two", sums[0] + sums[1] + sums[2])
