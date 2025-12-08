from pathlib import Path
from math import prod
from collections import defaultdict
import heapq

class DSU:
    def __init__(self, objects):
        self.objects = objects
        n = len(objects)
        self.parent = list(range(n))
        self.rank = [0] * n

    def index(self, object):
        try:
            return self.objects.index(object)
        except:
            print(f"Object not found {object}")

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x_ob, y_ob):
        x = self.index(x_ob)
        y = self.index(y_ob)

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

    def set(self, x_ob):
        x = self.index(x_ob)
        root = self.find(x)
        return [i for i, parent in enumerate(self.parent) if self.find(parent) == root]

    def sets(self):
        groups = defaultdict(list)
        for i in range(len(self.rank)):
            root = self.find(i)
            groups[root].append(i)
        return groups.values()


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

cs = []
i = 0
dsu = DSU(boxes)
while links:
    i += 1
    d, b1, b2 = heapq.heappop(links)

    dsu.union(b1, b2)

    if i == nr_con:
        print("Part1: ", prod(sorted([len(s) for s in dsu.sets()])[-3:]) == 40)

    if len(dsu.set(b1)) == len(data):
        print("Part2: ", b1[0] * b2[0] == 25272)
        break

