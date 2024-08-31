from gomoku_player_class import Player
from random import randint


class Bot(Player):
    def __init__(self):
        self.cheat_positions = []
        super().__init__()


    
    
    
  #aqui ele sorteia uma posição e retorna ela  
    def botPlay(self):
        position = []
        position_x = randint(1, 19)
        position_y = randint(1, 19)
        position.append(position_y)
        position.append(position_x)
        return position

       