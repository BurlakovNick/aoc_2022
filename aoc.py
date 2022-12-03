import os
import re
import sys
import time
from typing import Callable


SAMPLE = False


def force_sample():
    global SAMPLE
    SAMPLE = True


def cells(matrix):
    for x, row in enumerate(matrix):
        for y, v in enumerate(row):
            yield x, y, v


def neighbours8(x: int, y: int, matrix):
    for xx, yy in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                   (x - 1, y), (x + 1, y),
                   (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
        if 0 <= yy < len(matrix) and 0 <= xx < len(matrix[0]):
            yield xx, yy, matrix[yy][xx]


def neighbours4(x: int, y: int, matrix):
    w = len(matrix[0])
    h = len(matrix)
    for xx, yy in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= yy < h and 0 <= xx < w:
            yield xx, yy, matrix[yy][xx]


def measure(name, f):
    start = time.time()
    print(name, f(), time.time() - start)


def maze_dfs(maze, passable, x, y, used=None):
    if used is None:
        used = set()
    used.add((x, y))
    yield x, y
    for xx, yy, value in neighbours4(x, y, maze):
        if (xx, yy) not in used and passable(value):
            used.add((xx, yy))
            yield from maze_dfs(maze, passable, xx, yy, used)


def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1


def transpose(list2):
    return list(map(list, zip(*list2)))


def read_map_ints() -> list[list[int]]:
    return [list(map(int, line)) for line in read_lines()]


def read_map_dict() -> dict[tuple[int, int], int]:
    matrix = read_map_ints()
    return {(x, y): matrix[x][y] for x, y in cells(matrix)}


def read_lines() -> list[str]:
    fn = "inputs/" + (os.path.basename(sys.argv[0])[0:2] if not SAMPLE else "sample")
    fh = open(fn + ".txt", "r")
    try:
        return fh.read().splitlines()
    finally:
        fh.close()


def read(sep: str = None) -> list:
    return [parse_values(line, sep) for line in read_lines()]


def read_blocks(sep: str = None, parse: Callable = None) -> list:
    lines = [parse(line) if parse else parse_values(line, sep) for line in read_lines()]
    blocks = []
    block = []
    for line in lines:
        if not line:
            blocks.append(block)
            block = []
        else:
            block.append(line)
    blocks.append(block)
    return blocks


def parse_values(s: str, sep: str = None):
    parts: list[str] = s.split() if sep is None else re.split(sep, s)
    return [parse_value(item) for item in parts if item != '']


def parse_value(s: str):
    i = try_parse_int(s)
    if i is not None:
        return i
    f = try_parse_float(s)
    if f is not None:
        return f
    return s


def try_parse_int(s: str):
    try:
        return int(s)
    except ValueError:
        return None


def try_parse_float(s: str):
    try:
        return float(s)
    except ValueError:
        return None


def batch(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def ch_to_int(x):
    return (ord(x) - ord('a') + 1) if 'a' <= x <= 'z' else (ord(x) - ord('A') + 27)
