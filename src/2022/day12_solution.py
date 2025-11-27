with open("day12_input") as f:
    lines = f.read().splitlines()

height_map = [[letter for letter in row] for row in lines]
distance_map = [[float("inf") for _ in row] for row in lines]

for i_y, row in enumerate(height_map):
    for i_x, col in enumerate(row):
        if col == "S":
            y_start = i_y
            x_start = i_x
            height_map[y_start][x_start] = "a"
        elif col == "E":
            y_end = i_y
            x_end = i_x
            height_map[y_end][x_end] = "z"

y_bound = len(distance_map) - 1
x_bound = len(distance_map[0]) - 1

moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
# track = [(y_start, x_start)]
# distance_map[y_start][x_start] = 0

track = [(y_end, x_end)]
distance_map[y_end][x_end] = 0

while len(track) > 0:
    y_current, x_current = track.pop(0)
    h_current = ord(height_map[y_current][x_current])
    d_current = distance_map[y_current][x_current]
    d_next = d_current + 1

    for y_move, x_move in moves:
        y_next = y_current + y_move
        x_next = x_current + x_move
        if 0 <= x_next <= x_bound and 0 <= y_next <= y_bound:

            h_next = ord(height_map[y_next][x_next])

            letter_current = height_map[y_current][x_current]
            letter_next = height_map[y_next][x_next]

            # if h_next <= h_current + 1:
            if h_next >= h_current - 1:

                if distance_map[y_next][x_next] > d_next:
                    distance_map[y_next][x_next] = d_next
                    track.append((y_next, x_next))

# for row, row2 in zip(distance_map, height_map):
#     print([(str(x).zfill(3), x2) for x, x2 in zip(row, row2)])

print(f"Part1: {distance_map[y_start][x_start]}")
print(
    f"Part2: {min([dist_val for dist_row, height_row in zip(distance_map, height_map) for dist_val, height_val in zip(dist_row, height_row) if height_val == 'a'])}")
