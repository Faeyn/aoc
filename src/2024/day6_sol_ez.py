from collections import defaultdict
from advent_code.coord import Coord, dir_map


with open('day6_input') as f:
    data = f.read().splitlines()

H = len(data)
W = len(data[0])

obs = set()
for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        if cell == '#':
            obs.add(Coord(row_i, col_i))
        if cell == '^':
            c_c = Coord(row_i, col_i)

c_s = c_c
# orts = [dir_map[d] for d in 'URDL']
# ort_i = 0
#
# visited = {c_c}
# while True:
#     c_n = c_c + orts[ort_i]
#     if c_n in obs:
#         ort_i = (ort_i + 1) % 4
#         continue
#
#     if c_n.row < 0 or c_n.row == H or c_n.col < 0 or c_n.col == W:
#         break
#
#     visited.add(c_n)
#     c_c = c_n
#
# print(len(visited))



no_obs = set(obs)
no_obs.add(c_s)

orts = [dir_map[d] for d in 'URDL']
ort_i = 0

ans = 0
for row in range(H):
    for col in range(W):
        if Coord(row, col) in no_obs:
            continue

        c_c = c_s
        ort_i = 0
        o_c = Coord(row, col)
        visited = {(c_s, ort_i)}
        while True:
            c_n = c_c + orts[ort_i]
            if c_n in obs or c_n == o_c:
                ort_i = (ort_i + 1) % 4
                continue

            if c_n.row < 0 or c_n.row == H or c_n.col < 0 or c_n.col == W:
                break

            if (c_n, ort_i) in visited:
                ans += 1
                break

            visited.add((c_n, ort_i))
            c_c = c_n

print(ans)