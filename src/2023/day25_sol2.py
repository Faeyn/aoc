import math
import random
import re
from collections import defaultdict
import numpy as np
import networkx as nx
import scipy.optimize
from icecream import ic
import matplotlib.pyplot as plt

with open("day25_input") as f:
    data = f.read()
    nodes = set(re.findall("(\w+)", data))
    data = data.splitlines()

edges = []
paths = defaultdict(list)
for row in data:
    node, connections = row.split(": ")
    for c_node in connections.split(" "):
        paths[node].append(c_node)
        paths[c_node].append(node)

        edges.append((node, c_node))

pos = {node: ((random.random() - 0.5) * 1e2, (random.random() - 0.5) * 1e2) for node in nodes}

nodes = list(nodes)
G = nx.Graph()
G.add_edges_from(edges)

pos_ar = np.array([x for y in nodes for x in pos[y]])

k = 0.5
g = 0.01
A = np.array([[float(0) for _ in range(len(nodes) * 2)] for _ in range(len(nodes) * 2)])
for i_n, node in enumerate(nodes):
    for n_node in paths[node]:
        j_n = nodes.index(n_node)
        A[i_n * 2][i_n * 2] -= k
        A[i_n * 2 + 1][i_n * 2 + 1] -= k
        A[i_n * 2][j_n * 2] += k
        A[i_n * 2 + 1][j_n * 2 + 1] += k


def iteration(p, alpha):
    b = np.array([float(0) for _ in range(len(nodes) * 2)])
    for i_n, node in enumerate(nodes):
        bx = 0
        by = 0
        for j_n in range(len(nodes)):
            if nodes[j_n] in paths[i_n]:
                continue

            val = p[i_n * 2] - p[j_n * 2]
            if val != 0:
                bx += np.sign(val) * g / val**2 / abs(p[i_n * 2])

            val = p[i_n * 2 + 1] - p[j_n * 2 + 1]
            if val != 0:
                by += np.sign(val) * g / val**2 / abs(p[i_n * 2 + 1])

        b[i_n * 2] += bx
        b[i_n * 2 + 1] += by

    c = b + p @ A
    return p + c * 0.5 * alpha


for alpha in range(100):
    print(alpha)
    pos_ar = iteration(pos_ar, max(0.5 * np.exp(-0.01 * alpha), 0.3))

    pos = {node: (pos_ar[i * 2], pos_ar[i * 2 + 1]) for i, node in enumerate(nodes)}

    if alpha % 10 == 0:

        plt.figure()
        plt.axvline(x=0)
        plt.axhline(y=0)

        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos)

        plt.show()
