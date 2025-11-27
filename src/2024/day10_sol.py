from advent_code.coord import Coord

with open('day10_input') as f:
    data = f.read().splitlines()

# data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732""".splitlines()

starts = []
h = len(data)
w = len(data[0])

for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        if cell == '0':
            starts.append(Coord(row_i, col_i))

ans = 0

dirs = [Coord(x, y) for x, y in [(0,1), (1, 0), (0, -1), (-1, 0)]]

def walk(pos, nr):
    if nr == 9:
        return [pos]

    ends = []
    for dir in dirs:
        pos_n = pos + dir
        if 0 <= pos_n.row < h and 0 <= pos_n.col < w:
            if data[pos_n.row][pos_n.col] == '.':
                continue
            nr_n = int(data[pos_n.row][pos_n.col])
            if nr + 1 == nr_n:
                ends.extend(walk(pos_n, nr_n))
    return ends

ans = 0
for start in starts:
    ans += len(walk(start, 0))

print(ans)