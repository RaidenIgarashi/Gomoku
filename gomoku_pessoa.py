from gomoku_player_class import Player

class Pessoa(Player):
    def __init__(self):
        super().__init__()
          
 #aqui ele pede uma posição que é composta uma letra e um número, e depois retorna ela como apenas números       
    def play(self):
        player_location = input('escreva uma posição ')
        translate_player_location = self.translateLocation(player_location)
        self.position_lst.append(translate_player_location)
        return [translate_player_location[0], translate_player_location[1]]    