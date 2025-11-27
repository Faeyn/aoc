import itertools
from advent_code.coord import Coord

with open("day15_input") as f:
    data = f.read().splitlines()

length_single = len(data)
length_true = length_single * 5
risks = {}
for row_surface, col_surface in itertools.product(range(5), range(5)):
    for row, row_data in enumerate(data):
        for col, cell in enumerate(row_data):
            div, remain = divmod(eval(cell) + row_surface + col_surface, 10)
            risks[Coord(row + row_surface * length_single, col + col_surface * length_single)] = (remain + div)

cum_risks = {coord: float("inf") for coord, risk in risks.items()}
cum_risks[Coord(0, 0)] = 0

end_node_1 = Coord(length_single - 1, length_single - 1)
end_node_2 = Coord(length_true - 1, length_true - 1)

queue = [Coord(0, 0)]

conditions = [lambda coord: 0 <= coord.row_i < length_true and 0 <= coord.col_i < length_true]

while queue:
    c_coord = queue.pop(0)
    c_risk = cum_risks[c_coord]

    for n_coord in c_coord.get_valid_adjacent(conditions):
        n_risk = risks[n_coord]
        if c_risk + n_risk >= cum_risks[n_coord] or c_risk + n_risk >= cum_risks[end_node_2]:
            continue

        cum_risks[n_coord] = c_risk + n_risk
        queue.append(n_coord)

print(f"Part1: {cum_risks[end_node_1]}")
print(f"Part2: {cum_risks[end_node_2]}")
