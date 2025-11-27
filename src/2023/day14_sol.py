from functools import cache

from advent_code.matrix import Direction, rotate_matrix

with open("day14_input") as f:
    data = [list(row) for row in f.read().splitlines()]


def move_left(data):
    new_data = []
    for row in data:
        new_data.append(move_row_left(tuple(row)))
    return new_data


@cache
def move_row_left(row):
    return list("#".join(["".join(sorted(sec, reverse=True)) for sec in "".join(row).split("#")]))


def count_weight(data):
    tot_weight = 0
    for row_nr, row_data in enumerate(data[::-1], start=1):
        tot_weight += row_data.count("O") * row_nr
    return tot_weight


def get_state_string(data):
    return "".join([cell for row in data for cell in row])


def get_data_cycle_1e9(data):
    cycle_data = rotate_matrix(data, Direction.LEFT)
    states = {}
    for cycle in range(1, 1_000_000_000):

        for _ in range(4):
            cycle_data = rotate_matrix(move_left(cycle_data), Direction.RIGHT)

        state = get_state_string(cycle_data)

        if state in states:
            cycle_size = cycle - states[state]
            if (1_000_000_000 - cycle) % cycle_size == 0:
                break

        states[state] = cycle
    return cycle_data


states = {}


def get_matrix_after_cycle(cycle_data):
    state = get_state_string(cycle_data)
    if state in states:
        return states[state]

    for _ in range(4):
        cycle_data = rotate_matrix(move_left(cycle_data), Direction.RIGHT)

    states[state] = cycle_data
    return cycle_data


def get_data_cycle_1e9_bf(data):
    cycle_data = rotate_matrix(data, Direction.LEFT)

    for cycle in range(1, 1_000_000_000):
        if cycle % 1000 == 0:
            print(cycle)
        cycle_data = get_matrix_after_cycle(cycle_data)
    return cycle_data


if __name__ == "__main__":
    weight_1 = count_weight(rotate_matrix(move_left(rotate_matrix(data, Direction.LEFT)), Direction.RIGHT))
    print(f"Part1: {weight_1}, Check: {weight_1 == 108641}")

    weight_2 = count_weight(rotate_matrix(get_data_cycle_1e9_bf(data), Direction.RIGHT))
    print(f"Part2: {weight_2}, Check: {weight_2 == 84328}")
