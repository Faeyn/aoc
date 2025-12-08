from pathlib import Path
from math import prod
from collections import defaultdict
import heapq

with open(Path(__file__).parent / ".input/day08_input") as f:
    data = f.read()

data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

data = data.splitlines()
nr_con = 10 if len(data) == 20 else 1000

boxes = []
for line in data:
    boxes.append(tuple([int(x) for x in line.split(",")]))

links = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        b1, b2 = boxes[i], boxes[j]
        heapq.heappush(links, (sum([(b1[k] - b2[k]) ** 2 for k in range(3)]), b1, b2))

class Circuits:
    def __init__(self):
        self.list = []

    def union(self, b1, b2):
        new_c = set([b1, b2])

        new_cs = []
        for c in self.list:
            if b1 in c or b2 in c:
                new_c.update(c)
            else:
                new_cs.append(c)

        new_cs.append(new_c)
        self.list = new_cs
        return new_c

cs = Circuits() 
i = 0
while links:
    i += 1
    d, b1, b2 = heapq.heappop(links)

    new_c = cs.union(b1, b2)

    if i == nr_con:
        print("Part1 :", prod(sorted([len(c) for c in cs.list])[-3:]))
    
    if len(new_c) == len(data):
        print("Part2: ", b1[0] * b2[0])
        break
