import itertools
from collections import defaultdict
from itertools import combinations

from advent_code.aoc_utils import get_words

with open('day23input') as f:
    data = f.read().splitlines()

connections = defaultdict(list)
for row in data:
    pc1, pc2 = get_words(row)
    connections[pc1].append(pc2)
    connections[pc2].append(pc1)

tripplets = set()
for pc, conns in connections.items():
    for c1, c2 in itertools.product(conns, conns):
        if c2 in connections[c1]:
            tripplets.add(tuple(sorted([pc, c1, c2])))

ans = 0
for trip in tripplets:
    for pc in trip:
        if pc.startswith('t'):
            ans += 1
            break

print(ans)

def find_full_con(main_node, known_nodes):
    groupsize = []
    seen = set()
    no_new_nodes = True
    for node in connections[main_node]:
        if known_nodes.issubset(set(connections[node])) and node not in known_nodes and node not in seen:
            no_new_nodes = False
            g = find_full_con(main_node, set(list(known_nodes) + [node]))
            seen.update(g)
            groupsize.append(g)

    if no_new_nodes:
        return known_nodes
    return max(groupsize, key=len)

groups = []
for node in connections.keys():
    groups.append(find_full_con(node, set([node])))

print(",".join(sorted(list(max(groups, key=len)))))