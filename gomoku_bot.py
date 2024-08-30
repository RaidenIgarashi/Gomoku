from gomoku_player_class import player
from random import randint
from random import choice

class bot(player):
    def __init__(self):
        self.cheat_positions = []
        super().__init__()


    
    
    
  #aqui ele sorteia uma posição e retorna ela  
    def bot_play(self):
        position = []
        position_x = randint(1, 19)
        position_y = randint(1, 19)
        position.append(position_y)
        position.append(position_x)
        return position

       