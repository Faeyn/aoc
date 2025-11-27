import heapq

with open('day16input') as f:
    data = f.read().splitlines()

map = [list(row) for row in data]
dir_mapping = {(0, 1): [(1, 0, 1), (1001, -1, 0), (1001, 1, 0), (2001, 0, -1)],
               (0, -1): [(1, 0, -1), (1001, -1, 0), (1001, 1, 0), (2001, 0, 1)],
               (1, 0): [(1, 1, 0), (1001, 0, 1), (1001, 0, -1), (2001, -1, 0)],
               (-1, 0): [(1, -1, 0), (1001, 0, 1), (1001, 0, -1), (2001, 1, 0)]
               }
h = len(map)
w = len(map[0])

for row_i, row in enumerate(map):
    for col_i, cell in enumerate(row):
        if cell == 'S':
            start = (row_i, col_i)

        if cell == 'E':
            end = (row_i, col_i)


def bfs_walker(start, start_direction):
    queue = []
    heapq.heappush(queue, (0, start, start_direction))
    seen = {start: 0}

    while queue:
        points, (r, c), (xr, xc) = heapq.heappop(queue)

        for p, dr, dc in dir_mapping[(xr, xc)]:
            np = points + p
            nr = r + dr
            nc = c + dc

            if nr in range(h) and nc in range(w) and map[nr][nc] != '#':
                if (nr, nc) not in seen or seen[(nr, nc)] > np:
                    seen[(nr, nc)] = np
                    heapq.heappush(queue, (np, (nr, nc), (dr, dc)))

    return seen


walk1 = bfs_walker(start, (0, 1))
print('Ans1: ', walk1[end])

walk2 = bfs_walker(end, (1, 0))

# ans2 = 0
# for node, points in walk1.items():
#     if ans1 - walk2[node] == points:
#         ans2 += 1
#
# for node, points in walk2.items():
#     print(node, walk1[node], ans1 - points)
#
#
# print('Ans2: ', ans2)









# end_points = walk1[end]
#
# queue = []
# heapq.heappush(queue, (0, end, (1, 0)))
# seen = {end: 0}
#
# while queue:
#     points, (r, c), (xr, xc) = heapq.heappop(queue)
#
#     for p, dr, dc in dir_mapping[(xr, xc)]:
#         np = points + p
#         nr = r + dr
#         nc = c + dc
#
#         if nr in range(h) and nc in range(w) and map[nr][nc] != '#':
#             if (nr, nc) not in seen or seen[(nr, nc)] > np:
#                 seen[(nr, nc)] = np
#                 heapq.heappush(queue, (np, (nr, nc), (dr, dc)))
#
# def dfs_walk(pos, cd, pts, path):
#     r, c = pos
#     if pts > seen[pos] + 1000:
#         return []
#
#     if pos == end:
#         if pts == end_points:
#             return path
#         else:
#             return []
#
#     if pts > end_points:
#         return []
#
#     res_path = set()
#     for p, dr, dc in dir_mapping[cd]:
#         np = pts + p
#         nr = r + dr
#         nc = c + dc
#
#         if nr in range(h) and nc in range(w) and map[nr][nc] != '#':
#             if (nr, nc) not in path:
#                 res_path.update(dfs_walk((nr, nc), (dr, dc), np, path + [(nr, nc)]))
#
#     return res_path
#
#
# print('Ans2: ', len(dfs_walk(start, (0, 1), 0, [start])))
