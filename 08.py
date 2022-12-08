from itertools import takewhile, count

from aoc import *

trees = read_map_ints()
transposed_trees = transpose(trees)
n, m = len(trees), len(trees[0])


def is_visible(x, y):
    def all_visible(lst):
        return all(h < trees[x][y] for h in lst)

    return any([
        all_visible(trees[x][0:y]),
        all_visible(trees[x][y + 1:]),
        all_visible(transposed_trees[y][0:x]),
        all_visible(transposed_trees[y][x + 1:]),
    ])


print("Part One", sum(1 for x in range(n) for y in range(m) if is_visible(x, y)))


def scenic(x, y):
    def viewing_dist(lst):
        dist = sum(1 for _ in takewhile(lambda h: h < trees[x][y], lst))
        return dist + int(dist < len(lst))

    return (
        viewing_dist(list(reversed(trees[x][0:y]))) *
        viewing_dist(trees[x][y + 1:]) *
        viewing_dist(list(reversed(transposed_trees[y][0:x]))) *
        viewing_dist(transposed_trees[y][x + 1:])
    )


print("Part Two", max(scenic(x, y) for x in range(n) for y in range(m)))
