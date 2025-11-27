from collections import defaultdict
import re

opposite_edge = {
    "L": "R",
    "R": "L",
    "U": "D",
    "D": "U"
}
symbol = {"R": ">", "D": "v", "L": "<", "U": "^"}

example_size = 4
input_size = 50

size = input_size
with open("day22_input") as f:
    lines = f.read().splitlines()

maze = defaultdict(dict)
col_top = {}
col_bot = {}
row_start = {}
row_end = {}


def find_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None


map = []
for row, maze_line in enumerate(lines[:-2], start=1):
    map.append(maze_line)
    for col, cell in enumerate(maze_line, start=1):
        if cell in [".", "#"]:
            maze[row][col] = cell

            if row not in row_start:
                row_start[row] = col
            row_end[row] = col

            if col not in col_top:
                col_top[col] = row
            col_bot[col] = row

commands = re.findall(r'\d+|[RL]', lines[-1])

start_col = min(maze[1])

rotation_mapping = {"L": 1, "R": -1}
rotation_order = ["R", "U", "L", "D"]
rotation_score = {"R": 0, "U": 3, "L": 2, "D": 1}


def step_function(row, col, direction):
    new_row, new_col = row, col

    if direction == "R":
        new_col = col + 1
        if new_col > row_end[row]:
            new_col = row_start[row]

    if direction == "L":
        new_col = col - 1
        if new_col < row_start[row]:
            new_col = row_end[row]

    if direction == "D":
        new_row = row + 1
        if new_row > col_bot[col]:
            new_row = col_top[col]

    if direction == "U":
        new_row = row - 1
        if new_row < col_top[col]:
            new_row = col_bot[col]

    if maze[new_row][new_col] == ".":
        return new_row, new_col
    else:
        return row, col


state = [1, start_col, "R"]
for command in commands:
    row, col, direction = state

    if command.isnumeric():
        for _ in range(eval(command)):
            row, col = step_function(*state)
            state = [row, col, direction]
    else:
        direction = rotation_order[(rotation_order.index(direction) + rotation_mapping[command]) % len(rotation_order)]

    state = [row, col, direction]

pw = 1000 * state[0] + 4 * state[1] + rotation_score[state[2]]

print(f"Part1: {pw}")

sections_maze = defaultdict(lambda: defaultdict(dict))


def transition_funct(current_surface, row, col, direction):
    next_surface = surface_mapping[current_surface][direction]
    edge = find_key_by_value(surface_mapping[next_surface], current_surface)

    if edge == direction:
        new_col = size + 1 - col
        new_row = size + 1 - row

    elif opposite_edge[edge] == direction:
        new_col = col
        new_row = row

    elif set([edge, direction]) in [set("UR"), set("LD")]:
        new_row = size + 1 - col
        new_col = size + 1 - row

    else:
        new_col = row
        new_row = col

    if edge == "R":
        new_col, new_direction = size, 'L'

    if edge == "L":
        new_col, new_direction = 1, "R"

    if edge == "U":
        new_row, new_direction = 1, "D"

    if edge == "D":
        new_row, new_direction = size, "U"

    return new_row, new_col, new_direction


def step_function_cube(surface, row, col, direction):
    new_surface, new_row, new_col, new_direction = surface, row, col, direction

    if direction == "R":
        new_col = col + 1
        if new_col > size:
            new_row, new_col, new_direction = transition_funct(surface, row, col, "R")
            new_surface = surface_mapping[surface]["R"]

    if direction == "L":
        new_col = col - 1
        if new_col == 0:
            new_row, new_col, new_direction = transition_funct(surface, row, col, "L")
            new_surface = surface_mapping[surface]["L"]

    if direction == "D":
        new_row = row + 1
        if new_row > size:
            new_row, new_col, new_direction = transition_funct(surface, row, col, "D")
            new_surface = surface_mapping[surface]["D"]

    if direction == "U":
        new_row = row - 1
        if new_row == 0:
            new_row, new_col, new_direction = transition_funct(surface, row, col, "U")
            new_surface = surface_mapping[surface]["U"]

    if sections_maze[new_surface][new_row][new_col] == ".":
        return [new_surface, new_row, new_col, new_direction]
    else:
        return [surface, row, col, direction]


(" 12"
 " 3 "
 "45 "
 "6  ")

for row, row_info in maze.items():
    for col, cell in row_info.items():
        if 0 < row <= size:
            if size < col <= 2 * size:
                sections_maze[1][row][col - size] = cell

            if 2 * size < col <= 3 * size:
                sections_maze[2][row][col - 2 * size] = cell

        if size < row <= 2 * size and size < col <= 2 * size:
            sections_maze[3][row - size][col - size] = cell

        if 2 * size < row <= 3 * size:
            if 0 < col <= size:
                sections_maze[4][row - 2 * size][col] = cell

            if size < col <= 2 * size:
                sections_maze[5][row - 2 * size][col - size] = cell

        if 3 * size < row <= 4 * size:
            sections_maze[6][row - 3 * size][col] = cell

surface_mapping = {}
surface_mapping[1] = {"R": 2, "U": 6, "L": 4, "D": 3}
surface_mapping[2] = {"R": 5, "U": 6, "L": 1, "D": 3}
surface_mapping[3] = {"R": 2, "U": 1, "L": 4, "D": 5}
surface_mapping[4] = {"R": 5, "U": 3, "L": 1, "D": 6}
surface_mapping[5] = {"R": 2, "U": 3, "L": 4, "D": 6}
surface_mapping[6] = {"R": 5, "U": 4, "L": 1, "D": 2}

local_coord_to_global = {
    1: (0, size), 2: (0, 2 * size), 3: (size, size), 4: (2 * size, 0), 5: (2 * size, size), 6: (3 * size, 0)
}

# ("  1"
#  "234"
#  "  56")
#
# for row, row_info in maze.items():
#     for col, cell in row_info.items():
#         if 0 < row <= size:
#             if 2 * size < col <= 3 * size:
#                 sections_maze[1][row][col - 2 * size] = cell
#
#         if size < row <= 2 * size:
#             if 0 < col <= 1 * size:
#                 sections_maze[2][row - size][col] = cell
#
#             if size < col <= 2 * size:
#                 sections_maze[3][row - size][col - size] = cell
#
#             if 2 < col <= 3 * size:
#                 sections_maze[4][row - size][col - 2 * size] = cell
#
#         if 2 * size < row <= 3 * size:
#
#             if 2 * size < col <= 3 * size:
#                 sections_maze[5][row - 2 * size][col - 2 * size] = cell
#
#             if 3 * size < col <= 4 * size:
#                 sections_maze[6][row - 2 * size][col - 3 * size] = cell
#
# surface_mapping[1] = {"R": 6, "U": 2, "L": 3, "D": 4}
# surface_mapping[2] = {"R": 3, "U": 1, "L": 6, "D": 5}
# surface_mapping[3] = {"R": 4, "U": 1, "L": 2, "D": 5}
# surface_mapping[4] = {"R": 6, "U": 1, "L": 3, "D": 5}
# surface_mapping[5] = {"R": 6, "U": 4, "L": 3, "D": 2}
# surface_mapping[6] = {"R": 1, "U": 4, "L": 5, "D": 2}
#
# local_coord_to_global = {
#     1: (0, 2 * size), 2: (size, 0), 3: (size, size), 4: (size, 2 * size), 5: (2 * size, 2 * size),
#     6: (2 * size, 3 * size)
# }

state_cube = [1, 1, 1, "R"]
for command in commands:
    surface, row, col, direction = state_cube

    if command.isnumeric():
        for _ in range(eval(command)):
            state_cube = step_function_cube(*state_cube)
    else:
        direction = rotation_order[(rotation_order.index(direction) + rotation_mapping[command]) % len(rotation_order)]
        state_cube = [surface, row, col, direction]

surface_end = state_cube[0]

pw2 = 1000 * (state_cube[1] + local_coord_to_global[surface_end][0]) + 4 * (
        state_cube[2] + local_coord_to_global[surface_end][1]) + rotation_score[state_cube[3]]

print(f"Part2: {pw2}")

for line in map:
    print(line)
