import heapq
from collections import defaultdict

from advent_code.aoc_utils import get_nums
from advent_code.coord import adj4, adj8

with open('day18input') as f:
    data = f.read().splitlines()

wh = 71

cors = []
for row in data:
    x, y = get_nums(row)
    cors.append((x, y))


active_cor = set(cors[:1024])
start = (0, 0)
queue = []
heapq.heappush(queue, (0, start))
seen = {start: 0}

while queue:
    steps, (r, c) = heapq.heappop(queue)

    for dr, dc in adj4:
        nr = r + dr
        nc = c + dc
        n_steps = steps + 1

        if nr in range(wh) and nc in range(wh) and (nr, nc) not in active_cor:
            if (nr, nc) not in seen or seen[(nr, nc)] > n_steps:
                seen[(nr, nc)] = n_steps
                heapq.heappush(queue, (n_steps, (nr, nc)))


print('Ans1: ', seen[(70, 70)])


class Group:
    def __init__(self, id, ls):
        self.id = id
        self.upper_bound = False
        self.lower_bound = False
        self.right_bound = False
        self.left_bound = False
        self.adjs = set()
        self.add_adjacents(ls)

    def add_adjacents(self, ls):
        for r, c in ls:
            if r == -1:
                self.upper_bound = True
            if r == wh:
                self.lower_bound = True
            if c == -1:
                self.left_bound = True
            if c == wh:
                self.right_bound = True
        self.adjs.update([x for x in ls])

    def blocking(self):
        return (self.upper_bound or self.right_bound) and (self.lower_bound or self.left_bound)


def find_blocking_cor():
    groups = {}
    i_group = 0
    for cor in cors:
        adj = [(cor[0] + dx, cor[1] + dy) for dx, dy in adj8]

        combine = []
        for idx_g, g in groups.items():
            if cor in g.adjs:
                combine.append(idx_g)
                g.add_adjacents(adj)

        if len(combine) == 0:
            groups[i_group] = Group(i_group, adj)
            i_group += 1

        if len(combine) > 1:
            for i1, i2 in zip(combine, combine[1:]):
                groups[i2].add_adjacents(groups[i1].adjs)
                groups.pop(i1)

        for g in groups.values():
            if g.blocking():
                return ','.join(str(x) for x in cor)


print('Ans2: ', find_blocking_cor())
