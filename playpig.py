# TO RUN PROGRAM: Type in terminal python playpig.py

import random

class Pig(object):

    def __init__(self, player):
        self.player= player
        self.score = 0
        self.roll_value = 0

    def start_game(self):
        roll_die = self.roll_die()
        if roll_die != 1:
            current_score = ('{} your rolled a {}'.format(self.player, self.roll_value))
            print(current_score)
            return self.player_decision(roll_die)
        return roll_die

    def player_decision(self, roll_die):
        if self.score >= 100:
            return True
        decision = raw_input('{} your score is {}, would you like to roll again?(type r and return) or to hold(press return key)? '.format(self.player, self.score))
        return decision

    def roll_die(self):
        for x in range(1):
            self.roll_value = random.randint(1,6)
        if self.roll_value > 1:
            self.score = self.roll_value + self.score
            return self.score
        return self.roll_value

def main():
    game_over = False
    player_one = Pig(raw_input("Player One, what is your name? "))
    player_two = Pig(raw_input("Player Two, what is your name? "))

    while not game_over:
        player_one_turn = player_one.start_game()
        if player_one_turn is not True:
            while player_one_turn == 'r':
                player_one_turn = player_one.start_game()
        if player_one_turn is True:
            game_over = player_one_turn
            print('The winner is {}, with a score of {}, {} your score was {}.'.format(player_one.player, player_one.score, player_two.player, player_two.score))
            return game_over
        if player_one_turn == 1:
            print('Sorry {} you rolled a 1 and lost a turn, your current score is {}.'.format(player_one.player, player_one.score))
        else:
            print('Sorry {} you gave up a turn, your current score is {}.'.format(player_one.player, player_one.score))

        player_two_turn = player_two.start_game()
        if player_two_turn is not True:
            while player_two_turn == 'r':
                player_two_turn = player_two.start_game()
        if player_two_turn is True:
            game_over = player_two_turn
            print('The winner is {}, with a score of {}, {} your score was {}.'.format(player_two.player, player_two.score, player_one.player, player_one.score))
            return game_over
        if player_two_turn == 1:
            print('Sorry {} you rolled a 1 and lost turn, your current score is {}.'.format(player_two.player, player_two.score))
        else:
            print('Sorry {} you gave up a turn, your current score is {}.'.format(player_two.player, player_two.score))

if __name__ == '__main__':
    main()
