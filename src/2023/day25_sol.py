import re
from collections import defaultdict

import networkx as nx
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
        if ["nmv", "thl"] in [[c_node, node], [node, c_node]]:
            continue

        if ["fxr", "fzb"] in [[c_node, node], [node, c_node]]:
            continue

        if ["mbq", "vgk"] in [[c_node, node], [node, c_node]]:
            continue

        paths[node].append(c_node)
        paths[c_node].append(node)

        edges.append((node, c_node))

print(len(edges))

queue = ["nmv"]
visited = set()

while queue:
    node = queue.pop(0)
    visited.add(node)

    for n_node in paths[node]:
        if n_node not in visited and n_node not in queue:
            queue.append(n_node)

print((len(nodes) - len(visited)) * len(visited))

G = nx.DiGraph()
G.add_nodes_from(list(nodes))
G.add_edges_from(edges)

pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

plt.figure(figsize=(20, 10))
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()
