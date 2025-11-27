import re

from advent_code.coord import Coord

with open('day4_input') as f:
    data = f.read().splitlines()

h_data = len(data)
w_data = len(data[0])
min_axis = min(h_data, w_data)

ans = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
mas = 'MAS'
for row_i, r_data in enumerate(data):
    for col_i, cell in enumerate(r_data):
        if cell != 'X':
            continue

        for dir in dirs:
            row_c, col_c = row_i, col_i
            found_xmas = True
            for l in mas:
                row_c += dir[0]
                col_c += dir[1]

                if 0 > row_c or row_c > h_data - 1 or 0 > col_c or col_c > w_data - 1 or data[row_c][col_c] != l:
                    found_xmas = False
                    break

            if found_xmas:
                ans += 1

print('Ans1: ', ans)

ans = 0
for row_i, r_data in enumerate(data):
    for col_i, cell in enumerate(r_data):
        if cell != 'A' or 0 == row_i or row_i == h_data - 1 or 0 == col_i or col_i == w_data - 1:
            continue

        if (sorted(data[row_i + 1][col_i + 1] + data[row_i - 1][col_i - 1]) == ['M', 'S'] and
                sorted(data[row_i - 1][col_i + 1] + data[row_i + 1][col_i - 1]) == ['M', 'S']):
            ans += 1

print('Ans2: ', ans)

# Stupido

# strings = []
# for i, x in enumerate(data):
#     strings.append(x)
#     strings.append(x[::-1])
#
# for idx in range(w_data):
#     x = ''.join([row[idx] for row in data])
#     strings.append(x)
#     strings.append(x[::-1])
#
# number_diagonals = h_data+w_data-1
# for i in range(number_diagonals):
#     dia_length = i+1 if i + 1 <= min_axis else number_diagonals - i if i + 1 > number_diagonals - min_axis else min_axis
#     coord1 = (h_data - i - 1, 0) if i + 1 <= min_axis else (0, i + 1 - h_data)
#     coord2 = (i, 0) if i + 1 <= min_axis else (h_data-1, i + 1 - h_data)
#
#     s1, s2 = '', ''
#     for j in range(dia_length):
#         s2 += data[coord2[0]-j][coord2[1]+j]
#         s1 += data[coord1[0]+j][coord1[1]+j]
#
#     strings.append(s1)
#     strings.append(s1[::-1])
#     strings.append(s2)
#     strings.append(s2[::-1])
#
#
# print('Ans1: ', len(re.findall(pattern, ','.join(strings))))
