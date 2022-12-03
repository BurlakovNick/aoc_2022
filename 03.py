from aoc import *

inp = read_lines()


score = 0
for line in inp:
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    common = (set(a) & set(b)).pop()
    score += char_to_int(common)

print("Part One", score)

score = 0
for a, b, c in batch(inp, 3):
    common = (set(a) & set(b) & set(c)).pop()
    score += char_to_int(common)

print("Part Two", score)
