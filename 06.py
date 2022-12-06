from aoc import *


inp = read_lines()[0]


def solve(cnt):
    return next(
        end
        for end in range(cnt, len(inp) + 1)
        if len(set(inp[end - cnt:end])) == cnt
    )


print("Part One", solve(4))
print("Part Two", solve(14))
