from graphviz import Graph

g = Graph(format='png')

# attr will add attribute directly to the source?
# and node or edge or graph create after that will be create with default value of attr
g.attr('node', shape='circle') # first argument can also be graph or edge 
g.node('0')
g.node('1')
g.attr('node', shape='square')
g.node('2')
g.attr('node', shape='star')
g.node('3')

g.node('4', shape='circle')

g.view()
