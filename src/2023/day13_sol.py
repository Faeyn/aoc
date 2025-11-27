import math
from pprint import pprint

with open("day13_input") as f:
    data = f.read().splitlines()

data_sets, data_set = [], []
for row_data in data:
    if row_data == "":
        if data_set:
            data_sets.append(data_set)
        data_set = []
    else:
        data_set.append(row_data)


def get_mirror(set_to_check, with_smudge=True):
    mirror_index = 0

    set_length = len(set_to_check)
    for index in range(1, set_length):
        lower_range = 0 if index <= set_length - index else set_length - 2 * (set_length - index)
        orginl = "".join(set_to_check[lower_range:index])
        mirror = "".join(set_to_check[index:2 * index][::-1])

        if with_smudge:
            if orginl == mirror:
                mirror_index = index
        else:
            if sum([o != m for o, m in zip(orginl, mirror)]) == 1:
                mirror_index = index
    return mirror_index


def get_val(data_set, with_smudge=True):
    transposed_data_set = []
    for col_index in range(len(data_set[0])):
        transposed_data_set.append("".join([row[col_index] for row in data_set]))
    return get_mirror(data_set, with_smudge) * 100 + get_mirror(transposed_data_set, with_smudge)


tot, tot2 = 0, 0
for data_set in data_sets:
    tot += get_val(data_set)
    tot2 += get_val(data_set, False)

print(f"Part1: {tot}: 30487")
print(f"Part2: {tot2}: 31954")
