import re
from collections import defaultdict, namedtuple

from icecream import ic

ic.enable()

with open("day15_input") as f:
    data = f.read()

Lens = namedtuple("Lens", ["label", "focal_length"])


def HASH(seq):
    val = 0
    for char in seq:
        val = ((val + ord(char)) * 17) % 256
    return val


def HASHMAP(data):
    boxes_with_lenses = defaultdict(list)

    for code in data.split(','):
        label = re.search(r"[a-z]+", code).group()
        operator = code[len(label)]
        box = boxes_with_lenses[HASH(label)]
        c_lens = Lens(label, 0 if operator == "-" else eval(code[-1]))

        lens_not_in_box = True
        for i, lens in enumerate(box):
            if lens.label == label:
                if operator == "-":
                    box.pop(i)

                if operator == "=":
                    box[i] = c_lens
                    lens_not_in_box = False

                break

        if lens_not_in_box and operator == "=":
            box.append(c_lens)

    return boxes_with_lenses


def get_focus_power(boxes):
    power = 0
    for box_nr, lenses in boxes.items():
        power += sum([(box_nr + 1) * i * lens.focal_length for i, lens in enumerate(lenses, start=1)])
    return power


if __name__ == "__main__":
    sum_val = sum([HASH(seq) for seq in data.split(',')])
    print(f"Part1: {sum_val}: is correct {sum_val == 515210}")

    focal_power = get_focus_power(HASHMAP(data))
    print(f"Part2: {focal_power}: is correct {focal_power == 246762}")
