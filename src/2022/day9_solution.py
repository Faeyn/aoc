with open("day9_input") as f:
    lines = f.read().splitlines()


def move(h_coord, t_coord):
    x_h, y_h = h_coord
    x_t, y_t = t_coord

    x_diff = x_h - x_t
    y_diff = y_h - y_t

    if x_diff == 2:
        x_t += 1
        if y_diff > 0:
            y_t += 1
        elif y_diff < 0:
            y_t -= 1
    elif x_diff == -2:
        x_t -= 1
        if y_diff > 0:
            y_t += 1
        elif y_diff < 0:
            y_t -= 1
    elif y_diff == 2:
        y_t += 1
        if x_diff > 0:
            x_t += 1
        elif x_diff < 0:
            x_t -= 1
    elif y_diff == -2:
        y_t -= 1
        if x_diff > 0:
            x_t += 1
        elif x_diff < 0:
            x_t -= 1
    return (x_t, y_t)


move_mapping = {"U": 1, "D": -1, "R": 1, "L": -1}
knots = 10

if __name__ == "__main__":
    coords = [[(0, 0)] for _ in range(knots)]

    for line in lines:
        direc, dist = line.split(" ")

        x_h, y_h = coords[0][-1]
        for i in range(int(dist)):
            if direc in "UD":
                y_h += move_mapping[direc]

            if direc in "RL":
                x_h += move_mapping[direc]

            coords[0].append((x_h, y_h))

            for coord_1, (index, coord_2) in zip(coords[:-1], enumerate(coords[1:], start=1)):
                x_1, y_1 = coord_1[-1]
                x_2, y_2 = coord_2[-1]

                x_2, y_2 = move((x_1, y_1), (x_2, y_2))

                coords[index].append((x_2, y_2))

    print(f"Part1: {len(set(coords[1]))}")
    print(f"Part2: {len(set(coords[-1]))}")
