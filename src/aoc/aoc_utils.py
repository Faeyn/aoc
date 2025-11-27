import re


def get_nums(s: str) -> list[str]:
    return [int(x) for x in re.findall(r'-?\d+', s)]


def get_words(s: str) -> list[str]:
    return [str(x) for x in re.findall(r'\w+', s)]


def get_location_mapper(m: list[str]) -> dict[str, (int, int)]:
    loc_map = {}
    for row_i, row in enumerate(m):
        for col_i, col in enumerate(row):
            loc_map[col] = (row_i, col_i)
    return loc_map


def get_manhatten_distance(c1, c2) -> int:
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])