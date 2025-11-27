with open("day1_input") as f:
    lines = f.read().splitlines()

increased = 0
for index, depth in enumerate(lines[1:]):
    if eval(depth) > eval(lines[index]):
        increased += 1

print(f"Part1: {increased}")

increased = 0
for index in range(len(lines[:-3])):
    cum1 = sum([eval(lines[i + index]) for i in range(3)])
    cum2 = sum([eval(lines[i + index + 1]) for i in range(3)])

    if cum2 > cum1:
        increased += 1

print(f"Part2: {increased}")
