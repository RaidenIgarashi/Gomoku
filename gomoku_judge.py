from gomoku_tabuleiro import tabuleiro
from gomoku_player_class import player

#a classe judge é aquela que vai guardar as posições que estão ocupados e definir o ganhador
class judge():
    def __init__(self):
    #loc_places é a variavel na qual irá armazenar as posições que estão ocupadas
        self.lock_places = []
        
#win recebe uma posição e verifica se dentro da lista de posições de algum dos jogador, existe uma combinação de
#vitória
    def win(self, position_lst):
        
    
        ind = 0
        #sequence é uma lista onde vai guardar as posições com potencial de serem uma sequencia
        sequence = []
        ind2 = 0
        #sequence_correct verifica se a sequencia está correta
        sequence_correct = 0
        while ind < len(position_lst):
                #check_x e check_y são variaveis que juntas formam uma posição que vai ser usada para encontrar
                #posições com potencial de serem sequencia
                check_y = position_lst[ind][0]
                check_x = position_lst[ind][1]
                #soma é uma variavel usada para diminuir ou aumentar a(s) cordenadas da posição para verificar
                #se existe posições próximas
                soma = -5
                #horizontal
                while soma <= 5:
                    #aqui buscamos se há peças no perimetro possível de se formar uma sequencia e guardamos em 
                    #sequence
                    if [check_y, check_x + soma] in position_lst:
                        sequence.append([check_y, check_x + soma])
                    soma += 1
                if len(sequence) >= 5:
                    #aqui a gente verifica se as posições dentro da sequence é realmente uma sequencia
                    while ind2 < len(sequence):
                        if [sequence[ind2][0], sequence[ind2][1]+1] in sequence and sequence_correct <= 5:
                            ind2+=1
                            sequence_correct+=1
                        elif sequence_correct >= 4:
                            return True
                        else:
                            ind2 = len(sequence)
                            sequence_correct = 0
                
                else:
                    sequence = []
                soma = -5
                ind2 = 0
                #vertical
                while soma <= 5:
                    if [check_y + soma, check_x] in position_lst:
                        sequence.append([check_y + soma, check_x])
                    soma += 1
                soma = -5
                if len(sequence) == 5:
                    while ind2 < len(sequence):
                        if [sequence[ind2][0]+1, sequence[ind2][1]] in sequence and sequence_correct <= 5:
                            sequence_correct+=1
                            ind2+=1
                        elif sequence_correct == 4:
                            return True
                        else:
                            ind2 = len(sequence)
                            sequence_correct = 0
                else:
                    sequence = []
                sequence_correct = 0
                #diagonal
                while soma <= 5:
                    if [check_y + soma, check_x + soma] in position_lst and sequence_correct <= 5:
                        sequence.append([check_y + soma, check_x + soma])
                    soma += 1
                soma = -5
                if len(sequence) == 5:
                    while ind2 < len(sequence):
                        if [sequence[ind2][0]+1, sequence[ind2][1]+1] in sequence:
                            sequence_correct+=1
                            ind2+=1
                        elif sequence_correct == 4:
                            return True
                        else:
                            ind2 = len(sequence)
                            sequence_correct = 0 
                else:
                    sequence = []
                ind2 = 0 
                sequence_correct = 0
                soma = -5
                #diagonal reversa
                while soma <= 5:
                    if [check_y - soma, check_x + soma] in position_lst and sequence_correct <= 5:
                        sequence.append([check_y - soma, check_x + soma])
                    soma += 1
                if len(sequence) == 5:
                    while ind2 < len(sequence):
                        if [sequence[ind2][0]-1, sequence[ind2][1]+1] in sequence and sequence_correct <= 5:
                            sequence_correct+=1
                            ind2+=1
                        elif sequence_correct == 4:
                            return True
                        else:
                            ind2 = len(sequence)
                            sequence_correct = 0
                else:
                    sequence = []
                ind+=1
                ind2=0
                sequence_correct = 0
                sequence = []
            

        
       
#aqui ele recebe uma posição e depois a coloca no lock_place e por fim desenha o tabuleiro se draw for igual a 0
#se a posição já estiver no lock_places, ela faz um print e retorna False
    def positionJudge(self, position, player=0, draw=0):
        if not position in self.lock_places:
            t.changeBoard(position[0], position[1], player)
            if draw == 0:
                t.drawBoard()
            self.lock_places.append(position)
        else: 
            print('essa posição não está disponível')
            return False
            

t = tabuleiro()
p = player()