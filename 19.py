from collections import defaultdict
from functools import cache
from aoc import *

# force_sample()

inp = [[x for x in line if isinstance(x, int)] for line in read(trim=":")]

blueprints = {}
robots_limit = {}
for line in inp:
    id_, ore, clay, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = line
    blueprints[id_ - 1] = [
        (ore, 0, 0),
        (clay, 0, 0),
        (obsidian_ore, obsidian_clay, 0),
        (geode_ore, 0, geode_obsidian),
    ]
    robots_limit[id_ - 1] = (max(ore, clay, obsidian_ore, geode_ore), obsidian_clay, geode_obsidian)


def add_resources(blueprint_id: int, resources: tuple[int, int, int], robots: tuple[int, int, int, int]):
    x, y, z = resources
    dx, dy, dz, _ = robots
    lx, ly, lz = robots_limit[blueprint_id]
    return min(lx * 2, x + dx), min(ly * 2, y + dy), min(lz * 2, z + dz)


def spend_resources_on_blueprint(resources: tuple[int, int, int], blueprint: tuple[int, int, int]) -> tuple[int, int, int] | None:
    x, y, z = resources
    dx, dy, dz = blueprint
    if x < dx or y < dy or z < dz:
        return None
    return x - dx, y - dy, z - dz


def add_robot(robots: tuple[int, int, int, int], index: int) -> tuple[int, int, int, int]:
    return tuple(r if i != index else r + 1 for i, r in enumerate(robots))


@cache
def calc(blueprint_id: int, minutes: int, resources: tuple[int, int, int], robots: tuple[int, int, int, int]) -> int:
    if minutes == 0:
        return 0
    geode_robots = robots[-1]
    best = geode_robots * minutes

    for i in range(3, -1, -1):
        if i < 3 and robots[i] >= robots_limit[blueprint_id][i]:
            continue
        new_resources = spend_resources_on_blueprint(resources, blueprints[blueprint_id][i])
        if new_resources is None:
            continue
        new_resources = add_resources(blueprint_id, new_resources, robots)
        new_robots = add_robot(robots, i)
        best = max(best, geode_robots + calc(blueprint_id, minutes - 1, new_resources, new_robots))
        if i == 3:
            return best

    best = max(best, geode_robots + calc(blueprint_id, minutes - 1, add_resources(blueprint_id, resources, robots), robots))
    return best


total = 0
for i in range(len(blueprints)):
    ans = measure(str(i + 1), lambda: calc(i, 24, (0, 0, 0), (1, 0, 0, 0)))
    print(ans)
    total += (i + 1) * ans
print("Part One", total)


total = 1
for i in range(min(len(blueprints), 3)):
    ans = measure(str(i + 1), lambda: calc(i, 32, (0, 0, 0), (1, 0, 0, 0)))
    print(ans)
    total *= ans
print("Part Two", total)
