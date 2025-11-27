import heapq
import itertools
from functools import cache

from advent_code.aoc_utils import get_nums, get_location_mapper
from advent_code.coord import adj4

with open('day21input') as f:
    data = f.read().splitlines()

numpad = """789
456
123
.0A
""".splitlines()

dpad = """.^A
<v>""".splitlines()

minpad = """12
0A""".splitlines()

min_loc = get_location_mapper(minpad)
num_loc = get_location_mapper(numpad)
dir_loc = get_location_mapper(dpad)

dir_map = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}

cache = {}


def dfs_path(sy, sx, ey, ex, seen, path, l):
    if (sy, sx, ey, ex, tuple(seen), tuple(path), l) in cache:
        return cache[(sy, sx, ey, ex, tuple(seen), tuple(path), l)]

    m = dpad if l != 25 else numpad

    h = len(m)
    w = len(m[0])

    n_seen = [x for x in seen] + [(sy, sx)]

    if (sy, sx) == (ey, ex):
        if l > 0:
            l_path = 0
            c_char = 'A'
            for e_char in path + ['A']:
                sly, slx = dir_loc[c_char]
                ely, elx = dir_loc[e_char]
                l_path += dfs_path(sly, slx, ely, elx, [], [], l - 1)
                c_char = e_char
            cache[(sy, sx, ey, ex, tuple(seen), tuple(path), l)] = l_path
            return l_path
        else:
            cache[(sy, sx, ey, ex, tuple(seen), tuple(path), l)] = len(path) + 1
            return len(path) + 1

    branches = []
    for dy, dx in adj4:
        ny, nx = sy + dy, sx + dx

        if ny not in range(h) or nx not in range(w) or m[ny][nx] == '.' or (ny, nx) in n_seen:
            continue

        branch = dfs_path(ny, nx, ey, ex, n_seen, [x for x in path] + [dir_map[(dy, dx)]], l)

        if branch:
            branches.append(branch)

    if branches:
        cache[(sy, sx, ey, ex, tuple(seen), tuple(path), l)] = min(branches)
        return min(branches)
    else:
        return None


ans = 0
for row in data:
    num = get_nums(row)[0]
    p = 0
    c = 'A'
    for n in row:
        cy, cx = num_loc[c]
        ny, nx = num_loc[n]
        p += dfs_path(cy, cx, ny, nx, [], [], 25)
        c = n

    ans += p * num

print(ans)
