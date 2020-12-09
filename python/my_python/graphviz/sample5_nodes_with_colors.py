from graphviz import Graph

# Color name board
# https://www.graphviz.org/doc/info/colors.html
g = Graph(format='png')

g.attr('node', shape='circle', color='darkgreen')
g.attr('edge', color='darkgreen')

g.node('0', style='filled', fillcolor='gray85', fontcolor='red')
g.edge('0', '1')
g.edge('0', '2')

g.view(cleanup=True)
