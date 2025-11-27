from collections import deque

from advent_code.coord import adj4

with open('day12input') as f:
    data = f.read().splitlines()

h = len(data)
w = len(data[0])

seen = [[False] * w for _ in range(h)]

def walk(r, c):
    per, area = 4, 1
    seen[r][c] = True
    for dr, dc in adj4:
        nr, nc = r + dr, c + dc
        if nr not in range(h) or nc not in range(w):
            continue

        if data[r][c] != data[nr][nc]:
            continue
        per -= 1

        if not seen[nr][nc]:
            nps, nas = walk(nr, nc)
            area += nas
            per += nps

    return (per, area)


ans1 = 0
for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        if seen[row_i][col_i]:
            continue
        p, a = walk(row_i, col_i)
        ans1 += p * a
print('Ans1: ', ans1)

seen = [[False] * w for _ in range(h)]

ans = 0
for row_i, row in enumerate(data):
    for col_i, cell in enumerate(row):
        if seen[row_i][col_i]:
            continue

        queue = deque([(row_i, col_i)])
        r_min = float('inf')
        r_max = float('-inf')
        c_min = float('inf')
        c_max = float('-inf')

        block = []
        a = 0
        while queue:
            r, c = queue.popleft()
            block.append((r, c))
            a += 1
            seen[r][c] = True
            r_min = min(r_min, r)
            r_max = max(r_max, r)
            c_min = min(c_min, c)
            c_max = max(c_max, c)

            for dr, dc in adj4:
                nr, nc = r + dr, c + dc

                if nr in range(h) and nc in range(w) and not seen[nr][nc] and data[r][c] == data[nr][nc]:
                    queue.append((nr, nc))
                    seen[nr][nc] = True

        s = 0
        for r in range(r_min, r_max + 1):
            top = False
            bot = False
            for c in range(c_min, c_max + 1):
                if (r, c) in block:
                    if r - 1 not in range(h) or data[r - 1][c] != cell:
                        if not top:
                            s += 1
                            top = True
                    else:
                        top = False

                    if r + 1 not in range(h) or data[r + 1][c] != cell:
                        if not bot:
                            s += 1
                            bot = True
                    else:
                        bot = False
                else:
                    top = False
                    bot = False

        for c in range(c_min, c_max + 1):
            left = False
            right = False
            for r in range(r_min, r_max + 1):
                if (r, c) in block:
                    if c - 1 not in range(w) or data[r][c - 1] != cell:
                        if not left:
                            s += 1
                            left = True
                    else:
                        left = False

                    if c + 1 not in range(w) or data[r][c + 1] != cell:
                        if not right:
                            s += 1
                            right = True
                    else:
                        right = False
                else:
                    left = False
                    right = False

        ans += a * s

print('Ans2: ', ans)
