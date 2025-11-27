import re
import numpy as np

with open("day6_input") as f:
    data = f.read().splitlines()

times = [eval(x) for x in re.findall(r"(\d+)", data[0])]
distances = [eval(x) for x in re.findall(r"(\d+)", data[1])]

time_tot = eval("".join([str(x) for x in times]))
distance_tot = eval("".join([str(x) for x in distances]))


def get_range(time, distance):
    crit_point = np.roots([-1, time, -distance])
    return int(np.floor(crit_point[0]) - np.ceil(crit_point[1]) + 1)


sol1 = np.prod([get_range(time, distance) for time, distance in zip(times, distances)])
sol2 = get_range(time_tot, distance_tot)

print(f"Part1 {sol1} : 503424")
print(f"Part2 {sol2} : 32607562")
