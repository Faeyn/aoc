from collections import deque

with open("day17_input") as f:
    prob_input = f.read()

move_mapping = {"<": -1, ">": 1}

horizontal_moves = deque([])
move_index = 0
for horizontal_move in prob_input:
    horizontal_moves.append(move_mapping[horizontal_move])

stack = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
shapes = [[(0, 0), (1, 0), (2, 0), (3, 0)], [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
          [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (0, 1), (1, 0), (1, 1)]]

def moved_shape(move_x, move_y, shape):
    new_shape = []
    for x, y in shape:
        new_shape.append((x + move_x, y + move_y))
    return new_shape


def get_height(_stack):
    height = 0
    for _, y in _stack:
        height = max(height, y)

    return height


def is_colliding(_stack, _shape):
    for x, y in _shape:
        if (x, y) in _stack:
            return True

        if x == -1 or x == 7:
            return True

    return False


memory = {}

for nth_rock in range(int(1e12)):
    shape = shapes[nth_rock % len(shapes)]
    height = get_height(stack)

    key = (tuple(shape), tuple(horizontal_moves))
    if key in memory:
        print(nth_rock)
        nth_rock_cycle, cycle_height = memory[key]
        n_cycles, remainder = divmod(1e12 - nth_rock, nth_rock - nth_rock_cycle)
        if remainder == 0:
            print(height + (height - cycle_height) * n_cycles)
            break
    else:
        memory[key] = nth_rock, height

    shape = moved_shape(2, height + 4, shape)

    if nth_rock == 2022: print(height)

    while True:
        horizontal_move = horizontal_moves.popleft()
        horizontal_moves.append(horizontal_move)

        check_shape = moved_shape(horizontal_move, 0, shape)
        shape = check_shape if not is_colliding(stack, check_shape) else shape

        check_shape = moved_shape(0, -1, shape)

        if not is_colliding(stack, check_shape):
            shape = check_shape
        else:
            stack.extend(shape)
            break
