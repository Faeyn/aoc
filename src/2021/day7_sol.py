import numpy as np

with open("day7_input") as f:
    data = f.read()

positions = [eval(pos) for pos in data.split(",")]

ans1 = float('inf')
ans2 = float('inf')

for i in range(min(positions), max(positions) + 1):
    steps = abs(np.array(positions) - i)
    ans1 = min(ans1, sum(steps))

    true_fuel = sum([sum(range(1, step + 1)) for step in steps])
    ans2 = min(ans2, true_fuel)

print(f"Part1: {ans1}")
print(f"Part2: {ans2}")
