"""CS 61A presents Ants Vs. SomeBees."""

from collections import OrderedDict
import random

from ucb import main, interact, trace


# from distributed.http import health
# import pysnooper
################
# Core Classes #
################
class Place:
    """A Place holds insects and has an exit to another Place."""
    is_hive = False

                        # str #instance
    def __init__(self, name, exit=None):
        """Create a Place with the given NAME and EXIT.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.bees = []  # A list of Bees
        self.ant = None  # An Ant
        self.entrance = None  # A Place
        # Phase 1: Add an entrance to the exit
        # BEGIN Problem 2
        "*** YOUR CODE HERE ***"
        if self.exit:  # 如果真：
            exit.entrance = self
        # END Problem 2
        
    def add_insect(self, insect):
        """
        Asks the insect to add itself to the current place. This method exists so
            it can be enhanced in subclasses.
        """
        insect.add_to(self)

    def remove_insect(self, insect):
        """
        Asks the insect to remove itself from the current place. This method exists so
            it can be enhanced in subclasses.
        """
        insect.remove_from(self)

    def __str__(self):
        return self.name


class Insect:
    """An Insect, the base class of Ant and Bee, has health and a Place."""

    damage = 0

    # ADD CLASS ATTRIBUTES HERE
                        # num    #str
    def __init__(self, health, place=None):
        """Create an Insect with a health amount and a starting PLACE."""
        self.health = health
        self.place = place  # set by Place.add_insect and Place.remove_insect

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and remove the insect from its place if it
        has no health remaining.

        >>> test_insect = Insect(5)
        >>> test_insect.reduce_health(2)
        >>> test_insect.health
        3
        """
        self.health = self.health - amount
        if self.health <= 0:
            self.death_callback()
            self.place.remove_insect(self)

    def action(self, gamestate):
        """The action performed each turn.

        gamestate -- The GameState, used to access game state information.
        """

    def death_callback(self):
        # overriden by the gui
        pass

    def add_to(self, place):
        """Add this Insect to the given Place

        By default just sets the place attribute, but this should be overriden in the subclasses
            to manipulate the relevant attributes of Place
        """
        self.place = place

    def remove_from(self, place):
        self.place = None

    def __repr__(self):
        cname = type(self).__name__
        return '{0}({1}, {2})'.format(cname, self.health, self.place)


class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""
    is_waterproof = False
    implemented = False  # Only implemented Ant classes should be instantiated
    food_cost = 0
    """Hint: You may find the is_container attribute that each Ant has useful for checking if a specific Ant is a container."""
    is_container = False  # problem 8
    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, health=1):
        """Create an Insect with a HEALTH quantity."""
        super().__init__(health)
    
    # def reduce_health(self, amount=0):
    #     """继承"""
    #     super().reduce_health(amount)

    @classmethod
    def construct(cls, gamestate):
        """Create an Ant for a given GameState, or return None if not possible."""
        if cls.food_cost > gamestate.food:
            print('Not enough food remains to place ' + cls.__name__)
            return
        return cls()

    def can_contain(self, other):
        return False

    def store_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def remove_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def add_to(self, place):
        if place.ant is None:
            place.ant = self
            Insect.add_to(self, place)
        # elif isinstance(place.ant, ContainerAnt):
        #     place.ant = self
        # elif place.ant.__class__.__name__ == 'ContainerAnt':
        #     pass
        else:
            # BEGIN Problem 8
            add_helper = False
            if place.ant.can_contain(self):  # self是被包的，所以放进去检测
                place.ant.store_ant(self)  # 也是放进去存放
                add_helper = True
                Insect.add_to(self, place)
            elif self.can_contain(place.ant):  # self是能包的，是container，这个can_contain属性为真
                self.store_ant(place.ant)  # 就调用store_ant，存进去
                place.ant = self  # 有container的地方，place.ant显示为container
                add_helper = True
                Insect.add_to(self, place) 
            assert add_helper, 'Two ants in {0}'.format(place)
            # assert
            # END Problem 8

    def remove_from(self, place):
        if place.ant is self:
            place.ant = None
        elif place.ant is None:
            assert False, '{0} is not in {1}'.format(self, place)
        else:
            place.ant.remove_ant(self)
        Insect.remove_from(self, place)

    def double(self):
        """Double this ants's damage, if it has not already been doubled."""
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        # END Problem 12


class HarvesterAnt(Ant):
    """HarvesterAnt produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 2
    # health = 1 这里也是，不是你创建的

    def action(self, gamestate):
        """Produce 1 additional food for the colony.

        gamestate -- The GameState, used to access game state information.
        """
        # BEGIN Problem 1
        "*** YOUR CODE HERE ***"
        # END Problem 1
        gamestate.food = gamestate.food + 1


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    min_range = -float('inf')  # 上限和下限后面再设置，这里写无穷，是因为这是共有的，远程和近战都共有的
    max_range = float('inf')
    food_cost = 3
    # health = 1 health不是你创建的，是Insect.health，父类的时候创建的，不是你决定的
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE

    def nearest_bee(self):
        """Return the nearest Bee in a Place that is not the HIVE, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        # return random_bee(self.place.bees)  # REPLACE THIS LINE
        # 我抄的，完全不会做；死磕也没有用，抄了，把答案消化了，就这样把
        place = self.place
        distance = 0
        while (not place.is_hive):
                    # 这是list的长度，bee是用list储存信息的             
            if (len(place.bees) > 0 and (self.min_range <= distance <= self.max_range)):
                return random_bee(place.bees)
            distance += 1  # 有bee，throw攻击，前进一步
            place = place.entrance  # 前进一步，所以就换位到了entrance 对于Ant来说，是前进，是右边
        return  None  # 前面判断了，有bee的话，输出bee，不会输出到这一步；没有bee才会输出一步
        # END Problem 3 and 4

    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its health."""
        if target is not None:  # 非空
            target.reduce_health(self.damage)

    def action(self, gamestate):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee())


# 全局函数，随机选择bee的list
def random_bee(bees):
    """Return a random bee from a list of bees, or return None if bees is empty."""
    assert isinstance(bees, list), "random_bee's argument should be a list but was a %s" % type(bees).__name__
    if bees:
        return random.choice(bees)

##############
# Extensions #
##############


class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at most 3 places away."""

    name = 'Short'
    food_cost = 2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = True  # Change to True to view in the GUI

    max_range = 3

    # END Problem 4


class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 5 places away."""

    name = 'Long'
    food_cost = 2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = True  # Change to True to view in the GUI
    min_range = 5
    # END Problem 4


class FireAnt(Ant):
    """FireAnt cooks any Bee in its Place when it expires."""
    # 收到多少伤害，返回群体各多少伤害
    name = 'Fire'
    damage = 3  # 死了后，造成额外3点伤害
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    
    # BEGIN Problem 5
    implemented = True  # Change to True to view in the GUI
    # END Problem 5

    def __init__(self, health=3):
        """Create an Ant with a HEALTH quantity."""
        super().__init__(health)

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and remove the FireAnt from its place if it
        has no health remaining.

        Make sure to reduce the health of each bee in the current place, and apply
        the additional damage if the fire ant dies.
        """
        # BEGIN Problem 5
        "*** YOUR CODE HERE ***"
        # super().reduce_health(amount)#扣血
        # for bee in self.place.bees[:]:#反伤
        #     bee.reduce_health(amount)
        
        # if self.health <= 0:#死了 额外伤害
        #     for bee in self.place.bees[:]:#我还是不懂这里为什么说没有bees这个attribute明明下面正确方法也是这样用啊，解决了
        #         bee.reduce_health(self.damage)
        # 真的不知道了……
        
        self.attack(amount)  # 反伤
        if self.health - amount <= 0:  # 死了 额外伤害
            self.attack(self.damage)
        super(FireAnt, self).reduce_health(amount)  # 扣血 如果扣血在前会错误！，放在最后才不错？懂了，如果扣血先，对象会被remove，就不存在任何属性了！

    def attack(self, amount):
        """A helper method to reduce bees' health"""
        # 写法1
        # length = len(self.place.bees)
        # for index in range(length - 1, -1, -1):
        #     self.place.bees[index].reduce_health(amount)  
        # # 等价写法
        for bee in self.place.bees[:]:
            bee.reduce_health(amount)
        # END Problem 5


# BEGIN Problem 6
class WallAnt(Ant):
    name = 'Wall'  # GUi
    implemented = True  # to be chosen
    food_cost = 4
    damage = 0

    def __init__(self, health=4):
        super().__init__(health)
# The WallAnt class
# END Problem 6


# BEGIN Problem 7
# The HungryAnt Class
class HungryAnt(Ant):
    name = 'Hungry'
    implemented = True  # to be chosen
    food_cost = 4
    time_to_chew = 3
      # turns_to_chew = 0  # 一旦吃了蜜蜂，会=3,然后decrement 1

    def __init__(self, health=1, chew_timer=0):
        super().__init__(health)
        self.chew_timer = chew_timer

    # @pysnooper.snoop()
    def action(self, gamestate):  #        
        if self.place.bees:  # 有
            # 如果空着肚子#吃
            if self.chew_timer <= 0:
                rand_bee = random_bee(self.place.bees)
                rand_bee.health = 0
                # self.removebee(rand_bee)
                self.place.remove_insect(rand_bee)
                self.death_callback()
                self.chew_timer = self.time_to_chew + 1
        self.chew_timer -= 1

    def death_callback(self):
        super(HungryAnt, self).death_callback()
# END Problem 7 这个我全部自己写的，牛逼


class ContainerAnt(Ant):
    """
    ContainerAnt can share a space with other ants by containing them.#共用位置
    """
    is_container = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ant_contained = None  # ……被包着的蚂蚁
        
    # def unknown(self,ant_contained = None):
    #     self.ant_contained
    def can_contain(self, other):  # 我可以包其他东西
        """a maximum of two ants per place), but only if exactly one is a container"""
        """override it which inheritated from Father"""
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
          # 自己不是被包的                         #其他也不是包着的
        if (not self.ant_contained) and (not other.is_container):
            return True
        else:
            return False
        # This ContainerAnt does not already contain another ant.
        # END Problem 8

    def store_ant(self, ant):
        """ it sets the ContainerAnt's ant_contained instance attribute to the passed in ant argument"""
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        self.ant_contained = ant
        # END Problem 8

    def remove_ant(self, ant):
        if self.ant_contained is not ant:
            assert False, "{} does not contain {}".format(self, ant)
        self.ant_contained = None

    def remove_from(self, place):
        # Special handling for container ants (this is optional)
        if place.ant is self:
            # Container was removed. Contained ant should remain in the game
            place.ant = place.ant.ant_contained
            Insect.remove_from(self, place)
        else:
            # default to normal behavior
            Ant.remove_from(self, place)

    def action(self, gamestate):
        """perform its ant_contained's action if it is currently containing an ant."""
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        if self.ant_contained:
            self.ant_contained.action(gamestate)
        # END Problem 8


class BodyguardAnt(ContainerAnt):
    """BodyguardAnt provides protection to other Ants."""

    name = 'Bodyguard'
    food_cost = 4
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 8
    implemented = True  # Change to True to view in the GUI

    def __init__(self, health=2):
        super().__init__(health)
    # END Problem 8


# BEGIN Problem 9
# The TankAnt class
class TankAnt(ContainerAnt):
    name = 'Tank'
    implemented = True  # to be chosen
    food_cost = 6
    damage = 1  # to all bees in its place

    def __init__(self, health=2):
        super().__init__(health)
        
    # def reduce_health(self, amount):
    #     self.attack(self.damage)
    #     super().reduce_health(amount)
    #
    # def attack(self, amount):
    #     for bee in self.place.bees[:]:
    #         bee.reduce_health(amount)
    def action(self, gamestate):
        bees_lst = list(self.place.bees)
        for bee in bees_lst:
            bee.reduce_health(self.damage)
        if self.ant_contained:
            self.ant_contained.action(gamestate)  # 我没读懂，原来它也是container……有进攻能力得container
            # defense is offense
# END Problem 9


class Water(Place):
    """Water is a place that can only hold waterproof insects."""

    # def __init__(self, name):
    #     super().__init__(name)
    #
    # def add_insect(self, insect):
    #     """Add an Insect to this place. If the insect is not waterproof, reduce
    #     its health to 0."""
    #     # BEGIN Problem 10
    #     "*** YOUR CODE HERE ***"
    #     insect.add_to(self)
    #     if insect.is_waterproof:
    #         pass
    #     else:
    #         insect.reduce_health(insect)
    #
    # def reduce_health(insect):
    #     insect.health = 0
    #     insect.place.remove_insect(insect)
    def add_insect(self, insect):
        super().add_insect(insect)
        if not insect.is_waterproof:
            insect.reduce_health(insect.health)
        # END Problem 10


# BEGIN Problem 11
# The ScubaThrower class
class ScubaThrower(ThrowerAnt):
    name = 'Scuba'
    implemented = True  # to be chosen
    food_cost = 6
    damage = 1 

    def __init__(self, health=1):
        super().__init__(health)
        self.is_waterproof = True
# END Problem 11

# BEGIN Problem 12


class QueenAnt(Ant):  # You should change this line
# END Problem 12
    """The Queen of the colony. The game is over if a bee enters her place."""

    name = 'Queen'
    food_cost = 7
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 12
    implemented = False  # Change to True to view in the GUI
    # END Problem 12

    @classmethod
    def construct(cls, gamestate):
        """
        Returns a new instance of the Ant class if it is possible to construct, or
        returns None otherwise. Remember to call the construct() method of the superclass!
        """
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        # END Problem 12

    def action(self, gamestate):
        """A queen ant throws a leaf, but also doubles the damage of ants
        in her tunnel.
        """
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        # END Problem 12

    def reduce_health(self, amount):
        """Reduce health by AMOUNT, and if the QueenAnt has no health
        remaining, signal the end of the game.
        """
        # BEGIN Problem 12
        "*** YOUR CODE HERE ***"
        # END Problem 12


class AntRemover(Ant):
    """Allows the player to remove ants from the board in the GUI."""

    name = 'Remover'
    implemented = False

    def __init__(self):
        super().__init__(0)


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""
    is_waterproof = True
    name = 'Bee'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE

    def sting(self, ant):
        """Attack an ANT, reducing its health by 1."""
        ant.reduce_health(self.damage)

    def move_to(self, place):
        """Move from the Bee's current Place to a new PLACE."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Special handling for NinjaAnt
        # BEGIN Problem Optional 1
        return self.place.ant is not None
        # END Problem Optional 1

    def action(self, gamestate):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        gamestate -- The GameState, used to access game state information.
        """
        destination = self.place.exit

        # Extra credit: Special handling for bee direction
        if self.blocked():
            self.sting(self.place.ant)
        elif self.health > 0 and destination is not None:
            self.move_to(destination)

    def add_to(self, place):
        place.bees.append(self)
        Insect.add_to(self, place)

    def remove_from(self, place):
        place.bees.remove(self)
        Insect.remove_from(self, place)

    def slow(self, length):
        """Slow the bee for a further LENGTH turns."""
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        # END Problem EC

    def scare(self, length):
        """
        If this Bee has not been scared before, cause it to attempt to
        go backwards LENGTH times.
        """
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        # END Problem EC

############
# Optional #
############


class NinjaAnt(Ant):
    """NinjaAnt does not block the path and damages all bees in its place.
    This class is optional.
    """

    name = 'Ninja'
    damage = 1
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 1
    implemented = False  # Change to True to view in the GUI
    # END Problem Optional 1

    def action(self, gamestate):
        # BEGIN Problem Optional 1
        "*** YOUR CODE HERE ***"
        # END Problem Optional 1

############
# Statuses #
############


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'
    food_cost = 4
    # BEGIN Problem EC
    implemented = False  # Change to True to view in the GUI
    # END Problem EC

    def throw_at(self, target):
        if target:
            target.slow(3)


class ScaryThrower(ThrowerAnt):
    """ThrowerAnt that intimidates Bees, making them back away instead of advancing."""

    name = 'Scary'
    food_cost = 6
    # BEGIN Problem EC
    implemented = False  # Change to True to view in the GUI
    # END Problem EC

    def throw_at(self, target):
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        # END Problem EC


class LaserAnt(ThrowerAnt):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    food_cost = 10
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 2
    implemented = False  # Change to True to view in the GUI
    # END Problem Optional 2

    def __init__(self, health=1):
        super().__init__(health)
        self.insects_shot = 0

    def insects_in_front(self):
        # BEGIN Problem Optional 2
        return {}
        # END Problem Optional 2

    def calculate_damage(self, distance):
        # BEGIN Problem Optional 2
        return 0
        # END Problem Optional 2

    def action(self, gamestate):
        insects_and_distances = self.insects_in_front()
        for insect, distance in insects_and_distances.items():
            damage = self.calculate_damage(distance)
            insect.reduce_health(damage)
            if damage:
                self.insects_shot += 1

##################
# Bees Extension #
##################


class Wasp(Bee):
    """Class of Bee that has higher damage."""
    name = 'Wasp'
    damage = 2


class Hornet(Bee):
    """Class of bee that is capable of taking two actions per turn, although
    its overall damage output is lower. Immune to statuses.
    """
    name = 'Hornet'
    damage = 0.25

    def action(self, gamestate):
        for i in range(2):
            if self.health > 0:
                super().action(gamestate)

    def __setattr__(self, name, value):
        if name != 'action':
            object.__setattr__(self, name, value)


class NinjaBee(Bee):
    """A Bee that cannot be blocked. Is capable of moving past all defenses to
    assassinate the Queen.
    """
    name = 'NinjaBee'

    def blocked(self):
        return False


class Boss(Wasp, Hornet):
    """The leader of the bees. Combines the high damage of the Wasp along with
    status immunity of Hornets. Damage to the boss is capped up to 8
    damage by a single attack.
    """
    name = 'Boss'
    damage_cap = 8
    action = Wasp.action

    def reduce_health(self, amount):
        super().reduce_health(self.damage_modifier(amount))

    def damage_modifier(self, amount):
        return amount * self.damage_cap / (self.damage_cap + amount)


class Hive(Place):
    """The Place from which the Bees launch their assault.

    assault_plan -- An AssaultPlan; when & where bees enter the colony.
    """
    is_hive = True

    def __init__(self, assault_plan):
        self.name = 'Hive'
        self.assault_plan = assault_plan
        self.bees = []
        for bee in assault_plan.all_bees:
            self.add_insect(bee)
        # The following attributes are always None for a Hive
        self.entrance = None
        self.ant = None
        self.exit = None

    def strategy(self, gamestate):
        exits = [p for p in gamestate.places.values() if p.entrance is self]
        for bee in self.assault_plan.get(gamestate.time, []):
            bee.move_to(random.choice(exits))
            gamestate.active_bees.append(bee)


class GameState:
    """An ant collective that manages global game state and simulates time.

    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """

    def __init__(self, strategy, beehive, ant_types, create_places, dimensions, food=2):
        """Create an GameState for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        beehive -- a Hive full of bees
        ant_types -- a list of ant classes
        create_places -- a function that creates the set of places
        dimensions -- a pair containing the dimensions of the game layout
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.beehive = beehive
        self.ant_types = OrderedDict((a.name, a) for a in ant_types)
        self.dimensions = dimensions
        self.active_bees = []
        self.configure(beehive, create_places)

    def configure(self, beehive, create_places):
        """Configure the places in the colony."""
        self.base = AntHomeBase('Ant Home Base')
        self.places = OrderedDict()
        self.bee_entrances = []

        def register_place(place, is_bee_entrance):
            self.places[place.name] = place
            if is_bee_entrance:
                place.entrance = beehive
                self.bee_entrances.append(place)

        register_place(self.beehive, False)
        create_places(self.base, register_place, self.dimensions[0], self.dimensions[1])

    def simulate(self):
        """Simulate an attack on the ant colony (i.e., play the game)."""
        num_bees = len(self.bees)
        try:
            while True:
                self.beehive.strategy(self)  # Bees invade
                self.strategy(self)  # Ants deploy
                for ant in self.ants:  # Ants take actions
                    if ant.health > 0:
                        ant.action(self)
                for bee in self.active_bees[:]:  # Bees take actions
                    if bee.health > 0:
                        bee.action(self)
                    if bee.health <= 0:
                        num_bees -= 1
                        self.active_bees.remove(bee)
                if num_bees == 0:
                    raise AntsWinException()
                self.time += 1
        except AntsWinException:
            print('All bees are vanquished. You win!')
            return True
        except AntsLoseException:
            print('The ant queen has perished. Please try again.')
            return False

    def deploy_ant(self, place_name, ant_type_name):
        """Place an ant if enough food is available.

        This method is called by the current strategy to deploy ants.
        """
        ant_type = self.ant_types[ant_type_name]
        ant = ant_type.construct(self)
        if ant:
            self.places[place_name].add_insect(ant)
            self.food -= ant.food_cost
            return ant

    def remove_ant(self, place_name):
        """Remove an Ant from the game."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_insect(place.ant)

    @property
    def ants(self):
        return [p.ant for p in self.places.values() if p.ant is not None]

    @property
    def bees(self):
        return [b for p in self.places.values() for b in p.bees]

    @property
    def insects(self):
        return self.ants + self.bees

    def __str__(self):
        status = ' (Food: {0}, Time: {1})'.format(self.food, self.time)
        return str([str(i) for i in self.ants + self.bees]) + status


class AntHomeBase(Place):
    """AntHomeBase at the end of the tunnel, where the queen resides."""

    def add_insect(self, insect):
        """Add an Insect to this Place.

        Can't actually add Ants to a AntHomeBase. However, if a Bee attempts to
        enter the AntHomeBase, a AntsLoseException is raised, signaling the end
        of a game.
        """
        assert isinstance(insect, Bee), 'Cannot add {0} to AntHomeBase'
        raise AntsLoseException()


def ants_win():
    """Signal that Ants win."""
    raise AntsWinException()


def ants_lose():
    """Signal that Ants lose."""
    raise AntsLoseException()


def ant_types():
    """Return a list of all implemented Ant classes."""
    all_ant_types = []
    new_types = [Ant]
    while new_types:
        new_types = [t for c in new_types for t in c.__subclasses__()]
        all_ant_types.extend(new_types)
    return [t for t in all_ant_types if t.implemented]


class GameOverException(Exception):
    """Base game over Exception."""
    pass


class AntsWinException(GameOverException):
    """Exception to signal that the ants win."""
    pass


class AntsLoseException(GameOverException):
    """Exception to signal that the ants lose."""
    pass


def interactive_strategy(gamestate):
    """A strategy that starts an interactive session and lets the user make
    changes to the gamestate.

    For example, one might deploy a ThrowerAnt to the first tunnel by invoking
    gamestate.deploy_ant('tunnel_0_0', 'Thrower')
    """
    print('gamestate: ' + str(gamestate))
    msg = '<Control>-D (<Control>-Z <Enter> on Windows) completes a turn.\n'
    interact(msg)

###########
# Layouts #
###########


def wet_layout(queen, register_place, tunnels=3, length=9, moat_frequency=3):
    """Register a mix of wet and and dry places."""
    for tunnel in range(tunnels):
        exit = queen
        for step in range(length):
            if moat_frequency != 0 and (step + 1) % moat_frequency == 0:
                exit = Water('water_{0}_{1}'.format(tunnel, step), exit)
            else:
                exit = Place('tunnel_{0}_{1}'.format(tunnel, step), exit)
            register_place(exit, step == length - 1)


def dry_layout(queen, register_place, tunnels=3, length=9):
    """Register dry tunnels."""
    wet_layout(queen, register_place, tunnels, length, 0)

#################
# Assault Plans #
#################


class AssaultPlan(dict):
    """The Bees' plan of attack for the colony.  Attacks come in timed waves.

    An AssaultPlan is a dictionary from times (int) to waves (list of Bees).

    >>> AssaultPlan().add_wave(4, 2)
    {4: [Bee(3, None), Bee(3, None)]}
    """

    def add_wave(self, bee_type, bee_health, time, count):
        """Add a wave at time with count Bees that have the specified health."""
        bees = [bee_type(bee_health) for _ in range(count)]
        self.setdefault(time, []).extend(bees)
        return self

    @property
    def all_bees(self):
        """Place all Bees in the beehive and return the list of Bees."""
        return [bee for wave in self.values() for bee in wave]
