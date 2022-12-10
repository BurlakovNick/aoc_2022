from aoc import *

inp = read()
total, x, t = 0, 1, 1
field, line = [], ""


def tick():
    global total, t, field, line
    line += "#" if abs(x - len(line)) <= 1 else "."
    if t % 40 == 20:
        total += x * t
    if len(line) == 40:
        field.append(line)
        line = ""
    t += 1


for cmd in inp:
    match cmd:
        case ["noop"]:
            tick()
        case ["addx", dx]:
            tick()
            tick()
            x += dx


print("Part One", total)

print("Part Two")
for line in field:
    print(line)
