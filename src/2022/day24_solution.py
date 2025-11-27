from collections import namedtuple
from functools import cache
from time import time as tm

with open("day24_input") as f:
    lines = f.read().splitlines()

BlizzardInfo = namedtuple("BlizzardInfo", ["coord", "dir"])
Coord = namedtuple("Coord", ["row", "col"])

valley = []
directions = ['v', "^", ">", "<"]
storm_move = {'v': Coord(1, 0), ">": Coord(0, 1), "^": Coord(-1, 0), "<": Coord(0, -1)}
adj = [x for x in storm_move.values()]
adj.append(Coord(0, 0))

directions_set = set(directions)
blizzards = []

max_row_index = len(lines[1:-1]) - 1
max_col_index = len(lines[0][1:-1]) - 1

for row, line in enumerate(lines[1:-1]):
    for col, cell in enumerate(line[1:-1]):
        if cell in directions_set:
            blizzards.append(BlizzardInfo(Coord(row, col), cell))
blizzards = tuple(blizzards)


def get_new_blizzard(blizzard):
    move = storm_move[blizzard.dir]
    row = blizzard.coord.row_i + move.row_i
    col = blizzard.coord.col_i + move.col_i

    if row > max_row_index:
        row = 0

    if row < 0:
        row = max_row_index

    if col > max_col_index:
        col = 0

    if col < 0:
        col = max_col_index

    return Coord(row, col)


def add_coord(coord1, coord2):
    return Coord(coord1.row_i + coord2.row_i, coord1.col_i + coord2.col_i)


@cache
def get_next_blizzard_state(blizzard_state):
    next_blizzard = []
    for blizzard in blizzard_state:
        next_blizzard.append(BlizzardInfo(get_new_blizzard(blizzard), blizzard.dir))
    return tuple(next_blizzard)


def get_position(position, blizzard_state, start_position, end_position):
    coords_in_blizzard = [info.coord for info in blizzard_state]
    next_positions = []
    for move in adj:
        new_row = position.row_i + move.row
        new_col = position.col_i + move.col

        if Coord(new_row, new_col) == start_position:
            next_positions.append(start_position)

        if Coord(new_row, new_col) == end_position:
            return [end_position]

        if 0 <= new_row <= max_row_index and 0 <= new_col <= max_col_index:
            if add_coord(position, move) not in coords_in_blizzard:
                next_positions.append(Coord(new_row, new_col))

    return next_positions


def print_map(blizzard_state, position):
    for row in range(max_row_index + 1):
        line = ""
        for col in range(max_col_index + 1):
            if Coord(row, col) in [info.coord for info in blizzard_state]:
                index = [info.coord for info in blizzard_state].index(Coord(row, col))

                count = [info.coord for info in blizzard_state].count(Coord(row, col))

                if count == 1:
                    line += blizzard_state[index].dir
                else:
                    line += str(count)
            elif Coord(row, col) == position:
                line += "E"
            else:
                line += "."
        print(line)


@cache
def dfs(time, current_position, start_position, end_position, blizzard_state, min_time=None):
    if min_time is None:
        min_time = float("inf")

    if time >= min_time or time >= 400:
        return float("inf")

    if current_position == end_position:
        return min(time, min_time)

    next_blizzard_state = get_next_blizzard_state(blizzard_state)

    valid_positions = get_position(current_position, next_blizzard_state, start_position, end_position)

    for current_position in valid_positions:
        min_time = min(min_time,
                       dfs(time + 1, current_position, start_position, end_position, next_blizzard_state, min_time))

    return min_time


print("initial state")
start_time = tm()
start_pos = Coord(-1, 0)
end_pos = Coord(max_row_index + 1, max_col_index)

first_trip = dfs(1, start_pos, start_pos, end_pos, get_next_blizzard_state(blizzards))
print(f"Part1: {first_trip}")
print("time", tm() - start_time)

import cProfile

# cProfile.run("dfs(1, start_pos, start_pos, end_pos, get_next_blizzard_state(blizzards))", sort="cumtime")

# return_blizzard_state = tuple([x for x in blizzards])
#
# for _ in range(first_trip):
#     return_blizzard_state = get_next_blizzard_state(return_blizzard_state)
#
# start_time = tm()
# return_trip = dfs(1, end_pos, end_pos, start_pos, get_next_blizzard_state(return_blizzard_state))
# print(return_trip)
# print("time", tm() - start_time)
#
# second_trip_blizzard_state = tuple([x for x in return_blizzard_state])
# for _ in range(return_trip):
#     second_trip_blizzard_state = get_next_blizzard_state(second_trip_blizzard_state)
#
# start_time = tm()
# second_trip = dfs(1, start_pos, start_pos, end_pos, get_next_blizzard_state(second_trip_blizzard_state))
# print(second_trip)
# print("time", tm() - start_time)
# print(f"Part2: {first_trip + return_trip + second_trip}")
