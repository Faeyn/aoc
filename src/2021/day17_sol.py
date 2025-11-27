min_x, max_x = 211, 232
min_y, max_y = -124, -69

max_y_speed = abs(min_y) - 1
height = int(max_y_speed / 2 * (max_y_speed + 1))

print(f"Part1: {height}")


def valid_state(vx, vy):
    global local_max
    state = (0, 0, vx, vy)
    while state[1] >= min_y:
        if min_x <= state[0] <= max_x and min_y <= state[1] <= max_y:
            return True
        state = state[0] + state[2], state[1] + state[3], state[2] - 1 if state[2] > 0 else 0, state[3] - 1
    return False


pos = 0
for vx in range(max_x + 1):
    for vy in range(min_y - 1, abs(min_y) + 1):
        pos += valid_state(vx, vy)

print(max_max)
print(f"Part2: {pos}")
