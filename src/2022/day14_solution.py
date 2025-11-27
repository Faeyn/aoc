with open("day14_input") as f:
    lines = f.read().splitlines()


def get_coordinates_in_line(coord_1, coord_2):
    x_1, y_1 = coord_1
    x_2, y_2 = coord_2

    if x_1 == x_2:
        x_l = x_1
        y_l = [y for y in range(min(y_1, y_2) + 1, max(y_1, y_2))]
        coords = [(x_l, y) for y in y_l]
    else:
        y_l = y_1
        x_l = [x for x in range(min(x_1, x_2) + 1, max(x_1, x_2))]
        coords = [(x, y_l) for x in x_l]

    return coords


max_x = float("-inf")
max_y = float("-inf")
rock = []

for line in lines:
    l_element = [eval(element) for element in line.split(" -> ")]

    rock.extend(l_element)

    for e_1, e_2 in zip(l_element[:-1], l_element[1:]):
        rock.extend(get_coordinates_in_line((e_1[0], e_1[1]), (e_2[0], e_2[1])))

    largest_x = max(l_element, key=lambda x: x[0])[0]
    largest_y = max(l_element, key=lambda x: x[1])[1]

    max_x = max_x if largest_x < max_x else largest_x
    max_y = max_y if largest_y < max_y else largest_y

max_y += 2
max_x = 10000

rock.extend(get_coordinates_in_line((0, max_y), (max_x, max_y)))

obstacle_free_map = [[True for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for x, y in rock:
    obstacle_free_map[y][x] = False


def sand_movement(obstacle_free, pos=(500, 0)):
    x_pos = pos[0]
    y_pos = pos[1]

    if not obstacle_free[0][500]:
        return False

    if obstacle_free[y_pos + 1][x_pos]:
        return sand_movement(obstacle_free, (x_pos, y_pos + 1))

    elif obstacle_free[y_pos + 1][x_pos - 1]:
        return sand_movement(obstacle_free, (x_pos - 1, y_pos + 1))

    elif obstacle_free[y_pos + 1][x_pos + 1]:
        return sand_movement(obstacle_free, (x_pos + 1, y_pos + 1))

    else:
        return x_pos, y_pos


Simulating = True
index = 0
equilibrium = 0

while True:
    coord_sand = sand_movement(obstacle_free_map)

    if not coord_sand:
        break
    x_sand, y_sand = coord_sand

    if y_sand == max_y - 1 and not equilibrium:
        equilibrium = index

    index += 1

    obstacle_free_map[y_sand][x_sand] = False

print(f"Part1: {equilibrium}")
print(f"Part2: {index}")
