from gomoku_tabuleiro import Tabuleiro 
from gomoku_pessoa import Pessoa
from gomoku_bot import Bot
from gomoku_judge import Judge

j = Judge()
t = Tabuleiro()
p = Pessoa()

player1 = Pessoa()
player2 = Pessoa()
player_bot = Bot()

play1 = True
play2 = True
#game é um input feito para o jogador selecionar se vai competir contra um bot ou um outro player
game = int(input("Digite 1 para lutar contra um bot ou 2 contra um player "))
if game == 1:
    #aqui ele vai ficar fazendo o jogo funcionar até alguem ganhar
    while not (j.win(player1.position_lst) or j.win(player_bot.position_lst)):
        if play2:
            if j.positionJudge(player1.play()) == False:
                play1 = False
            else:
                play1 = True
                play2 = True
        if not (j.win(player1.position_lst) or j.win(player_bot.position_lst)) and play1:     
            if j.positionJudge(player_bot.bot_play(), 1, 1):
                play1 = False
            else:
                play1 = True
                play2 = True
            if j.win(player_bot.position_lst):
                print('Bot ganhou')
        elif j.win(player1.position_lst):
            print('player1 ganhou')
elif game == 2:
    while not (j.win(player1.position_lst) or j.win(player2.position_lst)):
        if play2:
            if j.positionJudge(player1.play(), 0) == False:
                play1 = False
            else:
                play2 = True  
                play1 = True         
        if not (j.win(player1.position_lst) or j.win(player2.position_lst)) and play1:
            if j.positionJudge(player2.play(), 1) == False:
                play2 = False
            else:
                play1 = True
                play2 = True
            
            if j.win(player2.position_lst):
                print('Player2 ganhou')
        elif j.win(player1.position_lst):
            print('Player1 ganhou')