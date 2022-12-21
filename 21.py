from functools import cache
from aoc import *


inp = read(trim=[":"])
cmds = {line[0]: line[1:] for line in inp}


@cache
def calc(name):
    match cmds[name]:
        case [x]:
            return x
        case [left, "+", right]:
            return calc(left) + calc(right)
        case [left, "-", right]:
            return calc(left) - calc(right)
        case [left, "*", right]:
            return calc(left) * calc(right)
        case[left, "/", right]:
            return calc(left) // calc(right)


print("Part One", calc("root"))


@cache
def human_is_reachable(name):
    match cmds[name]:
        case [_]:
            return name == "humn"
        case [left, _, right]:
            return human_is_reachable(left) or human_is_reachable(right)


@cache
def calc_2(name, target = None):
    if name == "humn":
        return target

    left, op, right = cmds[name]
    assert human_is_reachable(left) ^ human_is_reachable(right)

    if name == "root":
        if human_is_reachable(left):
            return calc_2(left, calc(right))
        return calc_2(right, calc(left))

    match op:
        case "+":
            # target = calc(left) + calc(right)
            if human_is_reachable(left):
                return calc_2(left, target - calc(right))
            else:
                return calc_2(right, target - calc(left))
        case "-":
            # target = calc(left) - calc(right)
            if human_is_reachable(left):
                return calc_2(left, target + calc(right))
            else:
                return calc_2(right, calc(left) - target)
        case "*":
            # target = calc(left) * calc(right)
            if human_is_reachable(left):
                return calc_2(left, target // calc(right))
            else:
                return calc_2(right, target // calc(left))
        case "/":
            # target = calc(left) / calc(right)
            if human_is_reachable(left):
                return calc_2(left, target * calc(right))
            else:
                return calc_2(right, calc(left) // target)


print("Part Two", calc_2("root"))
