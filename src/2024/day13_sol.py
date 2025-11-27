from advent_code.aoc_utils import get_nums

with open('day13input') as f:
    data = f.read().splitlines()

buttons_a = []
buttons_b = []
prices = []
for i, row in enumerate(data):
    if i % 4 == 0:
        buttons_a.append(get_nums(row))

    if i % 4 == 1:
        buttons_b.append(get_nums(row))

    if i % 4 == 2:
        prices.append(get_nums(row))

def sol(ax, ay, bx, by, px, py):
    A = round((px - (bx / by)*py) / (ax - bx/by*ay), 3)
    B = round((py - A*ay) / by, 3)

    return int(A*3 + B) if 0 <= A == int(A) and 0 <= B == int(B) else 0

ans1 = 0
ans2 = 0
for (ax, ay), (bx, by), (px, py) in zip(buttons_a, buttons_b, prices):
    ans1 += sol(ax, ay, bx, by, px, py)
    ans2 += sol(ax, ay, bx, by, px+10000000000000, py+10000000000000)

print('Ans1: ', ans1)
print('Ans2: ', ans2)