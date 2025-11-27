from pprint import pprint

import numpy as np

with open("day18_input") as f:
    line = f.read().splitlines()

cubes_array = [np.array([eval(val) + 1 for val in line.split(",")]) for line in line]
cubes_tuple = [tuple([eval(val) + 1 for val in line.split(",")]) for line in line]

mods = [
    np.array([0, 0, 1]),
    np.array([0, 0, -1]),
    np.array([0, 1, 0]),
    np.array([0, -1, 0]),
    np.array([1, 0, 0]),
    np.array([-1, 0, 0])
]

surfaces = len(cubes_array) * 6
connected_surfaces = 0
for cube in cubes_array:
    for mod in mods:

        # Direct
        if tuple(cube + mod) in cubes_tuple:
            connected_surfaces += 1

exposed_surfaces = surfaces - connected_surfaces
print(f"Part1: {exposed_surfaces}")

# Sol 2
max_cube = [0, 0, 0]
for cube in cubes_array:
    max_cube = np.array([max(x, y) for x, y in zip(cube, max_cube)])

max_cube = max_cube + [2, 2, 2]

queue = [np.array([0, 0, 0])]
water_cubes = []
exposed_surfaces = 0

while queue:
    cube = queue.pop()

    if tuple(cube) in water_cubes:
        continue

    water_cubes.append(tuple(cube))

    for mod in mods:
        next_cube = cube + mod

        if tuple(next_cube) in cubes_tuple:
            exposed_surfaces += 1
            continue

        if all(0 <= val < max_val for val, max_val in zip(next_cube, max_cube)):
            queue.append(next_cube)

print(f"Part2: {exposed_surfaces}")
