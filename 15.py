from aoc import *

inp = read(trim=["Sensor", "at", "closest", "beacon", "is", "at", "x=", "y=", ":", ","])
inp = [[V(sx, sy), V(bx, by)] for sx, sy, bx, by in inp]
beacons = {b for _, b in inp}


def get_segments(y: int) -> list[list[int]]:
    results = []
    for s, b in inp:
        max_d = (b - s).dist()
        d = abs(y - s.y)
        if d < max_d:
            left = max_d - d
            results.append([s.x - left, s.x + left])
    return results


def solve_1():
    target_y = 2000000
    segments = sorted(get_segments(target_y), key=lambda s: s[0])
    total = 0
    max_x = -100000000000
    for lx, rx in segments:
        if rx <= max_x:
            continue
        elif lx > max_x:
            total += rx - lx + 1 - sum(1 for b in beacons if b.y == target_y and lx <= b.x <= rx)
            max_x = rx
        elif rx > max_x:
            total += rx - max_x - sum(1 for b in beacons if b.y == target_y and max_x + 1 <= b.x <= rx)
            max_x = rx
    return total


ans = measure("solve_1", solve_1)
print("Part One", ans)


def solve_2():
    for y in range(0, 4000000):
        segments = sorted(get_segments(y), key=lambda s: s[0])
        max_x = -1
        for i in range(len(segments) - 1):
            if segments[i][1] + 2 > max_x and segments[i][1] + 2 == segments[i + 1][0]:
                cur = V(segments[i][1] + 1, y)
                return cur
            max_x = max(max_x, segments[i][1])
    return None


ans = measure("solve_2", solve_2)
print("Part Two", ans.x * 4000000 + ans.y)
