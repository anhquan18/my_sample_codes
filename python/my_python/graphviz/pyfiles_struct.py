from graphviz import Digraph, Graph

g = Digraph(name='pyfiles_contruction', format='png')

g.attr(bgcolor='dimgray')

with g.subgraph(name='cluster_robot_library') as r_lib:
    r_lib.attr('graph', label='pyfiles (strategy_library)')
    r_lib.attr('graph', fontsize='40')
    r_lib.attr('graph', color='dimgray')
    #r_lib.attr('graph', rankir='TD')
    r_lib.attr('graph', compound='true')

    r_lib.node(name='runstrategy.py\n(activate soccer robot)', shape='rect', style='filled', fillcolor='springgreen3', fontsize='20')
    r_lib.node('rcl.py', shape='tripleoctagon', fontsize='25')
    r_lib.node('motions\n(provide motions from MotionGenerator)', shape='folder', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')

    # create kid_directory
    with r_lib.subgraph(name='cluster_kid_directory') as kid:
        kid.attr(color='tomato', label='kid_directory', fontsize='30', rank='same', style='bold')
        
        # create file nodes 
        kid.node('tactics.py\n(provide behavior lists for roles using GOAP)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        kid.node('role.py\n(provide role classes and update functions)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        kid.node('common_network.py\n(provide sub HTN behaviors)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        kid.node('root_network.py\n(provide behavior lists for roles using HTN)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        kid.node('goal.py\n(provide goal_state for role update)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        kid.node('motion.py\n(provide kick,walk,... call functions)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        kid.node('strategy.py\n(update soccer roles, behaviors list)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        
        # create action_directory
        with kid.subgraph(name='cluster_action_directory') as act:
            act.attr(color='gold', label='action_directory', fontsize='30', style='bold')
        
            # create file nodes 
            act.node('neutralaction.py\n(provide SideEntry behaviors)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
            act.node('approach.py\n(provide approach algorithm functions)', shape='rect', fontsize='20', style='filled', fillcolor='sandybrown')
            act.node('approachfunc.py1\n(provide approach algorithm functions)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
            act.node('keeperaction.py\n(provide Keeper behaviors)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
            act.node('defenderaction.py\n(provide HTN behaviors for Defender)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        
        # connect files in kid directory
        kid.edge('approach.py\n(provide approach algorithm functions)', 'root_network.py\n(provide behavior lists for roles using HTN)', style='bold', color='lightpink3')
        kid.edge('approach.py\n(provide approach algorithm functions)', 'common_network.py\n(provide sub HTN behaviors)', style='bold', color='lightpink3')
        kid.edge('approachfunc.py1\n(provide approach algorithm functions)', 'approach.py\n(provide approach algorithm functions)', style='bold')
        kid.edge('common_network.py\n(provide sub HTN behaviors)', 'root_network.py\n(provide behavior lists for roles using HTN)', style='bold', fontsize='18')
        kid.edge('root_network.py\n(provide behavior lists for roles using HTN)', 'role.py\n(provide role classes and update functions)', style='bold')
        kid.edge('tactics.py\n(provide behavior lists for roles using GOAP)', 'role.py\n(provide role classes and update functions)', style='bold')
        kid.edge('motion.py\n(provide kick,walk,... call functions)', 'role.py\n(provide role classes and update functions)', style='bold')
        kid.edge('goal.py\n(provide goal_state for role update)', 'role.py\n(provide role classes and update functions)', style='bold')
        kid.edge('role.py\n(provide role classes and update functions)', 'strategy.py\n(update soccer roles, behaviors list)', style='bold')
        kid.edge('keeperaction.py\n(provide Keeper behaviors)', 'role.py\n(provide role classes and update functions)', style='bold')
        kid.edge('neutralaction.py\n(provide SideEntry behaviors)', 'role.py\n(provide role classes and update functions)', style='bold')
        kid.edge('neutralaction.py\n(provide SideEntry behaviors)', 'tactics.py\n(provide behavior lists for roles using GOAP)', style='bold')
        kid.edge('defenderaction.py\n(provide HTN behaviors for Defender)', 'role.py\n(provide role classes and update functions)', style='bold')
        
    # create actionbase_directory
    with r_lib.subgraph(name='cluster_actionbase_directory') as act_base:
        act_base.attr(color='aquamarine', label='actionbase_directory', fontsize='30', style='bold')

        #create file nodes
        act_base.node(name='headmotionfunc.py\n(provide behavior using camera)', shape='rect', fontsize='20', style='filled', fillcolor='violet')
        act_base.node(name='search.py\n(provide search ball behavior)', shape='rect', fontsize='20', style='filled', fillcolor='lightseagreen')
        act_base.node(name='bodymotion.py\n(provide idle,kick behaviors)', shape='rect', fontsize='20', style='filled', fillcolor='palevioletred1')
        act_base.node(name='approachfunc.py2\n(provide approach calculation)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        act_base.node(name='bodymotionabs.py\n(provide kick behavior)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')
        act_base.node(name='bodymotionfunc.py\n(provide kick parameters)', shape='rect', fontsize='20', fontcolor='black', style='filled', fillcolor='darksalmon')

        act_base.edge('approachfunc.py2\n(provide approach calculation)', 'search.py\n(provide search ball behavior)', style='bold')
        act_base.edge('bodymotionabs.py\n(provide kick behavior)', 'bodymotion.py\n(provide idle,kick behaviors)', style='bold')
        act_base.edge('bodymotionfunc.py\n(provide kick parameters)', 'bodymotion.py\n(provide idle,kick behaviors)', style='bold')
        act_base.edge('bodymotion.py\n(provide idle,kick behaviors)', 'common_network.py\n(provide sub HTN behaviors)', style='bold', color='orangered')
        act_base.edge('bodymotion.py\n(provide idle,kick behaviors)', 'root_network.py\n(provide behavior lists for roles using HTN)', style='bold', color='orangered')
        act_base.edge('bodymotion.py\n(provide idle,kick behaviors)', 'tactics.py\n(provide behavior lists for roles using GOAP)', style='bold', color='orangered')
        act_base.edge('headmotionfunc.py\n(provide behavior using camera)', 'bodymotion.py\n(provide idle,kick behaviors)', style='bold', color='violetred4')
        act_base.edge('headmotionfunc.py\n(provide behavior using camera)', 'bodymotionabs.py\n(provide kick behavior)', style='bold', color='violetred4')
        act_base.edge('headmotionfunc.py\n(provide behavior using camera)', 'search.py\n(provide search ball behavior)', style='bold', color='violetred4')
        act_base.edge('headmotionfunc.py\n(provide behavior using camera)', 'approach.py\n(provide approach algorithm functions)', style='bold', color='violetred4')
        act_base.edge('headmotionfunc.py\n(provide behavior using camera)', 'keeperaction.py\n(provide Keeper behaviors)', style='bold', color='violetred4')
        act_base.edge('headmotionfunc.py\n(provide behavior using camera)', 'defenderaction.py\n(provide HTN behaviors for Defender)', style='bold', color='violetred4')
        act_base.edge('headmotionfunc.py\n(provide behavior using camera)', 'neutralaction.py\n(provide SideEntry behaviors)', style='bold', color='violetred4')
        act_base.edge('search.py\n(provide search ball behavior)', 'common_network.py\n(provide sub HTN behaviors)', style='bold', color='yellowgreen')
        act_base.edge('search.py\n(provide search ball behavior)', 'root_network.py\n(provide behavior lists for roles using HTN)', style='bold', color='yellowgreen')
        act_base.edge('search.py\n(provide search ball behavior)', 'tactics.py\n(provide behavior lists for roles using GOAP)', style='bold', color='yellowgreen')

    # connect rcl.py to directories
    r_lib.edge('motions\n(provide motions from MotionGenerator)', 'rcl.py', style='bold')
    r_lib.edge('runstrategy.py\n(activate soccer robot)', 'rcl.py', style='bold')
    r_lib.edge('strategy.py\n(update soccer roles, behaviors list)', 'rcl.py', style='bold')

g.view(cleanup=True)
