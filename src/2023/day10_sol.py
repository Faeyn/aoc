import math

from advent_code.coord import Coord, print_coords_dict

with open("day10_input") as f:
    data = f.read().splitlines()

"https://en.wikipedia.org/wiki/Box-drawing_character"
box_mapping = {"-": "─", "|": "│", "F": "┌", "7": "┐", "L": "└", "J": "┘", ".": " ", "S": "S"}

nodes = {}
for row, row_data in enumerate(data):
    for col, cell in enumerate(row_data):
        nodes[Coord(row, col)] = box_mapping[cell]

        if cell == "S":
            start = Coord(row, col)

pipe_mapping = {
    box_mapping["|"]: [Coord(1, 0), Coord(-1, 0)],
    box_mapping["-"]: [Coord(0, 1), Coord(0, -1)],
    box_mapping["L"]: [Coord(-1, 0), Coord(0, 1)],
    box_mapping["J"]: [Coord(-1, 0), Coord(0, -1)],
    box_mapping["7"]: [Coord(1, 0), Coord(0, -1)],
    box_mapping["F"]: [Coord(1, 0), Coord(0, 1)],
    box_mapping["."]: []
}

# Find pipes connected to start
nodes_next_to_start = []
for n_start_node in start.get_adjacent():
    for mod in pipe_mapping[nodes[n_start_node]]:
        if nodes[n_start_node + mod] == "S":
            nodes_next_to_start.append(n_start_node)

# Replace start with pipe
if start + Coord(1, 0) in nodes_next_to_start:
    if start + Coord(-1, 0) in nodes_next_to_start:
        nodes[start] = "│"
    elif start + Coord(0, 1) in nodes_next_to_start:
        nodes[start] = "┌"
    elif start + Coord(0, -1) in nodes_next_to_start:
        nodes[start] = "┐"
elif start + Coord(-1, 0) in nodes_next_to_start:
    if start + Coord(0, 1) in nodes_next_to_start:
        nodes[start] = "└"
    elif start + Coord(0, -1) in nodes_next_to_start:
        nodes[start] = "┘"
else:
    nodes[start] = "─"


def get_connecting_pipe(path):
    new_path = [node for node in path]
    c_node = path[-1]
    for mod in pipe_mapping[nodes[c_node]]:
        if c_node + mod not in path:
            new_path.append(c_node + mod)
    return new_path


path = [start, nodes_next_to_start[0]]
while path[-1] != nodes_next_to_start[1]:
    path = get_connecting_pipe(path)

furthest_point = math.ceil(len(path) / 2)
print(f"Part1: {furthest_point}: 6640")

print_coords_dict({coord: nodes[coord] for coord in path}, single=True)

# Ray tracing
corner_mapping = {"┐": "└", "┘": "┌"}
surrounded_nodes = 0
sur_nodes = {}
for row_index in range(len(data)):
    inside = False
    last_corner = ""
    for col_index in range(len(data[0])):
        coord = Coord(row_index, col_index)
        cell = "." if coord not in path else nodes[coord]

        if cell == "│":
            inside = not inside

        if cell in "┌┐└┘":
            if cell in "┐┘":
                if last_corner == corner_mapping[cell]:
                    inside = not inside
            last_corner = cell

        if cell == "." and inside:
            sur_nodes[Coord(row_index, col_index)] = "#"
            surrounded_nodes += 1

print(f"Part2: {surrounded_nodes}: 411")

new_dict = {coord: nodes[coord] for coord in path}
new_dict.update(sur_nodes)
print_coords_dict(new_dict, single=True)

# # Double and flood
# double_space_path = []
# for index, node in enumerate(path):
#     new_node = node * 2
#     bit_node = new_node.mid(path[(index + 1) % len(path)] * 2)
#     double_space_path.extend([new_node, bit_node])
#
# max_row = max([coord.row for coord in double_space_path])
# min_row = min([coord.row for coord in double_space_path])
# max_col = max([coord.col for coord in double_space_path])
# min_col = min([coord.col for coord in double_space_path])
#
# visited = set()
# areas = []
#
# for row in range(min_row, max_row + 1):
#     for col in range(min_col, max_col + 1):
#         c_coord = Coord(row, col)
#         if c_coord in visited or c_coord in double_space_path:
#             continue
#
#         queue, area = [c_coord], []
#         surrounded = True
#         while queue:
#             cu_coord = queue.pop(0)
#             visited.add(cu_coord)
#             area.append(cu_coord)
#             for n_coord in cu_coord.get_adjacent():
#                 if n_coord in visited or n_coord in queue or n_coord in double_space_path:
#                     continue
#
#                 if min_row <= n_coord.row <= max_row and min_col <= n_coord.col <= max_col:
#                     queue.append(n_coord)
#                 else:
#                     surrounded = False
#
#         if surrounded:
#             areas.extend(area)
#
# surrounded_nodes = len([coord for coord in areas if coord.row % 2 == 0 and coord.col % 2 == 0])
# print(f"Part2: {surrounded_nodes}: 411")
