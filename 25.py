from functools import reduce
from itertools import cycle, dropwhile, accumulate
from aoc import *

snafu_to_decimal = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}
snafu_order = ["0", "1", "2", "=", "-"]

print("Part One", next(dropwhile(lambda x: x[0], accumulate(cycle([1]), lambda x, _: ((x[0] - snafu_to_decimal[snafu_order[x[0] % 5]]) // 5, snafu_order[x[0] % 5] + x[1]), initial=((sum(reduce(lambda s, x: s * 5 + snafu_to_decimal[x], line, 0) for line in read_lines())), ""))))[1])
