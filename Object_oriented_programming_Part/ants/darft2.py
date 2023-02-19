from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
#
# Testing HungryAnt chew duration looked up on instance
very_hungry = HungryAnt()  # Add very hungry caterpi- um, ant
HungryAnt.time_to_chew = 0
place = gamestate.places["tunnel_0_0"]
place.add_insect(very_hungry)
for _ in range(100):
    place.add_insect(Bee(3))
for _ in range(100):
    very_hungry.action(gamestate)   # Eat all the bees!
r = len(place.bees)
print(r)# 100
r = place.bees
print(r)