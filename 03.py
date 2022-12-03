from aoc import *

inp = read_lines()

score = 0
for line in inp:
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    ch = (set(a) & set(b)).pop()
    score += (ord(ch) - ord('a') + 1) if 'a' <= ch <= 'z' else (ord(ch) - ord('A') + 27)

print("Part One", score)

score = 0
for a, b, c in batch(inp, 3):
    ch = (set(a) & set(b) & set(c)).pop()
    score += (ord(ch) - ord('a') + 1) if 'a' <= ch <= 'z' else (ord(ch) - ord('A') + 27)

print("Part Two", score)
