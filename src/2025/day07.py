from pathlib import Path
import re
from collections import defaultdict
from functools import cache

with open(Path(__file__).parent / ".input/day07_input") as f:
    data = f.read()

# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

data = data.splitlines()

tachyons = [(0, data[0].index("S"))]

splitters = defaultdict(list)

for i_r, row in enumerate(data):
    for i_c, val in enumerate(row):
        if val == "^":
            splitters[i_c].append(i_r)

def find_min_row(r, c):
    min_row = float("inf")
    for r_s in splitters[c]:
        min_row = min(min_row, r_s if r_s > r else float("inf"))
    return min_row

hit_splitter = set()
while tachyons:
    r, c = tachyons.pop(0)

    min_row = find_min_row(r, c)
    if min_row != float("inf"):
        hit_splitter.add((min_row, c))
        if (min_row, c-1) not in tachyons:
            tachyons.append((min_row, c-1))

        if (min_row, c+1) not in tachyons:
            tachyons.append((min_row, c+1))

print("Part1 :", len(hit_splitter))


@cache
def timelines(pos):
    r, c = pos
    tls = 0

    min_row = find_min_row(r, c) 

    if min_row != float("inf"):
        tls += timelines((min_row, c-1)) + timelines((min_row, c+1))
    else:
        return 1

    return tls
        
print("Part2: ", timelines((0, data[0].index("S"))))
