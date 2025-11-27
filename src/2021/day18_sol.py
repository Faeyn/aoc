import ast

from advent_code.aoc_utils import get_nums

with open('day18input') as f:
    data = f.read().splitlines()

test = '[[[[[9,8],1],2],3],4]'
test = ast.literal_eval(test)


def find_layer(ls, res=[], d=0):
    for idx, e in enumerate(ls):
        if isinstance(e, list):
            if d == 4:
                return res
            res = find_layer(e, res + [idx], d + 1)
    return res

to_explode = find_layer(test)

if to_explode:
    cl = [x for x in test]
    for idx in to_explode:
       cl = cl[idx]

    left, right = cl

cl = [x for x in test]


def mod(ls, to_explode, left, right):
    if len(to_explode) > 1:
        left, right = mod(ls[to_explode[0]], to_explode[1:], left, right)

    for idx, e in enumerate(ls):
        if idx == to_explode[0] - 1 and left is not None:
            ls[idx] += left
            left = None

        if idx == to_explode[0] + 1 and right is not None:
            print('hi')
            ls[idx] += right
            right = None

    return left, right


test[to_explode[0]][to_explode[1]][to_explode[2]].pop(to_explode[3])
print(test)
