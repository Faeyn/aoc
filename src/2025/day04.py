import itertools as it
from pathlib import Path

f = open(Path(__file__).parent / '.input/day04_input')
data = f.read()
f.close()

# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

data = data.splitlines()
live_chart = [[y for y in x] for x in data]

h = len(data)
w = len(data[0])
orth = [(x, y) for x, y in it.product((-1, 0, 1), (-1, 0, 1)) if (x, y) != (0, 0)]


def inChart(r, c):
    return 0 <= r < h and 0 <= c < w

def canRemove(r, c, chart):
    return sum(chart[r + r_a][c + c_a] == "@" for r_a, c_a in orth if inChart(r+r_a, c+c_a)) < 4
    
print("Part1: ", sum(canRemove(r, c, data) for r, c in it.product(range(h), range(w)) if data[r][c] == "@"))


part_2 = 0
rolls = [(r, c) for r, c in it.product(range(h), range(w)) if data[r][c] == "@"]
while rolls:
    r, c = rolls.pop()

    if not canRemove(r, c, live_chart):
        continue
    
    part_2 += 1
    live_chart[r][c] = "x"
    
    for r_a, c_a in orth:
        r_c = r + r_a
        c_c = c + c_a 
        if inChart(r_c, c_c) and live_chart[r_c][c_c] == "@" and (r_c, c_c) not in rolls:
            rolls.append((r_c, c_c))

print("Part2: ", part_2)

