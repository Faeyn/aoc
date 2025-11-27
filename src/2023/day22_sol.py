from collections import defaultdict, namedtuple
from typing import List

from icecream import ic

with open("day22_input") as f:
    data = f.read().splitlines()

Brick = namedtuple("Brick", ["x", "y", "z", "i"])
Range = namedtuple("Range", ["lower", "upper"])


def overlapping(range_1: Range, range_2: Range):
    return range_2.upper > range_1.lower and range_1.upper > range_2.lower


bricks = []
for brick_i, brick_data in enumerate(data):
    head, tail = brick_data.split("~")
    head = [eval(x) for x in head.split(",")]
    tail = [eval(x) + 1 for x in tail.split(",")]

    bricks.append(Brick(*[Range(head[i], tail[i]) for i in range(len(head))], brick_i))

stack: List[Brick] = []
supported_by = []
supports = defaultdict(list)

for brick in sorted(bricks, key=lambda _brick: _brick.z.lower):
    supported, max_z_base = ["g"], 0

    for s_brick in stack:
        z_base = s_brick.z.upper

        if overlapping(s_brick.x, brick.x) and overlapping(s_brick.y, brick.y):

            if max_z_base < z_base:
                supported = [s_brick.i]
                max_z_base = z_base

            elif max_z_base == z_base:
                supported.append(s_brick.i)

    supported_by.append(supported)
    supports[tuple(supported)].append(brick.i)

    z_range = Range(max_z_base, brick.z.upper - (brick.z.lower - max_z_base))
    stack.append(Brick(brick.x, brick.y, z_range, brick.i))

cannot_remove = set(support[0] for support in supported_by if len(support) == 1)
cannot_remove.remove('g')

can_remove = len(data) - len(cannot_remove)
print(f"Part1: {can_remove}: Check is {can_remove == 503}")

bricks_collapsing = 0
for brick_i in range(len(data)):
    removed = {brick_i}

    for support_set in supports:
        if set(support_set).issubset(removed):
            removed.update(supports[support_set])
            collapsing = True

    collapsed = len(removed) - 1
    bricks_collapsing += collapsed

print(f"Part2: {bricks_collapsing}: Check is {bricks_collapsing == 98431}")
