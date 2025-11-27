with open("day25_input") as f:
    lines = f.read().splitlines()

snafu_mapping = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
rev_snafu_mapping = {value: key for key, value in snafu_mapping.items()}
snafu_vals = [-2, -1, 0, 1, 2]


def convert_to_dec(_snafu_nr):
    decimal_nr = 0
    for index, char in enumerate(reversed(_snafu_nr)):
        decimal_nr += snafu_mapping[char] * 5 ** index
    return decimal_nr


decimal_nrs = []
for snafu_nr in lines:
    decimal_nrs.append(convert_to_dec(snafu_nr))

total_value = sum(decimal_nrs)


def snafu_range(_index):
    dec_val = 0
    for val in range(_index):
        dec_val += 2 * 5 ** val
    return dec_val


def convert_to_snafu(decimal, index_to_check=None, snafu=None):
    if snafu is None:
        snafu = ""

    if index_to_check is None:
        index_list = range(1000)
    else:
        index_list = [index_to_check]

    match = False
    next_index = 0
    snafu_char = ""
    for i in index_list:
        for val in snafu_vals:
            dec_val = val * 5 ** i
            if dec_val - snafu_range(i) <= decimal <= dec_val + snafu_range(i):
                snafu_char = rev_snafu_mapping[val]
                next_index = i
                decimal -= dec_val
                match = True
                break

        if match:
            break

    snafu += snafu_char
    if next_index >= 1:
        return convert_to_snafu(decimal, next_index - 1, snafu)
    return snafu


print(f"Part1: {convert_to_snafu(total_value)}")
