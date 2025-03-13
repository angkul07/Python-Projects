import math
import random

class Player:
    def __init__(self,letter):
        # Select the letter x or o
        self.letter = letter

    def getMove(self, game):
        pass

class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        square = random.choice(game.availabe_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-9): ')
            try:
                val = int(square)
                if val not in game.availabe_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Please try again.")

        return val

