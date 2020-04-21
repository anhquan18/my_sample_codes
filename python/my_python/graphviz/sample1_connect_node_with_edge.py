from graphviz import Graph
from graphviz import Digraph

g = Graph(name='graph_nodes')
dg = Digraph(name='sample1_digraph_nodes')

# add nodes
g.node('1', shape='rect')
g.node('2', shape='rect')
g.node('3', shape='rect')
g.node('4', shape='rect')

# add edges
g.edge('1', '2')
g.edge('2', '3')
g.edge('3', '1')
g.edge('4', '2')

# graph with direction
dg.node('1')
dg.node('2')
dg.node('3')

dg.edge('1','2')
dg.edge('2','3')
dg.edge('3','1')
dg.edge('4','2')


#print(g)
#print(type(g))

g.render(view=True, cleanup=True, format='pdf')
#dg.render(view=True, cleanup=True, format='png')

# change format after intialize
# g.format = "svg"
