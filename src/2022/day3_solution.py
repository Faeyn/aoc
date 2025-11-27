with open('day3_input') as f:
    lines = f.read().splitlines()

items = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
priority_map = {item: priority for priority, item in enumerate(items + [item.upper() for item in items], start=1)}

total_priority_value = 0
for line in lines:
    size_compartment = int(len(line) / 2)
    compartment_1 = line[:size_compartment]
    compartment_2 = line[size_compartment:]
    common_item = list(set(compartment_1).intersection(compartment_2))
    assert len(common_item) == 1
    total_priority_value += priority_map[common_item[0]]

print(f"Part1: {total_priority_value}")


groups = [lines[x:x + 3] for x in range(0, int(len(lines)), 3)]
check_lines = []

total_priority_value = 0
for group in groups:
    check_lines += group
    common_item = list(set(group[0]).intersection(group[1]).intersection(group[2]))
    assert len(common_item) == 1
    total_priority_value += priority_map[common_item[0]]
assert len(lines) == len(check_lines)

print(f"Part2: {total_priority_value}")
