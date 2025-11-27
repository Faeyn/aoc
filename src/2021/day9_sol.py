from functools import reduce
from operator import mul

from advent_code.coord import Coord

with open("day9_input") as f:
    data = f.read().splitlines()

map_data = {}
for row, row_data in enumerate(data):
    for col, cell in enumerate(row_data):
        map_data[Coord(row, col)] = eval(cell)

ans1 = 0
low_points = []
for coord, height in map_data.items():

    if all(map_data[n_coord] > height for n_coord in coord.get_adjacent() if n_coord in map_data):
        ans1 += height + 1
        low_points.append(coord)

print(f"Part1: {ans1}")

basin_sizes = []
for low_point in low_points:
    visited = set()
    queue = [low_point]
    while queue:
        c_coord = queue.pop()
        visited.add(c_coord)

        conditions = [
            lambda coord: coord in map_data,
            lambda coord: coord not in visited,
            lambda coord: map_data[c_coord] < map_data[coord] < 9
        ]

        next_coords = c_coord.get_valid_adjacent(conditions)

        queue.extend(next_coords)

    basin_sizes.append(len(visited))

sum_three_largest_basins = reduce(mul, sorted(basin_sizes)[-3:])

print(f"Part2: {sum_three_largest_basins}")
