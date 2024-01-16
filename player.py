import math
import random

class Player:
      def __init__(self,sign):
          self.sign=sign     # sign will bw o or x

      def get_move(self,game):
           pass
      
     
class RandomComputerPlayer(Player):
      def __init__(self,sign):
          super().__init__(sign)

      def get_move(self,game):
          square=random.choice(game.available_moves())
          return square
      
class HumanPlayer(Player):
      def __init__(self,sign):
           super().__init__(sign)
      
      def get_move(self,game):
          valid_square=False
          val=None
          while not valid_square:
               square=input(self.sign+ '\'s.turn .Input move(0-8):')
               try:
                    val=int(square)
                    if val not in game.available_moves():
                       raise ValueError
                    valid_square=True
               except ValueError:
                    print("Invalid square. Try again. ")
          return val
