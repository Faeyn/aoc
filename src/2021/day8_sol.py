import re

with open("day8_input") as f:
    data = f.read().splitlines()

pattern = r"(\w+)"

codes = [code for row in data for code in re.findall(pattern, row.split("|")[-1])]

ans = 0
for code in codes:
    if len(code) in [2, 3, 4, 7]:
        ans += 1

print(f"Part1: {ans}")

ans2 = 0
for row in data:
    decode = re.findall(pattern, row.split("|")[0])
    decode = ["".join(sorted(code)) for code in decode]

    number = re.findall(pattern, row.split("|")[-1])

    eb = ""
    for l in "abcdefg":
        count = [letter for code in decode for letter in code].count(l)
        if count == 4 or count == 6:
            eb += l

    digit_mapping = {}
    code_mapping = {}
    for code in decode:
        if len(code) == 2:
            digit_mapping[1] = code
            code_mapping[code] = "1"

        if len(code) == 4:
            digit_mapping[4] = code
            code_mapping[code] = "4"

        if len(code) == 3:
            digit_mapping[7] = code
            code_mapping[code] = "7"

        if len(code) == 7:
            digit_mapping[8] = code
            code_mapping[code] = "8"

    for code in decode:
        if set(digit_mapping[4] + digit_mapping[7]).issubset(set(code)) and code not in code_mapping:
            digit_mapping[9] = code
            code_mapping[code] = "9"

        if set(digit_mapping[7] + eb).issubset(set(code)) and code not in code_mapping:
            digit_mapping[0] = code
            code_mapping[code] = "0"

    for code in decode:
        if len(code) == 6 and code not in code_mapping:
            digit_mapping[6] = code
            code_mapping[code] = "6"

    for code in decode:
        if set(code).issubset(set(digit_mapping[6])) and code not in code_mapping:
            digit_mapping[5] = code
            code_mapping[code] = "5"

        if set(code).issubset(set(digit_mapping[9])) and code not in code_mapping:
            digit_mapping[3] = code
            code_mapping[code] = "3"

    for code in decode:
        if code not in code_mapping:
            digit_mapping[2] = code
            code_mapping[code] = "2"

    nr = ""
    for code in number:
        nr += code_mapping["".join(sorted(code))]

    ans2 += eval(nr.lstrip("0"))

print(f"Part2: {ans2}")
