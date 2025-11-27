import re

with open("day9_input") as f:
    data = f.read().splitlines()

sol1 = 0
sol2 = 0
for row in data:
    sequence = [eval(val) for val in row.split(" ")]

    sequences = [sequence]
    current_sequence = sequence
    while not all([val == 0 for val in current_sequence]):
        current_sequence = [y-x for x, y in zip(current_sequence[:-1], current_sequence[1:])]
        sequences.append(current_sequence)

    sol1 += sum(seq[-1] for seq in sequences)

    ext_val = 0
    for seq in sequences[::-1]:
        ext_val = seq[0] - ext_val
    sol2 += ext_val


print(f"Part1: {sol1}")
print(f"Part2: {sol2}")
