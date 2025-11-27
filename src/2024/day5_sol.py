import re
from collections import defaultdict
from math import floor

from advent_code.aoc_utils import get_nums

with open('day5_input') as f:
    data = f.read().splitlines()

rs = []
us = []

is_r = True
for row in data:
    if row == '':
        is_r = False
        continue

    if is_r:
        f, l = get_nums(row)
        rs.append((int(f), int(l)))
    else:
        us.append({int(x): i for i, x in enumerate(get_nums(row))})


def create_ls(d):
    return [item[0] for item in sorted(d.items(), key=lambda item: item[1])]


def ordering(ls):
    d = {k: v for v, k in enumerate(ls)}
    d_c = {}
    while d != d_c:
        d_c = {k: v for k, v in d.items()}
        for f, l in rs:
            if d.get(f, float('-inf')) > d.get(l, float('inf')):
                d[f], d[l] = d[l], d[f]
    return create_ls(d)

ans1, ans2 = 0, 0
for u in us:
    os = ordering(u)
    ls = create_ls(u)
    mid = floor(len(ls) / 2)
    if os == ls:
        ans1 += ls[mid]
    else:
        ans2 += os[mid]

print('Ans1: ', ans1)
print('Ans2: ', ans2)
