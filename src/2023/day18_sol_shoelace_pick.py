from advent_code.coord import Coord, dir_map

with open('day18_input') as f:
    data = f.read().splitlines()


def get_area(dig_plan):
    c_coord = Coord(0, 0)
    area, perimeter = 0, 0
    for op in dig_plan:
        dist = eval(op[1])
        perimeter += dist
        n_coord = c_coord + dir_map[op[0]] * dist
        area += 0.5 * (c_coord.col * n_coord.row - c_coord.row * n_coord.col)
        c_coord = n_coord
    return int(area + perimeter / 2 + 1)


def parse_hex(hex_input):
    hex_map = {"0": "R", "1": "D", "2": "L", "3": "U"}
    return str(hex_map[hex_input[-2]]), str(int(hex_input[2:-2], 16))


dig_plan_1, dig_plan_2 = [], []
for row in data:
    dig_plan_1.append(row.split(" "))
    dig_plan_2.append(list(parse_hex(row.split(" ")[-1])))

area_1 = get_area(dig_plan_1)
area_2 = get_area(dig_plan_2)

print(f"Part1: {area_1}, Check is {area_1 == 62500}")
print(f"Part2: {area_2}, Check is {area_2 == 122109860712709}")
