import math
import re
import random
import numpy as np
from numpy.linalg import LinAlgError

file = "day24_input"
with open(file) as f:
    data = f.read().splitlines()


class Hail:
    def __init__(self, px, py, pz, vx, vy, vz):
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz

    @property
    def set(self):
        return [self.px, self.py, self.pz, self.vx, self.vy, self.vz]

    def __repr__(self):
        return f"{self.px}, {self.py}, {self.pz}, {self.vx}, {self.vy}, {self.vz}"


def hail_x(_hail1, _hail2):
    try:
        px1, py1, pz1, vx1, vy1, vz1 = _hail1.set
        px2, py2, pz2, vx2, vy2, vz2 = _hail2.set

        xy = (py1 - py2 - vy1 / vx1 * px1 + vy2 / vx2 * px2) / (vy2 / vx2 - vy1 / vx1)
        xz = (pz1 - pz2 - vz1 / vx1 * px1 + vz2 / vx2 * px2) / (vz2 / vx2 - vz1 / vx1)
        return math.isclose(xy, xz, rel_tol=.15e-13)
    except ZeroDivisionError:
        print("Zero division")


hails = [Hail(*[eval(x) for x in re.findall(r"-?\w+", row)]) for row in data]


def hail_path_intersection(_hail1, _hail2, min_range, max_range):
    _a = np.array([[_hail1.vx, -_hail2.vx], [_hail1.vy, -_hail2.vy]])
    _b = np.array([_hail2.px - _hail1.px, _hail2.py - _hail1.py])
    try:
        t1, t2 = np.linalg.solve(_a, _b)

        if t1 < 0 or t2 < 0:
            return False

        _x = _hail1.px + t1 * _hail1.vx
        _y = _hail1.py + t1 * _hail1.vy

        if min_range <= _x <= max_range and min_range <= _y <= max_range:
            return True

    except LinAlgError:
        return False


min_area = 200_000_000_000_000
max_area = 400_000_000_000_000

intersections = 0
for i, hail1 in enumerate(hails):
    for hail2 in hails[i + 1:]:
        if hail_path_intersection(hail1, hail2, min_area, max_area):
            intersections += 1

print(f"Part1: {intersections}, Check is {intersections == 15889}")

check, x, y, z = 0, 0, 0, 0
while check != 300:
    start = random.randint(0, len(hails) - 9)
    hail1, hail2, hail3, hail4, hail5, hail6, hail7, hail8 = [hails[i] for i in range(start, start + 8)]

    a = np.array([
        [hail2.vy - hail1.vy, hail1.vx - hail2.vx, 0, hail1.py - hail2.py, hail2.px - hail1.px, 0],
        [hail4.vy - hail3.vy, hail3.vx - hail4.vx, 0, hail3.py - hail4.py, hail4.px - hail3.px, 0],
        [hail6.vy - hail5.vy, hail5.vx - hail6.vx, 0, hail5.py - hail6.py, hail6.px - hail5.px, 0],
        [hail8.vy - hail7.vy, hail7.vx - hail8.vx, 0, hail7.py - hail8.py, hail8.px - hail7.px, 0],
        [hail2.vz - hail1.vz, 0, hail1.vx - hail2.vx, hail1.pz - hail2.pz, 0, hail2.px - hail1.px],
        [hail4.vz - hail3.vz, 0, hail3.vx - hail4.vx, hail3.pz - hail4.pz, 0, hail4.px - hail3.px],
    ])
    b = np.array([
        hail1.py * hail1.vx - hail1.px * hail1.vy - hail2.py * hail2.vx + hail2.px * hail2.vy,
        hail3.py * hail3.vx - hail3.px * hail3.vy - hail4.py * hail4.vx + hail4.px * hail4.vy,
        hail5.py * hail5.vx - hail5.px * hail5.vy - hail6.py * hail6.vx + hail6.px * hail6.vy,
        hail7.py * hail7.vx - hail7.px * hail7.vy - hail8.py * hail8.vx + hail8.px * hail8.vy,
        hail1.pz * hail1.vx - hail1.px * hail1.vz - hail2.pz * hail2.vx + hail2.px * hail2.vz,
        hail3.pz * hail3.vx - hail3.px * hail3.vz - hail4.pz * hail4.vx + hail4.px * hail4.vz,
    ])

    x, y, z, dx, dy, dz = np.linalg.solve(a, b)
    check = sum(hail_x(Hail(x, y, z, dx, dy, dz), hail) for hail in hails)

print(f"Part2: {int(sum([x, y, z]))}: Check is {int(sum([x, y, z])) == 801386475216902}")
