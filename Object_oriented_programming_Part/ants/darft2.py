import ants, importlib   
importlib.reload(ants)   
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9) 
            # 这里的ants是ants.py 所以说是module!
gamestate = ants.GameState(None, beehive, ants.ant_types(),ants.dry_layout, dimensions, food=20)

ants.ants_lose = lambda: None#写入输的方法，……不写也可以啊草，反正后面会重写
# QueenAnt Placement
queen = ants.QueenAnt.construct(gamestate)
impostor = ants.QueenAnt.construct(gamestate)
impostor is None # you cannot create a second QueenAnt!
True
front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
tunnel = [gamestate.places['tunnel_0_{0}'.format(i)] for i in range(9)]
# tunnel[1].add_insect(back_ant)
print("tunnel[1].add_insect(back_ant)", tunnel[1].add_insect(back_ant))
# tunnel[7].add_insect(front_ant)
print("tunnel[7].add_insect(front_ant)", tunnel[7].add_insect(front_ant))
tunnel[4].ant is None
print("tunnel[4]", tunnel[4])
True
back_ant.damage           # Ants should not have double damage
1
front_ant.damage
1
# tunnel[4].add_insect(queen)


print("type(queen)", type(queen))#<class 'NoneType'>
print("type(ants)", type(ants))#<class 'module'>
type(ants.QueenAnt)
print("type(ants.QueenAnt)", type(ants.QueenAnt))#<class 'type'>
type(ants.QueenAnt.construct)
print("type(ants.QueenAnt.construct)", type(ants.QueenAnt.construct))#<class 'method'>
print("gamestate", gamestate)# ['ThrowerAnt(1, tunnel_0_1)', 'ThrowerAnt(1, tunnel_0_7)'] (Food: 20, Time: 0)
# print("gamestate", gamestate.__dict__)