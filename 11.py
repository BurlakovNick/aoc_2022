from dataclasses import dataclass
from typing import Tuple

from aoc import *


@dataclass
class Monkey:
    id: int
    items: list[int]
    operation: list
    test_divisible_by: int
    throw_true: int
    throw_false: int
    total_inspections: int


inp = read_blocks(trim=[":", ","])


def parse_monkeys() -> Tuple[list[Monkey], int]:
    mod = 1
    monkeys = []
    for monkey in inp:
        name, starting, operation, test, if_true, if_false = monkey
        monkeys.append(Monkey(
            id=name[1],
            items=starting[2:],
            operation=operation[3:],
            test_divisible_by=test[3],
            throw_true=if_true[5],
            throw_false=if_false[5],
            total_inspections=0,
        ))
        mod *= test[3]
    return monkeys, mod


def increase_worry(level: int, operation: list) -> int:
    match operation:
        case["old", "*", "old"]:
            return level * level
        case ["old", "*", x]:
            return level * x
        case ["old", "+", x]:
            return level + x
    raise RuntimeError()


def simulate_round(monkeys: list[Monkey], need_division: bool, mod: int):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.total_inspections += 1
            level = increase_worry(item, monkey.operation)
            if need_division:
                level //= 3
            level %= mod
            if level % monkey.test_divisible_by == 0:
                monkeys[monkey.throw_true].items.append(level)
            else:
                monkeys[monkey.throw_false].items.append(level)
        monkey.items = []


def simulate(rounds: int, need_division: bool) -> int:
    monkeys, mod = parse_monkeys()

    for i in range(rounds):
        simulate_round(monkeys, need_division, mod)

    busiest = sorted(monkeys, key=lambda m: m.total_inspections, reverse=True)
    return busiest[0].total_inspections * busiest[1].total_inspections


print("Part One", simulate(20, True))
print("Part Two", simulate(10000, False))
