from graphviz import Graph

g = Graph(format='png')

g.attr('node', shape='circle', label='')

edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]

for i, j in edges:
    g.edge(str(i), str(j)) 

g.view(cleanup=True)
print(g)
