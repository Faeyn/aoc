from advent_code.coord import Coord

with open("day11_input") as f:
    data = f.read().splitlines()

empty_rows = [index for index, row_data in enumerate(data) if "#" not in row_data]
empty_cols = [col_index for col_index in range(len(data[0])) if "#" not in [row_data[col_index] for row_data in data]]


def get_expansion_mod(reference, empty_index_list, expansion_rate=2):
    for index, value in enumerate(empty_index_list + [float("inf")]):
        if value > reference:
            return index * (expansion_rate - 1)


def get_mod_nodes(expansion_rate):
    nodes = []
    for row, row_data in enumerate(data):
        for col, cell in enumerate(row_data):
            if cell == "#":
                row_mod = get_expansion_mod(row, empty_rows, expansion_rate)
                col_mod = get_expansion_mod(col, empty_cols, expansion_rate)
                nodes.append(Coord(row + row_mod, col + col_mod))
    return nodes


def get_tot_pair_distance(nodes):
    tot_dist = 0
    for index, first_pair in enumerate(nodes[:-1], start=1):
        for second_pair in nodes[index:]:
            tot_dist += first_pair.orthogonal_distance(second_pair)
    return tot_dist


nodes_2 = get_mod_nodes(2)
tot_dist_2 = get_tot_pair_distance(nodes_2)

print(f"Part1: {tot_dist_2}: 9647174")

nodes_mil = get_mod_nodes(1_000_000)
tot_dist_mil = get_tot_pair_distance(nodes_mil)

print(f"Part2: {tot_dist_mil}: 377318892554")
