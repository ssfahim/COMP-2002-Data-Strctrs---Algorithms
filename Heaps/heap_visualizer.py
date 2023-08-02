# COMP 2002 - Assignment 3
# Terrence Tricco
# October 2022

from pyvis.network import Network
import math

def visualize_heap(heap, filename='heap.html'):
    """ Creates a Javascript visualization of a Heap. """

    net = Network(height='800px', layout=True)

    def build_network(net, heap, i=1):
        title = f"key={heap._data[i]}"
        net.add_node(i, label=title, level=int(math.log(i, 2)))
        if 2*i <= heap._size:
            build_network(net, heap, i=2*i)
            net.add_edge(i, 2*i)
        if 2*i+1 <= heap._size:
            build_network(net, heap, i=2*i+1)
            net.add_edge(i, 2*i+1)
        return net

    net = build_network(net, heap)
    net.show(filename)