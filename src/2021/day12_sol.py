import re
from collections import defaultdict

with open("day12_input") as f:
    data = f.read().splitlines()

pattern = r"(\w+)"

node_connections = defaultdict(lambda: [])
for row in data:
    node_a, node_b = re.findall(pattern, row)
    node_connections[node_a].append(node_b)
    node_connections[node_b].append(node_a)

queue = ['start']


def bfs_paths(paths=[["start"]]):
    new_paths = []
    next_layer = False

    for path in paths:
        dont_visit = [node for node in path if node.islower()]
        next_nodes = node_connections[path[-1]]

        if path[-1] == "end":
            new_paths.append(path)
            continue

        if all(node in dont_visit for node in next_nodes):
            continue

        next_layer = True
        new_paths.extend(
            [[node for node in path] + [next_node] for next_node in next_nodes if next_node not in dont_visit])

    if next_layer:
        return bfs_paths(new_paths)

    return new_paths


print(f"Part1: {len(bfs_paths())}")


def bfs_paths_2(paths=[["start"]]):
    new_paths = []
    next_layer = False

    for path in paths:
        dont_visit = ["start"]
        if any(path.count(node) == 2 for node in path if node.islower()):
            dont_visit = [node for node in path if node.islower()]

        next_nodes = node_connections[path[-1]]
        if path[-1] == "end":
            new_paths.append(path)
            continue

        if all(node in dont_visit for node in next_nodes):
            continue

        next_layer = True
        new_paths.extend(
            [[node for node in path] + [next_node] for next_node in next_nodes if next_node not in dont_visit])

    if next_layer:
        return bfs_paths_2(new_paths)

    return paths


print(f"Part2: {len(bfs_paths_2())}")
