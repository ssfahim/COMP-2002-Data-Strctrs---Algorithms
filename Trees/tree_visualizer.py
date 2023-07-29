# COMP 2002 - Assignment 2
# Terrence Tricco
# October 2022

from pyvis.network import Network
import math

def visualize_tree(tree, filename='tree.html'):
    """ Creates a Javascript visualization of a BSPTree. """

    net = Network(height='800px', layout=True)

    def build_network(net, node, i=1):
        title = f"length={node.length}\npos={node.position}\nvalue={node.value}"
        net.add_node(i, label=title, level=int(math.log(i, 2)))
        if node.left:
            build_network(net, node.left, i=2 * i)
            net.add_edge(i, 2 * i)
        if node.right:
            build_network(net, node.right, i=2 * i + 1)
            net.add_edge(i, 2 * i + 1)
        return net

    net = build_network(net, tree._root)
    net.show(filename)