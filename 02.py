from aoc import *

inp = read()

round_scores = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}
scores = {"X": 1, "Y": 2, "Z": 3}


def get_score():
    return sum(round_scores[(p1, p2)] + scores[p2] for p1, p2 in inp)


print("Part One", get_score())


def find_option(target_p1, res):
    target_score = {"X": 0, "Y": 3, "Z": 6}[res]
    for (p1, p2), score in round_scores.items():
        if p1 == target_p1 and score == target_score:
            return p2


inp = [[p1, find_option(p1, p2)] for p1, p2 in inp]

print("Part Two", get_score())
