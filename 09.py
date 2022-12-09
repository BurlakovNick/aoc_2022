from aoc import *

inp = read()


def touching(p1: V, p2: V):
    return p1 == p2 or any(n == p2 for n in p1.neighbors_8())


def move_close(head: V, tail: V):
    return sorted(tail.neighbors_8(), key=lambda x: head.dist(x))[0]


dirs = {"R": V(0, 1), "L": V(0, -1), "U": V(-1, 0), "D": V(1, 0)}


def move(n):
    rope = [V(0, 0) for _ in range(n)]
    tail_positions = set()

    for dir, cnt in inp:
        for _ in range(cnt):
            rope[0] = rope[0] + dirs[dir]
            for i in range(1, len(rope)):
                if not touching(rope[i - 1], rope[i]):
                    rope[i] = move_close(rope[i - 1], rope[i])
            tail_positions.add(rope[-1])
    return len(tail_positions)


print("Part One", move(2))
print("Part Two", move(10))
