from functools import cmp_to_key
from aoc import *


def get_line(s):
    if s == "":
        return None
    return eval(s)


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return sign(left - right)

    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])

    for x, y in zip(left, right):
        if cmp := compare(x, y):
            return cmp
    return sign(len(left) - len(right))


inp = read_blocks(parse=get_line)

result = 0
for idx, (left, right) in enumerate(inp):
    if compare(left, right) < 0:
        result += idx + 1


print("Part One", result)

inp = [*flatten(inp), [[2]], [[6]]]
inp = sorted(inp, key=cmp_to_key(compare))

x = inp.index([[2]]) + 1
y = inp.index([[6]]) + 1

print("Part Two", x * y)
