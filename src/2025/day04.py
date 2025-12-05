import itertools as it
from pathlib import Path

f = open(Path(__file__).parent / '.input/day04_input')
data = f.read()
f.close()

data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

data = data.splitlines()
live_chart = [[y for y in x] for x in data]

h = len(data)
w = len(data[0])

def inChart(r, c):
    return 0 <= r < h and 0 <= c < w

orth = [(x, y) for x, y in it.product((-1, 0, 1), (-1, 0, 1)) if (x, y) != (0, 0)]

def canRemove(r, c):
    adj_count = 0
    
    for r_a, c_a in orth:
        if inChart(r+r_a, c+c_a):
            adj_count += 1 if data[r+r_a][c+c_a] == "@" else 0

    return adj_count < 4

def canRemove2(r, c):
    adj_count = 0
    
    for r_a, c_a in orth:
        if inChart(r+r_a, c+c_a):
            adj_count += 1 if live_chart[r+r_a][c+c_a] == "@" else 0

    return adj_count < 4

part_1 = 0
for r in range(h):
    for c in range(w):
        if data[r][c] != "@":
            continue
         
        part_1 += 1 if canRemove(r, c) else 0

print("Part1: ", part_1)

rolls = []
for r in range(h):
    for c in range(w):
        if data[r][c] == "@":
            rolls.append((r,c))

part_2 = 0

while rolls:
    r, c = rolls.pop(0)

    if not canRemove2(r, c):
        continue
    
    part_2 += 1
    live_chart[r][c] = "x"
    removed.add((r,c))
    
    for r_a, c_a in orth:
        r_c = r + r_a
        c_c = c + c_a 
        if inChart(r_c, c_c) and live_chart[r_c][c_c] == "@" and (r_c, c_c) not in rolls:
            rolls.append((r_c, c_c))

print("Part2: ", part_2)


        







            
            
