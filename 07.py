from collections import defaultdict
from functools import *

from aoc import *

inp = read()

path, dirs, i = [""], defaultdict(list), 0
while i < len(inp):
    match inp[i]:
        case ["$", "cd", ".."]:
            path.pop()
        case ["$", "cd", "/"]:
            path = [""]
        case ["$", "cd", dir_name]:
            path.append(dir_name)
        case ["$", "ls"]:
            while i + 1 < len(inp) and inp[i + 1][0] != '$':
                i += 1
                size_or_dir, name = inp[i]
                dirs["/".join(path)].append(size_or_dir if isinstance(size_or_dir, int) else name)
    i += 1


@cache
def get_size(path):
    total = 0
    for item in dirs[path]:
        if isinstance(item, int):
            total += item
        else:
            total += get_size(path + "/" + item)
    return total


sizes = sorted([get_size(x) for x in dirs.keys()])
print("Part One", sum(sz for sz in sizes if sz <= 100000))

target = 30000000 - (70000000 - get_size(""))
print("Part Two", next(sz for sz in sizes if sz >= target))
