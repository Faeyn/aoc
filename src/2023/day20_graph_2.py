import graphviz

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

nodes = [x for y in edges for x in y]

graph = graphviz.Digraph('MyGraph')

# Add nodes to the graph
for node in nodes:
    graph.node(node)

for edge in edges:
    # Add edges to the graph
    graph.edge(*edge)

# Save the graph visualization to a file (e.g., in PNG format)
graph.render('output', format='png', cleanup=True)
