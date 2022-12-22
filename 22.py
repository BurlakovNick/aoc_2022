from collections import defaultdict
from pprint import pprint

from aoc import *

# force_sample()
# cube_size = 4
cube_size = 50

inp = read_lines()

INF = 100000
field = inp[:-2]
cmds = parse_values(inp[-1].replace("R", ",R,").replace("L", ",L,"), sep=",")

n, m = len(field), max(len(row) for row in field)
max_x, max_y = defaultdict(lambda :-INF), defaultdict(lambda :-INF)
min_x, min_y = defaultdict(lambda : INF), defaultdict(lambda : INF)
tiles = {}

for x, row in enumerate(field):
    for y, col in enumerate(row):
        if col in (".", "#"):
            tiles[V(x, y)] = col
            min_x[y] = min(min_x[y], x)
            max_x[y] = max(max_x[y], x)
            min_y[x] = min(min_y[x], y)
            max_y[x] = max(max_y[x], y)

directions = [
    V(0, 1),
    V(1, 0),
    V(0, -1),
    V(-1, 0),
]


def move(pos: V, dir_index: int):
    dir = directions[dir_index]
    new_pos = pos + dir
    if dir.x == 0:
        length = max_y[pos.x] - min_y[pos.x] + 1
        new_pos.y = (new_pos.y - min_y[pos.x]) % length + min_y[pos.x]
    else:
        length = max_x[pos.y] - min_x[pos.y] + 1
        new_pos.x = (new_pos.x - min_x[pos.y]) % length + min_x[pos.y]

    if tiles.get(new_pos) == ".":
        return new_pos
    if tiles.get(new_pos) == "#":
        return pos
    assert False


pos, dir = V(0, min_y[0]), 0
for cmd in cmds:
    if cmd == "L":
        dir = (dir - 1) % len(directions)
    elif cmd == "R":
        dir = (dir + 1) % len(directions)
    else:
        for _ in range(cmd):
            pos = move(pos, dir)

print("Part One", pos, dir)
print("Part One", (pos.x + 1) * 1000 + (pos.y + 1) * 4 + dir)



def get_cube_pos(pos: V):
    return V(pos.x % cube_size, pos.y % cube_size)


def move_2_sample(pos: V, dir_index: int) -> tuple[V, int]:
    def get_cube_side(pos: V):
        if pos.x < cube_size:
            return 0
        if pos.x < cube_size * 2:
            return 1 + pos.y // cube_size
        return 2 + pos.y // cube_size

    def get_cube_side_offset(side: int):
        if side == 0:
            return V(0, 2 * cube_size)
        if side < 4:
            return V(cube_size, (side - 1) * cube_size)
        return V(cube_size * 2, (side - 2) * cube_size)

    cube_side, cube_pos = get_cube_side(pos), get_cube_pos(pos)
    dir = directions[dir_index]
    new_cube_pos = cube_pos + dir
    new_cube_side = cube_side
    new_dir_index = dir_index
    if not all([
        0 <= new_cube_pos.x < cube_size,
        0 <= new_cube_pos.y < cube_size
    ]):
        if cube_side == 0:
            if dir.y > 0:
                new_cube_side = 5
                new_cube_pos = V(cube_size - cube_pos.x - 1, cube_size - 1)
                new_dir_index = 2
            elif dir.y < 0:
                new_cube_side = 2
                new_cube_pos = V(0, cube_pos.x)
                new_dir_index = 1
            elif dir.x > 0:
                new_cube_side = 3
                new_cube_pos = V(0, cube_pos.y)
                new_dir_index = dir_index
            else:
                new_cube_side = 2
                new_cube_pos = V(0, cube_size - cube_pos.y - 1)
                new_dir_index = 1
        elif cube_side == 1:
            if dir.y > 0:
                new_cube_side = 2
                new_cube_pos = V(cube_pos.x, 0)
                new_dir_index = dir_index
            elif dir.y < 0:
                new_cube_side = 5
                new_cube_pos = V(cube_size - 1, cube_size - cube_pos.x - 1)
                new_dir_index = 3
            elif dir.x > 0:
                new_cube_side = 4
                new_cube_pos = V(cube_size - 1, cube_size - cube_pos.y - 1)
                new_dir_index = 3
            else:
                new_cube_side = 0
                new_cube_pos = V(0, cube_size - cube_pos.y - 1)
                new_dir_index = 1
        elif cube_side == 2:
            if dir.y > 0:
                new_cube_side = 3
                new_cube_pos = V(cube_pos.x, 0)
                new_dir_index = dir_index
            elif dir.y < 0:
                new_cube_side = 1
                new_cube_pos = V(cube_pos.x, cube_size - 1)
                new_dir_index = dir_index
            elif dir.x > 0:
                new_cube_side = 4
                new_cube_pos = V(cube_size - cube_pos.x - 1, 0)
                new_dir_index = 0
            else:
                new_cube_side = 0
                new_cube_pos = V(cube_pos.y, 0)
                new_dir_index = 0
        elif cube_side == 3:
            if dir.y > 0:
                new_cube_side = 5
                new_cube_pos = V(0, cube_size - cube_pos.x - 1)
                new_dir_index = 1
            elif dir.y < 0:
                new_cube_side = 2
                new_cube_pos = V(cube_pos.x, cube_size - 1)
                new_dir_index = dir_index
            elif dir.x > 0:
                new_cube_side = 4
                new_cube_pos = V(0, cube_pos.y)
                new_dir_index = dir_index
            else:
                new_cube_side = 0
                new_cube_pos = V(cube_size - 1, cube_pos.y)
                new_dir_index = dir_index
        elif cube_side == 4:
            if dir.y > 0:
                new_cube_side = 5
                new_cube_pos = V(cube_pos.x, 0)
                new_dir_index = dir
            elif dir.y < 0:
                new_cube_side = 2
                new_cube_pos = V(cube_size - 1, cube_size - cube_pos.x - 1)
                new_dir_index = 3
            elif dir.x > 0:
                new_cube_side = 1
                new_cube_pos = V(cube_size - 1, cube_size - cube_pos.y - 1)
                new_dir_index = 3
            else:
                new_cube_side = 3
                new_cube_pos = V(cube_size - 1, cube_pos.y)
                new_dir_index = dir_index
        else:
            if dir.y > 0:
                new_cube_side = 0
                new_cube_pos = V(cube_size - cube_pos.x - 1, cube_size - 1)
                new_dir_index = 2
            elif dir.y < 0:
                new_cube_side = 4
                new_cube_pos = V(cube_pos.x, cube_size - 1)
                new_dir_index = dir_index
            elif dir.x > 0:
                new_cube_side = 1
                new_cube_pos = V(cube_size - cube_pos.y - 1, 0)
                new_dir_index = 0
            else:
                new_cube_side = 3
                new_cube_pos = V(cube_size - cube_pos.y - 1, cube_size - 1)
                new_dir_index = 2

    new_pos = get_cube_side_offset(new_cube_side) + new_cube_pos

    if tiles.get(new_pos) == ".":
        return new_pos, new_dir_index
    if tiles.get(new_pos) == "#":
        return pos, dir_index
    assert False


def move_2_prod(pos: V, dir_index: int) -> tuple[V, int]:
    def get_cube_side(pos: V):
        if pos.x < cube_size:
            return -1 + pos.y // cube_size
        if pos.x < cube_size * 2:
            return 2
        if pos.x < cube_size * 3:
            return 3 + pos.y // cube_size
        return 5

    def get_cube_side_offset(side: int):
        if side < 2:
            return V(0, cube_size * (side + 1))
        if side == 2:
            return V(cube_size, cube_size)
        if side < 5:
            return V(2 * cube_size, cube_size * (side - 3))
        return V(cube_size * 3, 0)

    cube_side, cube_pos = get_cube_side(pos), get_cube_pos(pos)
    dir = directions[dir_index]
    new_cube_pos = cube_pos + dir
    new_cube_side = cube_side
    new_dir_index = dir_index
    if not all([
        0 <= new_cube_pos.x < cube_size,
        0 <= new_cube_pos.y < cube_size
    ]):
        if cube_side == 0:
            if dir.y > 0:
                new_cube_side = 1
                new_cube_pos = V(cube_pos.x, 0)
                new_dir_index = dir_index
            elif dir.y < 0:
                new_cube_side = 3
                new_cube_pos = V(cube_size - cube_pos.x - 1, 0)
                new_dir_index = 0
            elif dir.x > 0:
                new_cube_side = 2
                new_cube_pos = V(0, cube_pos.y)
                new_dir_index = dir_index
            else:
                new_cube_side = 5
                new_cube_pos = V(cube_pos.y, 0)
                new_dir_index = 0
        elif cube_side == 1:
            if dir.y > 0:
                new_cube_side = 4
                new_cube_pos = V(cube_size - cube_pos.x - 1, cube_size - 1)
                new_dir_index = 2
            elif dir.y < 0:
                new_cube_side = 0
                new_cube_pos = V(cube_pos.x, cube_size - 1)
                new_dir_index = dir_index
            elif dir.x > 0:
                new_cube_side = 2
                new_cube_pos = V(cube_pos.y, cube_size - 1)
                new_dir_index = 2
            else:
                new_cube_side = 5
                new_cube_pos = V(cube_size - 1, cube_pos.y)
                new_dir_index = 3
        elif cube_side == 2:
            if dir.y > 0:
                new_cube_side = 1
                new_cube_pos = V(cube_size - 1, cube_pos.x)
                new_dir_index = 3
            elif dir.y < 0:
                new_cube_side = 3
                new_cube_pos = V(0, cube_pos.x)
                new_dir_index = 1
            elif dir.x > 0:
                new_cube_side = 4
                new_cube_pos = V(0, cube_pos.y)
                new_dir_index = dir_index
            else:
                new_cube_side = 0
                new_cube_pos = V(cube_size - 1, cube_pos.y)
                new_dir_index = dir_index
        elif cube_side == 3:
            if dir.y > 0:
                new_cube_side = 4
                new_cube_pos = V(cube_pos.x, 0)
                new_dir_index = dir_index
            elif dir.y < 0:
                new_cube_side = 0
                new_cube_pos = V(cube_size - cube_pos.x - 1, 0)
                new_dir_index = 0
            elif dir.x > 0:
                new_cube_side = 5
                new_cube_pos = V(0, cube_pos.y)
                new_dir_index = dir_index
            else:
                new_cube_side = 2
                new_cube_pos = V(cube_pos.y, 0)
                new_dir_index = 0
        elif cube_side == 4:
            if dir.y > 0:
                new_cube_side = 1
                new_cube_pos = V(cube_size - cube_pos.x - 1, cube_size - 1)
                new_dir_index = 2
            elif dir.y < 0:
                new_cube_side = 3
                new_cube_pos = V(cube_pos.x, cube_size - 1)
                new_dir_index = dir_index
            elif dir.x > 0:
                new_cube_side = 5
                new_cube_pos = V(cube_pos.y, cube_size - 1)
                new_dir_index = 2
            else:
                new_cube_side = 2
                new_cube_pos = V(cube_size - 1, cube_pos.y)
                new_dir_index = dir_index
        else:
            if dir.y > 0:
                new_cube_side = 4
                new_cube_pos = V(cube_size - 1, cube_pos.x)
                new_dir_index = 3
            elif dir.y < 0:
                new_cube_side = 0
                new_cube_pos = V(0, cube_pos.x)
                new_dir_index = 1
            elif dir.x > 0:
                new_cube_side = 1
                new_cube_pos = V(0, cube_pos.y)
                new_dir_index = 1
            else:
                new_cube_side = 3
                new_cube_pos = V(cube_size - 1, cube_pos.y)
                new_dir_index = dir_index

    new_pos = get_cube_side_offset(new_cube_side) + new_cube_pos

    if tiles.get(new_pos) == ".":
        return new_pos, new_dir_index
    if tiles.get(new_pos) == "#":
        return pos, dir_index
    assert False


pos, dir = V(0, min_y[0]), 0
for cmd in cmds:
    if cmd == "L":
        dir = (dir - 1) % len(directions)
    elif cmd == "R":
        dir = (dir + 1) % len(directions)
    else:
        for _ in range(cmd):
            move_func = move_2_prod if cube_size == 50 else move_2_sample
            pos, dir = move_func(pos, dir)

print("Part Two", pos, dir)
print("Part Two", (pos.x + 1) * 1000 + (pos.y + 1) * 4 + dir)
