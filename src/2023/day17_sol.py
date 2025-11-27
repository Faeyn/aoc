import heapq
from collections import defaultdict
from functools import cache
from time import time

from icecream import ic

with open('day17_input') as f:
    data = f.read().splitlines()

cols = len(data[0])
rows = len(data)

heat_loss = [[eval(hl) for hl in row] for row in data]


def get_valid_moves(row, col, moves, min_dist, max_dist):
    possible_moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    valid_moves = []

    for move_row, move_col in possible_moves:
        for step in range(min_dist, max_dist + 1):
            if moves[-1] == (move_row * -1, move_col * -1):
                continue

            if tuple([(move_row, move_col)] * (max_dist + 1 - step)) == moves[step - 1:]:
                continue

            if 0 <= row + move_row * step < rows and 0 <= col + move_col * step < cols:
                valid_moves.append((move_row, move_col, step, moves[step:] + tuple([(move_row, move_col)] * step)))
    return valid_moves


def dijkstra(min_dist, max_dist):
    c_heat_loss = [[defaultdict(lambda: float("inf")) for _ in row] for row in data]
    c_heat_loss[0][0][tuple([(0, 0)] * max_dist)] = 0

    visited = set()
    queue = [(0, (0, 0, tuple([(0, 0)] * max_dist)))]
    while queue:
        HL, (row, col, moves) = heapq.heappop(queue)

        if (row, col, moves) in visited:
            continue

        visited.add((row, col, moves))

        for move_row, move_col, n_steps, n_moves in get_valid_moves(row, col, moves, min_dist, max_dist):
            new_HL = HL + sum([heat_loss[row + move_row * step][col + move_col * step] for step in range(1, n_steps + 1)])
            n_row, n_col = row + move_row * n_steps, col + move_col * n_steps

            if (n_row, n_col, n_moves) in visited:
                continue

            if new_HL < c_heat_loss[n_row][n_col][n_moves]:
                c_heat_loss[n_row][n_col][n_moves] = new_HL
                heapq.heappush(queue, (new_HL, (n_row, n_col, n_moves)))
    return min(c_heat_loss[rows - 1][cols - 1].values())


sol1 = dijkstra(1, 3)
ic(f"Part1: {sol1}: Check is {sol1 == 956}")

sol2 = dijkstra(4, 10)
ic(f"Part2: {sol2}: Check is {sol2 == 1106}")
