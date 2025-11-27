import networkx as nx
import matplotlib.pyplot as plt
from numpy import array

with open('day20_input') as f:
    data = f.read().splitlines()

edges = [('bu', 'br')]
for row_data in sorted(data, key=lambda string: string[0]):
    pulser, to_pulser = row_data.split(" -> ")
    pulser_type = pulser[0]
    to_pulser = to_pulser.split(", ")

    if pulser_type in "%&":
        node = pulser[1:]
    else:
        node = pulser[:2]

    edges.extend([(node, n_node) for n_node in to_pulser])

G = nx.DiGraph()
G.add_edges_from(edges)

pos = nx.spring_layout(G, k=0.2)

pos['bu'] = array([0, 3])
pos['br'] = array([0, 2.5])
pos['gf'] = array([0, -2.5])
pos['rx'] = array([0, -3])

clusters = [
    ["bx", "sp", "xc", "ff", "rv", "nx", "rn", "fn", "fk", "mv", "kn", "fx", "sk", "hr"],
    ["jq", "sv", "jt", "qt", "lj", "vk", "nk", "xk", "jm", "lp", "vp", "fb", "zb", "dt"],
    ["nv", "qs", "bc", "xb", "jf", "xm", "gv", "mh", "th", "hx", "nr", "jh", "vh", "cj", ],
    ["jp", "pg", "kt", "mb", "jc", "ph", "dx", "ct", "kd", "pp", "pz", "hp", "tx", "vr"]
]

cluster_pos = [-6, -2, 2, 6]

for index, cluster in enumerate(clusters):
    new_pos = nx.kamada_kawai_layout(G.subgraph(cluster[2:]))

    offset = array([cluster_pos[index], 0])  # Adjust the offset as needed
    new_pos = {node: pos + offset for node, pos in new_pos.items()}

    pos.update(new_pos)

pos['bx'] = array([cluster_pos[0], 1.5])
pos['jq'] = array([cluster_pos[1], 1.5])
pos['nv'] = array([cluster_pos[2], 1.5])
pos['jp'] = array([cluster_pos[3], 1.5])

pos['sp'] = array([cluster_pos[0], -1.5])
pos['sv'] = array([cluster_pos[1], -1.5])
pos['qs'] = array([cluster_pos[2], -1.5])
pos['pg'] = array([cluster_pos[3], -1.5])

nx.draw_networkx_nodes(G, pos, node_size=300)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)

plt.show()
