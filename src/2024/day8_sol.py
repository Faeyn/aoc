from collections import defaultdict
from itertools import combinations

with open('day8_input') as f:
    data = f.read().splitlines()

map = defaultdict(list)
h = len(data)
w = len(data[0])

for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        if cell != "." and cell != '#':
            map[cell].append((row_i, col_i))

nodes2 = set()
nodes1 = set()

def update_nodes(n, c, r_d, c_d):
    n.add(c)
    if 0 <= c[0] + r_d < h and 0 <= c[1] + c_d < w:
        update_nodes(n, (c[0] + r_d, c[1] + c_d), r_d, c_d)

for k, v in map.items():
    for c1, c2 in combinations(v, 2):
        row_d = c1[0] - c2[0]
        col_d = c1[1] - c2[1]

        update_nodes(nodes2, c1, row_d, col_d)
        update_nodes(nodes2, c1, -row_d, -col_d)

        if 0 <= c1[0] + row_d < h and 0 <= c1[1] + col_d < w:
            nodes1.add((c1[0] + row_d, c1[1] + col_d))

        if 0 <= c2[0] - row_d < h and 0 <= c2[1] - col_d < w:
            nodes1.add((c2[0] - row_d, c2[1] - col_d))

print(len(nodes1))
print(len(nodes2))