import graphviz


def grapher(nodes, edges):
    graph = graphviz.Digraph('MyGraph')

    # Add nodes to the graph
    for node in nodes:
        graph.node(str(node))

    for edge in edges:
        graph.edge(*edge)

    # Save the graph visualization to a file (e.g., in PNG format)
    graph.render('output', format='png', cleanup=True)
