from pprint import pprint

with open("day10_input") as f:
    lines = f.read().splitlines()

x = [1]
for line in lines:
    split_lines = line.split(" ")

    if len(split_lines) == 1:
        x.append(x[-1])

    elif len(split_lines) == 2:
        x.append(x[-1])
        x.append(x[-1] + int(split_lines[-1]))

print(sum([pos * x[pos - 1] for pos in [20 + i * 40 for i in range(6)]]))

image = ["." * 40] * 6
pprint(image)

for index, x_val in enumerate(x[:-1]):
    row_index = index // 40
    row = image[row_index]

    row_pos_index = index - row_index * 40
    if x_val - 1 <= row_pos_index <= x_val + 1:
        image[row_index] = row[0:row_pos_index] + "#" + row[row_pos_index + 1:]

pprint(image)
