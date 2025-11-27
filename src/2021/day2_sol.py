import re

with open("day2_input") as f:
    lines = f.read().splitlines()


def add_coord(coord1, coord2):
    return tuple(x + y for x, y in zip(coord1, coord2))


moves = {"forward": (0, 1), "down": (1, 0), "up": (-1, 0)}
moves2 = {
    "forward": lambda coord: (coord[2], 1, 0),
    "down": lambda coord: (0, 0, 1),
    "up": lambda coord: (0, 0, -1),
}

re_string = r"(\w+) (\d+)"

commands = []
commands2 = []

for line in lines:
    match = re.search(re_string, line)
    commands.append((moves[match.group(1)], eval(match.group(2))))
    commands2.append((moves2[match.group(1)], eval(match.group(2))))
current_coord = (0, 0)

for vector, repetition in commands:
    for _ in range(repetition):
        current_coord = add_coord(current_coord, vector)

print(f"Print1: {current_coord[0] * current_coord[1]}")

current_coord = (0, 0, 0)

for move_function, repetition in commands2:
    for _ in range(repetition):
        current_coord = add_coord(current_coord, move_function(current_coord))

print(f"Print2: {current_coord[0] * current_coord[1]}")
