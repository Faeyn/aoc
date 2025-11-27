import re

with open("day4_input") as f:
    data = f.read().splitlines()

bingo_nrs = [eval(val) for val in data[0].split(",")]
board_sets = []
for i in range(int(len(data) / 6)):
    board = [eval(val) for row in data[2 + 6 * i:7 + 6 * i] for val in re.findall(r"(\d+)", row)]
    board_set = [set(board[5 * j:5 + 5 * j]) for j in range(5)] + [set(board[j::5]) for j in range(5)]
    board_sets.append((board_set, tuple(board)))

prev_completed, set_check = set(), set()


def get_score(comp, prev_comp, set_c, _nr):
    return sum(set(comp.difference(prev_comp).pop()).difference(set_c)) * _nr


for nr in bingo_nrs:
    set_check.add(nr)
    completed = {full_set for board_set, full_set in board_sets if any(row.issubset(set_check) for row in board_set)}

    if len(completed) == 1 and len(prev_completed) == 0:
        print(f"Part1: {get_score(completed, prev_completed, set_check, nr)}")

    if len(completed) == len(board_sets) and len(prev_completed) == len(board_sets) - 1:
        print(f"Part2: {get_score(completed, prev_completed, set_check, nr)}")

    if len(completed) > len(prev_completed):
        prev_completed = completed
