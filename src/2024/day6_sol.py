from collections import defaultdict
from operator import lt, gt

from advent_code.coord import Coord, dir_map


with open('day6_input') as f:
    data = f.read().splitlines()

H = len(data)
W = len(data[0])
obs = defaultdict(lambda: defaultdict(list))
for row_i, row in enumerate(data):
    for col_i, col in enumerate(row):
        if col == '#':
            obs['row'][row_i].append(col_i)
            obs['col'][col_i].append(row_i)

        if col == '^':
            p_c = Coord(row_i, col_i)

visited = {p_c}
ort_i = 0
ort = [('col', lt, -1, 1), ('row', gt, 0, -1), ('col', gt, -1, -1), ('row', lt, 0, 1)]
rev = {'row': 'col', 'col': 'row'}



axis, comp, pos, stop = ort[ort_i]
a_c = p_c.__getattribute__(axis)
a_inv_c = p_c.__getattribute__(rev[axis])



p_n = Coord(**{rev[axis]: [x for x in obs[axis][a_c] if comp(x, a_inv_c)][pos] + stop, axis: a_c})
a_n = p_n.__getattribute__(axis)
a_inv_n = p_n.__getattribute__(rev[axis])
print(p_n, p_c)

for r in range(min(a_inv_n, a_inv_c), max(a_inv_n, a_inv_c)+1):
    visited.add(Coord(**{axis: r, rev[axis]: a_c}))
print(visited)
