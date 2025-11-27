import re
from collections import defaultdict
from typing import List

from advent_code.coord import Coord

with open("day5_input") as f:
    data = f.read().splitlines()

pattern = r"(\d+),(\d+)"
pairs: List[List[Coord]] = [
    [Coord(*[eval(val) for val in reversed(coord)]) for coord in re.findall(pattern, row)] for row in data
]

vents = defaultdict(lambda: defaultdict(lambda: 0))
for pair in pairs:
    head, tail = pair

    for coord in head.straight_line(tail):
        vents["dia"][coord] += 1

    try:
        for coord in head.orthogonal_line(tail):
            vents["lin"][coord] += 1
    except:
        pass

ans = len([val for val in vents["lin"].values() if val > 1])
print(f"Part1: {ans}")

ans2 = len([val for val in vents["dia"].values() if val > 1])
print(f"Part2: {ans2}")
