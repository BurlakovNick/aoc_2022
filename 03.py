from aoc import *

inp = read_lines()


score = 0
for line in inp:
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    x = (set(a) & set(b)).pop()
    score += ch_to_int(x)

print("Part One", score)

score = 0
for a, b, c in batch(inp, 3):
    x = (set(a) & set(b) & set(c)).pop()
    score += ch_to_int(x)

print("Part Two", score)
