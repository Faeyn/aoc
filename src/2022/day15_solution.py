import itertools
from datetime import datetime
from itertools import product
from pprint import pprint

# file = "example"
file = 'input'
with open(f"day15_{file}") as f:
    lines = f.read().splitlines()

sensor_beacon_pair = []
for line in lines:
    split_line = line.split(" ")
    sensor_coord = (
        eval(split_line[2].replace("x=", "").replace(",", "")), eval(split_line[3].replace("y=", "").replace(":", "")))
    beacon_coord = (eval(split_line[-2].replace("x=", "").replace(",", "")), eval(split_line[-1].replace("y=", "")))

    sensor_beacon_pair.append((sensor_coord, beacon_coord))

line_check = 10 if file == "example" else 2000000
occupied_in_line = []
dist_map = {}

for s_coord, b_coord in sensor_beacon_pair:
    x_s, y_s = s_coord
    x_b, y_b = b_coord
    dist = abs(x_s - x_b) + abs(y_s - y_b)

    y_high = y_s - (x_s - dist - 1)
    y_low = y_s - (x_s + dist + 1)

    x_high = y_s + (x_s - dist - 1)
    x_low = y_s + (x_s + dist + 1)

    dist_map[s_coord] = {"y_high": y_high, "y_low": y_low, "x_high": x_high, "x_low": x_low}

    if y_s - dist <= line_check <= y_s + dist:
        vertical_distance_to_line = abs(line_check - y_s)
        horizontal_range = dist - vertical_distance_to_line

        occupied_in_line.append((x_s - horizontal_range, x_s + horizontal_range))

min_x = min([min(x) for x in occupied_in_line])
max_x = max([max(x) for x in occupied_in_line])

occupied = 0
for x in range(min_x - 1, max_x + 1):
    for range_min, range_max in occupied_in_line:
        if range_min < x <= range_max:
            occupied += 1
            break

print(f"Part1: {occupied}")

y_at_0_pos, y_at_0_neg = 0, 0
for (beacon, vals), (beacon2, vals2) in itertools.combinations(dist_map.items(), 2):
    if vals["x_high"] == vals2["x_low"]:
        y_at_0_neg = vals2["x_low"]

    if vals2["x_high"] == vals["x_low"]:
        y_at_0_neg = vals["x_low"]

    if vals["y_high"] == vals2["y_low"]:
        y_at_0_pos = vals["y_low"]

    if vals2["y_high"] == vals["y_low"]:
        y_at_0_pos = vals["y_low"]

x_val = (y_at_0_neg - y_at_0_pos) / 2
y_val = y_at_0_neg - x_val

print(f'Part2: {x_val * 4000000 + y_val}')
