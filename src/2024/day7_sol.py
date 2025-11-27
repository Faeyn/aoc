from advent_code.aoc_utils import get_nums

with open('day7_input') as f:
    data = f.read().splitlines()

sls, nrs = [], []
for row in data:
    sl, nr = row.split(':')
    sls.append(get_nums(sl))
    nrs.append(get_nums(nr))


def add_mul_cat(ins: list, sol: int, tot: int, with_cat: bool = False):
    if tot == sol and len(ins) == 0:
        return True

    if tot > sol or len(ins) == 0:
        return False

    nor = ins[0]
    if add_mul_cat(ins[1:], sol, tot + nor, with_cat):
        return True
    elif add_mul_cat(ins[1:], sol, tot * nor, with_cat):
        return True
    elif with_cat and add_mul_cat(ins[1:], sol, int(str(tot) + str(nor)), with_cat):
        return True
    return False


ans1, ans2 = 0, 0
for sl, nr in zip(sls, nrs):
    ans1 += sl[0] if add_mul_cat(nr[1:], sl[0], nr[0]) else 0
    ans2 += sl[0] if add_mul_cat(nr[1:], sl[0], nr[0], True) else 0
print('Ans1: ', ans1)
print('Ans2: ', ans2)
