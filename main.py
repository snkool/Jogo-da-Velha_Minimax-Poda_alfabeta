import os, time
from j_velha import iniciarLayout, printLayout, getJogada, marcaPosicao, verificaPosicao, verificaVitoria, getOpJogo, getOpReset, logo, limpa

from minimax_poda_alfabeta import marcaPosicaoIA

limpa() # Limpa a tela do terminal
logo() # Carrega a logo "Jogo da Velha" no terminal

jogador = 0 # Variavel para identificar o jogador X ou O
layout = iniciarLayout() # A variavel layout é responsável por receber a função que gera a matriz do jogo da velha
jogo = verificaVitoria(layout) # A variavel jogo recebe a função responsável por verificar a situação do jogo, se houve vitória para um dos jogadores ou empate

# Pergunta se o jogador desejar jogar com X ou O
op_jogo = getOpJogo("\033[33mVoce deseja jogar com X ou O?\n\033[m")

# While é executado até o jogador escolher a opcao de encerrar o jogo (reset = 1)
reset = 0
while(reset is 0):
    
    printLayout(layout)

    # Condição para estabelecer a ordem em que cada jogadar vai marcar uma posição no jogo da velha
    if(jogador == 0):
        if(op_jogo.lower() == "x"):
            i = getJogada("\n\033[36mDigite a linha:\n\033[m")
            j = getJogada("\033[34mDigite a coluna:\n\033[m")
        else: 
            i, j = marcaPosicaoIA(layout, jogador) 
    else:
        if(op_jogo.lower() == "o"):
            i = getJogada("\n\033[36mDigite a linha:\n\033[m")
            j = getJogada("\033[34mDigite a coluna:\n\033[m") 
        else:
            i, j = marcaPosicaoIA(layout, jogador)  

    # Verifica se a posicao escolhida pelo jogador esta vazia efetua a jogada
    if(verificaPosicao(layout, i, j)):
        marcaPosicao(layout, i, j, jogador)
        jogador = (jogador + 1) % 2
    else: 
        print("\n\033[31mEssa posicao ja foi escolhida! Por favor digite novamente.\033[m")
        time.sleep(1)

    # Verifica se um dos jogadores ganhou 
    jogo = verificaVitoria(layout)  
    limpa()
    logo()

    if(jogo):
        # Printa na tela o ganhador / Empate
        printLayout(layout)
        if(jogo == " \033[33mX\033[m " or jogo == " \033[35mO\033[m "):
            print("\n\033[32mVitória do\033[m", jogo) 
        else:
            print("\n\033[32mHouve um empate!\033[m") 

        # Pergunta se o jogador deseja continuar jogando depois do fim da partida
        op_reset = getOpReset("\033[33mVoce deseja continuar jogando? S - N\n\033[m")
        if(op_reset == "n"):
            reset = 1
            limpa()
            print("\n\033[33mEncerrando...\033[m")
            time.sleep(2)
            limpa()
        else:
            layout = iniciarLayout()
            jogador = 0
            op_jogo = getOpJogo("\033[33mVoce deseja jogar com X ou O?\n\033[m")
            limpa()
            logo()
        

