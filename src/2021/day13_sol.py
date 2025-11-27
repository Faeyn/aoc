import re
from advent_code.coord import Coord, print_coords

with open('day13_input') as f:
    data = f.read().splitlines()

pattern = r"(\d+)"

coords = []
for row in data:
    if re.match(r"(\d+),(\d+)", row):
        x, y = re.findall(pattern, row)
        coords.append(Coord(eval(y), eval(x)))

pattern = r"([xy])=(\d+)"

commands = []
for row in data:
    if re.search("fold", row):
        axis, value = re.findall(pattern, row)[0]
        commands.append((axis, eval(value)))

fold_mapping = {"y": Coord(-1, 0), "x": Coord(0, -1)}


def coords_post_fold(fold, coords):
    axis, value = fold
    new_coords = []
    for coord in coords:
        coord_val = coord.row_i if axis == "y" else coord.col_i

        if coord_val > value:
            new_coords.append(coord + fold_mapping[axis] * 2 * (coord_val - value))
        else:
            new_coords.append(coord)
    return new_coords


folded_coords = [coord for coord in coords]

for fold_i, fold in enumerate(commands):
    folded_coords = coords_post_fold(fold, folded_coords)

    if fold_i == 0:
        print(f"Part1: {len(set(folded_coords))}")

print("Part2")
print_coords(folded_coords)
