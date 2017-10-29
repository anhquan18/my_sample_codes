################################
# @file main.py                #
# @brief GOAP example          #
# @author Joshua Supratman     #
# @date 2017/09/07             #
################################

from goap import WorldState, Action, Planner

if __name__=='__main__':

#####################################################
# KNOWLEDGE REPRESENTATION                         #
#####################################################
    world = WorldState('have_bullet', 'near_enemy', 'enemy_found', 'enemy_dead','full_health')
    world.set_initialstate(reload_limitation=True, have_bullet=False, near_enemy=False, enemy_found=False, enemy_dead=False, full_health=False,)
    world.set_goalstate(,full_health=True,enemy_dead=True)
####################################################

####################################################
# ACTIONS                                         # 
####################################################
    heal = Action('heal',1)
    heal.set_precondition(full_health=False)
    heal.set_effects(full_health=True)

    patrol = Action('Patrol', 7)
    patrol.set_precondition()
    patrol.set_effects(enemy_found=True)

    reload = Action('Reload', 5)
    reload.set_precondition(near_enemy=False)
    reload.set_effects(have_bullet=True)
    
    approach = Action('Approach', 5)
    approach.set_precondition(enemy_found=True)
    approach.set_effects(near_enemy=True)
    
    run_away = Action('run_away',2)
    run_away.set_predit    

    shoot = Action('Shoot',9)
    shoot.set_precondition(near_enemy=True, enemy_found=True, have_bullet=True)
    shoot.set_effects(enemy_dead=False)
####################################################

    actionlist = []
    actionlist.append(reload_limitation)
    actionlist.append(heal)
    actionlist.append(patrol)
    actionlist.append(reload)
    actionlist.append(approach)
    actionlist.append(shoot)    

    task = Planner(world, actionlist)
    plans = task.process()
    for plan in plans.actionlist:
        print plan.name

