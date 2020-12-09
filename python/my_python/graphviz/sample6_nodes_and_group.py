from graphviz import Graph

# use subgraph to create a group of nodes
g =  Graph(name='sample6', format='png')

g.attr('node', shape='circle')

with g.subgraph(name='cluster_root') as c:
    c.attr(color='white', label='root')
    #c.node('0')
    c.edges( [('0', '1'), ('0', '2')])


with g.subgraph(name='cluster_01') as c:
    c.attr(color='blue')
    c.edges([('1', '3'), ('1', '4')])

    with c.subgraph(name='cluster_013') as cc0:
        cc0.attr(color='darkgreen', label='cluster_013')
        cc0.node('3')
    with c.subgraph(name='cluster_014') as cc1:
        cc1.attr(color='orchid1', label='cluster_014')
        cc1.node('4')


with g.subgraph(name='cluster_02') as c:
    c.attr(color='blue')
    c.edges([('2', '5'), ('2', '6')])

    with c.subgraph(name='cluster_025') as cc0:
        cc0.attr(color='cyan', label='cluster_025')
        cc0.node('5')

    with c.subgraph(name='cluster_026') as cc1:
        cc1.attr(color='seagreen1', label='cluster_026')
        cc1.edges([('6', '7'), ('6', '8')])

        with cc1.subgraph(name='cluster_0267') as ccc0:
            ccc0.attr(color='red')
            ccc0.node('7')

        with cc1.subgraph(name='cluster_0268') as ccc1:
            ccc1.attr(color='red')
            ccc1.node('8')
g.view(cleanup=True)    
print(g)
