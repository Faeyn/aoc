from time import sleep

from advent_code.aoc_utils import get_nums

with open('day14input') as f:
    data = f.read().splitlines()

w = 101
h = 103

def get_pos(turns):
    pos = []
    for row in data:
        px, py, vx, vy = get_nums(row)
        pos.append(((px + turns * vx) % w, (py + turns * vy) % h))
    return pos


quads = [0, 0, 0, 0]
p = get_pos(100)
for px_e, py_e in p:
    if px_e in range(w // 2) and py_e in range(h // 2):
        quads[0] += 1

    if px_e in range(w // 2) and py_e in range(h // 2 + 1, h):
        quads[1] += 1

    if px_e in range(w // 2 + 1, w) and py_e in range(h // 2 + 1, h):
        quads[2] += 1

    if px_e in range(w // 2 + 1, w) and py_e in range(h // 2):
        quads[3] += 1

ans = 1
for quad in quads:
    ans *= quad

print(ans)

# Part to 29 + i * 101 -> iteratoe over i to find the xmas tree