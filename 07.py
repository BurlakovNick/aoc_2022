from collections import defaultdict
from functools import *
from aoc import *

inp = read()

path, dirs = [""], defaultdict(list)
for cmd in inp:
    match cmd:
        case ["$", "cd", ".."]:
            path.pop()
        case ["$", "cd", "/"]:
            path = [""]
        case ["$", "cd", dir_name]:
            path.append(dir_name)
        case ["$", "ls"]:
            pass
        case ["dir", name]:
            dirs["/".join(path)].append(name)
        case [size, _]:
            dirs["/".join(path)].append(size)


@cache
def get_size(path):
    def size(x):
        return x if isinstance(x, int) else get_size(path + "/" + x)
    return sum(size(x) for x in dirs[path])


sizes = sorted([get_size(x) for x in dirs.keys()])
print("Part One", sum(sz for sz in sizes if sz <= 100000))

target = 30000000 - (70000000 - get_size(""))
print("Part Two", next(sz for sz in sizes if sz >= target))
