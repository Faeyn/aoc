import re

with open("day1_input") as f:
    data = f.readlines()

pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
reversed_pattern = r"(enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|\d)"
number_mapping = {
    "one": "1", "1": "1", "eno": "1", "two": "2", "2": "2", "owt": "2", "three": "3", "3": "3", "eerht": "3",
    "four": "4", "4": "4", "ruof": "4", "five": "5", "5": "5", "evif": "5", "six": "6", "6": "6", "xis": "6",
    "seven": "7", "7": "7", "neves": "7", "eight": "8", "8": "8", "thgie": "8", "nine": "9", "9": "9", "enin": "9"}

tot1, tot2 = 0, 0
for row in data:
    row_digits = re.findall(r"(\d)", row)
    tot1 += eval(row_digits[0] + row_digits[-1])

    digit_1 = re.search(pattern, row).group()
    digit_2 = re.search(reversed_pattern, row[::-1]).group()
    tot2 += eval(number_mapping[digit_1] + number_mapping[digit_2])

print(f"Part1: {tot1} : 57346")
print(f"Part2: {tot2} : 57345")
