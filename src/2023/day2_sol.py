import re
import numpy as np

with open("day2_input") as f:
    data = f.read().splitlines()

cubes_in_bag = {"red": 12, "green": 13, "blue": 14}

game_data_pattern = "\d+ green|\d+ red|\d+ blue"

tot, tot_power = 0, 0
for index, row in enumerate(data, start=1):
    game_id, game_data = row.split(":")
    game_data = re.findall(game_data_pattern, game_data)

    possible_game = True
    min_set_required = {"green": 0, "red": 0, "blue": 0}

    for game_set in game_data:
        number_of_cube = eval(re.search(r"(\d+)", game_set).group())
        color_cube = re.search(r"[a-zA-Z]+", game_set).group()

        if number_of_cube > cubes_in_bag[color_cube]:
            possible_game = False

        if number_of_cube > min_set_required[color_cube]:
            min_set_required[color_cube] = number_of_cube

    tot_power += np.prod([power for power in min_set_required.values()])

    if possible_game:
        tot += index

print(f"Part1: {tot}: 2239")
print(f"Part2: {tot_power}: 83435")
