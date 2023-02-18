from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
#
# Testing ShortThrower miss
ant = ShortThrower()
out_of_range = Bee(2)
gamestate.places["tunnel_0_0"].add_insect(ant)
gamestate.places["tunnel_0_4"].add_insect(out_of_range)
ant.action(gamestate)
r = out_of_range.health
print(r)# 1 expected 2
