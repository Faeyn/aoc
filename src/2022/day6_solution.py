with open("day6_input") as f:
    lines = f.read()

length_1 = 4  # 4 for part 1,
length_2 = 14  # 14 for part 2
part1_ans = float("inf")

for index in range(len(lines)):
    if len(set(lines[index - length_1: index])) == length_1:
        part1_ans = min(part1_ans, index)

    if len(set(lines[index - length_2: index])) == length_2:
        part2_ans = index
        break

print(f"Part1: {part1_ans}")
print(f"Part2: {part2_ans}")
