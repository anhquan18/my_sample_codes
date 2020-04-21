from graphviz import Digraph

g = Digraph(format='png')

for i in range(3):
    g.node(str(i), label='state{0}'.format(i+1))

edges = [ [0, 0], [0, 1], [1, 0], [1, 2], [2, 0] ]
edge_labels = ['0.5', '0.3', '0.7', '1.0', 'Hello World']

for i, e in enumerate(edges):
    g.edge(str(e[0]), str(e[1]), label=edge_labels[i])
g.view(cleanup=True)
