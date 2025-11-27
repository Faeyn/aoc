from advent_code.coord import Coord

with open("day3_input") as f:
    data = f.read().splitlines()

digits, symbols, gears, numbers = {}, set(), [], []

for row, row_data in enumerate(data):
    for col, cell in enumerate(row_data):
        if cell.isdigit():
            digits[Coord(row, col)] = cell

        elif cell != ".":
            symbols.add(Coord(row, col))

            if cell == "*":
                gears.append(Coord(row, col))


def get_value_and_coords(init_coord):
    coords, queue = [init_coord], [init_coord]
    while queue:
        current_coord = queue.pop()
        for adj_coord in current_coord.get_surrounding():
            if adj_coord in digits and adj_coord not in coords:
                coords.append(adj_coord)
                queue.append(adj_coord)

    return eval("".join(list(map(lambda x: digits[x], sorted(coords, key=lambda x: x.col_i))))), coords


coords_queue = [coord for coord in digits.keys()]

tot = 0
while coords_queue:
    coord_check = coords_queue.pop()
    val, val_coords = get_value_and_coords(coord_check)

    coords_queue = [coord for coord in coords_queue if coord not in val_coords]

    if len(symbols.intersection(set(adj for coord in val_coords for adj in coord.get_surrounding()))):
        tot += val

print(f"Part1: {tot} : 498559")

tot = 0
for gear_coord in gears:
    val1, val2, val1_coords = None, None, []
    coords_queue = [gear_coord]
    while coords_queue:
        current_coord = coords_queue.pop(0)

        for adj_coord in current_coord.get_surrounding():
            if adj_coord in digits and adj_coord not in val1_coords:
                if not val1:
                    val1, val1_coords = get_value_and_coords(adj_coord)
                else:
                    val2, _ = get_value_and_coords(adj_coord)

    if val2:
        tot += val1 * val2

print(f"Part2: {tot} : 72246648")
