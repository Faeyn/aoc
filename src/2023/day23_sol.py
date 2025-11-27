from advent_code.coord import Coord
from advent_code.graph_nodes import grapher

with open("day23_input") as f:
    data = f.read().splitlines()

width = len(data)
height = len(data[0])

start = Coord(0, 1)
end = Coord(len(data) - 1, len(data[0]) - 2)
queue = [start]

slide_mapping = {">": (0, 1), "v": (1, 0)}

nodes = {start, end}
edges = []
visited = set()

while queue:
    c_coord = queue.pop(0)
    visited.add(c_coord)

    valid_n_coord = 0

    if data[c_coord.row][c_coord.col] in slide_mapping:
        queue.append(c_coord + slide_mapping[data[c_coord.row][c_coord.col]])
        continue

    for n_coord in c_coord.get_adjacent():
        if not (0 <= n_coord.row < height and 0 <= n_coord.col < width):
            continue

        if data[n_coord.row][n_coord.col] == "#":
            continue

        valid_n_coord += 1

        if n_coord in visited or n_coord in queue:
            continue

        queue.append(n_coord)

    if valid_n_coord > 2:
        nodes.add(c_coord)

# print(len(nodes))
# print(nodes)

for node in nodes:
    queue = [(node, 0)]
    visited = set()

    while queue:
        c_coord, steps = queue.pop(0)
        visited.add(c_coord)

        if c_coord in nodes and node != c_coord:
            edges.append((node, c_coord, steps))
            continue

        # Part 1
        # if data[c_coord.row][c_coord.col] in slide_mapping:
        #     queue.append((c_coord + slide_mapping[data[c_coord.row][c_coord.col]], steps + 1))
        #     continue

        for n_coord in c_coord.get_adjacent():
            if not (0 <= n_coord.row < height and 0 <= n_coord.col < width):
                continue

            if data[n_coord.row][n_coord.col] == "#":
                continue

            if n_coord in visited or n_coord in [t[0] for t in queue]:
                continue

            queue.append((n_coord, steps + 1))

grapher(nodes, [[str(i) for i in edge] for edge in edges])

connections = {}
for node in nodes:
    connections[node] = {edge[1]: edge[2] for edge in edges if edge[0] == node}

node_list = list(nodes)


def get_bits(path):
    bitmask = 0
    for _node in path:
        bitmask = 1 << node_list.index(_node) | bitmask
    return bitmask


states = {}
counter = 0

# DFS
def dfs_path(path):
    global counter
    counter += 1
    if counter % 100000 == 0:
        print(counter, len(states))
    node = path[-1]

    state = (node, get_bits(path))

    if state in states:
        return states[state]

    if node == end:
        states[state] = 0
        return 0

    valid_n_nodes = 0

    max_steps = 0
    for n_node in connections[node]:
        if n_node in path:
            continue
        valid_n_nodes += 1
        max_steps = max(max_steps, dfs_path(path + (n_node,)) + connections[node][n_node])

    if valid_n_nodes == 0:
        states[state] = float("-inf")
        return float("-inf")

    states[state] = max_steps
    return max_steps


print(dfs_path((start,)))
