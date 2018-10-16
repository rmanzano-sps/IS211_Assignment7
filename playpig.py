import random

class Pig(object):

    def __init__(self, name):
        self.name = name
        self.score = 0


    def player_setup(self):
        player_one = self.name
        self.roll_die()

    def roll_die(self):
        roll = 0
        while roll != 1:
            for x in range(1):
                roll = random.randint(1,7)
                if roll != 1:
                    self.score = roll + self.score
        print(self.score, 'score')
        print(roll)
        if roll == 1:
            print('blue cheese')

        if self.score == 100:
            print(self.name, 'winner')


player_one = Pig('Frank')
player_two = Pig('Sue')
player_one.player_setup()
player_two.player_setup()
