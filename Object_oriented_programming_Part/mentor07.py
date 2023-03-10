class Baller:
    all_players = []
    def __init__(self, name, has_ball = False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)
    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False
class BallHog(Baller):
    def pass_ball(self, other_player):
        return False
    
alex = Baller('Alex', True)
mitas = BallHog('Mitas')

class TeamBaller(Baller):
    """
    >>> mitas = BallHog('Mitas')
    >>> cheerballer = TeamBaller('Chris', has_ball=True)
    >>> cheerballer.pass_ball(mitas)
    Yay!
    True
    >>> cheerballer.pass_ball(mitas)
    I don't have the ball
    False
    """
    def pass_ball(self, other_player):
        # did_pass = Baller.pass_ball(self,other_player) 和下面语句等价
        did_pass = super().pass_ball(other_player)
        if did_pass:
            print('Yay!')
        else:
            print('I don\'t have the ball')
        return did_pass
mitas = BallHog('Mitas')
cheerballer = TeamBaller('Chris', has_ball=True)
print(cheerballer.pass_ball(mitas))
print(cheerballer.pass_ball(mitas))
"""mentor07"""
