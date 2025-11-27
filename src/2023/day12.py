import re
from functools import cache
from icecream import ic


@cache
def get_arrangements(sequence, groups):
    if len(groups) == 0:
        return 1 if sequence.count("#") == 0 else 0

    if len(sequence) == 0:
        return 0

    next_char = sequence[0]
    next_group = groups[0]

    pos = 0
    if next_char in ".?":
        pos += get_arrangements(sequence[1:], groups)

    if next_char in "#?":
        if sequence[:next_group].replace("?", "#") != "#" * next_group:
            return pos

        if len(sequence[next_group:]) == 0:
            return pos if len(groups) > 1 else pos + 1

        if sequence[next_group] not in "?.":
            return pos

        pos += get_arrangements(sequence[next_group + 1:], groups[1:])

    return pos


if __name__ == "__main__":
    with open("day12_input") as f:
        data = f.read().splitlines()

    tot, tot_2 = 0, 0
    for i, row_data in enumerate(data):
        sequence, _ = row_data.split(" ")
        groups = tuple(eval(val) for val in re.findall(r"(\w+)", row_data))
        tot += get_arrangements(sequence, groups)
        tot_2 += get_arrangements("?".join([sequence] * 5), groups * 5)

    print(f"Part1: {tot}: Check is {tot == 7361}")
    print(f"Part2: {tot_2}: Check is {tot_2 == 83317216247365}")
