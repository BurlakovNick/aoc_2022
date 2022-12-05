from aoc import *

inp = [
    "BZT",
    "VHTDN",
    "BFMD",
    "TJGWVQL",
    "WDGPVFQM",
    "VZQGHFS",
    "ZSNRLTCW",
    "ZHWDJNRM",
    "MQLFDS"
]
cmds = read()

st = [[y for y in x] for x in inp]
for _, cnt, _, fr, _, to in cmds:
    fr -= 1
    to -= 1
    for _ in range(cnt):
        st[to].append(st[fr].pop())

print("Part One", "".join([x[-1] for x in st]))

st = [[y for y in x] for x in inp]
for _, cnt, _, fr, _, to in cmds:
    fr -= 1
    to -= 1
    st[to].extend(st[fr][-cnt:len(st[fr])])
    for _ in range(cnt):
        st[fr].pop()

print("Part Two", "".join([x[-1] for x in st]))
