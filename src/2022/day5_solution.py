from pprint import pprint

with open("day5_input") as f:
    lines = f.read().splitlines()

stacks1 = {}
data_column = {}

for index, line in enumerate(reversed(lines[:9])):
    if index == 0:
        for column_index, x in enumerate(line):
            if x != " ":
                stacks1[x] = []
                data_column[column_index] = x

    else:
        for column_index, x in enumerate(line):
            if column_index in data_column and x.isalpha():
                stacks1[data_column[column_index]].append(x)

print("Initial state:")
pprint(stacks1)

moves = []

for line in lines[10:]:
    split_line = line.split(" ")
    number_of_crates = int(split_line[1])
    from_stack = split_line[3]
    to_stack = split_line[5]
    moves.append({"number_of_crates": number_of_crates, "from_stack": from_stack, "to_stack": to_stack})

stacks2 = {key: [_ for _ in val] for key, val in stacks1.items()}

for move in moves:
    stacks1[move["to_stack"]].extend(reversed(stacks1[move["from_stack"]][-move["number_of_crates"]:]))  # Part 1
    stacks1[move["from_stack"]] = stacks1[move["from_stack"]][:-move["number_of_crates"]]

    stacks2[move["to_stack"]].extend(stacks2[move["from_stack"]][-move["number_of_crates"]:])  # Part 2
    stacks2[move["from_stack"]] = stacks2[move["from_stack"]][:-move["number_of_crates"]]

ans1 = ""
ans2 = ""

for i in range(1, 10):
    ans1 += stacks1[str(i)][-1]
    ans2 += stacks2[str(i)][-1]

print(f"Part1: {ans1}")
print(f"Part2: {ans2}")
