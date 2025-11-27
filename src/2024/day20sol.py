import heapq
from collections import namedtuple, defaultdict

from advent_code.coord import adj4

with open('day20input') as f:
    data = f.read().splitlines()

path = set()
for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        if cell == 'S':
            start = (row_i, col_i)

        if cell == 'E':
            end = (row_i, col_i)

        if cell != '#':
            path.add((row_i, col_i))

h = len(data)
w = len(data[0])

q = []
heapq.heappush(q, (0, start))
base_distances = {x: float('inf') for x in path}
while q:
    dist, current_c = heapq.heappop(q)
    base_distances[current_c] = dist

    for dr, dc in adj4:
        nr, nc = dr + current_c[0], dc + current_c[1]

        if nr in range(h) and nc in range(w) and data[nr][nc] != '#':
            if base_distances[(nr, nc)] > dist + 1:
                heapq.heappush(q, (dist + 1, (nr, nc)))


def find_skip(start, cut_distance):
    # Find all path nodes in cut_distance range
    within_range = set()
    for r in range(-cut_distance, cut_distance + 1):
        for c in range(-cut_distance + abs(r), cut_distance + 1 - abs(r)):
            within_range.add((start[0] + r, start[1] + c))

    possible_cuts = within_range.intersection(path)

    effective_cuts = []
    for c in possible_cuts:
        d = abs(start[0] - c[0]) + abs(start[1] - c[1])
        if d < base_distances[c] - base_distances[start]:
            effective_cuts.append(base_distances[c] - base_distances[start] - d)
    return effective_cuts


ans1, ans2 = 0, 0
for i_r in range(h):
    for i_c in range(w):
        if data[i_r][i_c] == '#':
            continue

        ans1 += sum([1 for c in find_skip((i_r, i_c), 2) if c >= 100])
        ans2 += sum([1 for c in find_skip((i_r, i_c), 20) if c >= 100])

print('Ans1: ', ans1)
print('Ans2: ', ans2)