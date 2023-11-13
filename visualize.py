from graphviz import Digraph
from ast_nodes import NumNode, BinOpNode

def visualize_ast(node, graph=None, parent=None, edge_label=''):
    if graph is None:
        graph = Digraph()
        graph.node(str(id(node)), label=str(node))

    if isinstance(node, BinOpNode):
        for child, label in [(node.left, 'left'), (node.right, 'right')]:
            graph.node(str(id(child)), label=str(child))
            graph.edge(str(id(node)), str(id(child)), label=label)
            visualize_ast(child, graph, node)

    return graph

def render_ast(node, filename='ast'):
    graph = visualize_ast(node)
    graph.render(filename, view=True)
