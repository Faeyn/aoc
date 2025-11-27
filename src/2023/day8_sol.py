import re
import numpy as np

with open("day8_input") as f:
    data = f.read().splitlines()

instructions = data[0]

node_map = {}
for row in data[2:]:
    current_n, left_n, right_n = re.findall(r"(\w+)", row)
    node_map[current_n] = {"L": left_n, "R": right_n}


def find_steps(start, condition):
    current = start
    steps = 0
    while condition(current):
        current = node_map[current][instructions[steps % len(instructions)]]
        steps += 1
    return steps


print(f"Part1: {find_steps('AAA', lambda x: x != 'ZZZ')}: 14257")

current_set = [x for x in node_map.keys() if x[-1] == "A"]
all_steps = [find_steps(start, lambda x: x[-1] != "Z") for start in current_set]

print(f"Part2: {np.lcm.reduce(all_steps)}: 16187743689077")
