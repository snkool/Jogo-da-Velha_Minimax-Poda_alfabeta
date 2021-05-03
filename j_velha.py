import os, time

vazio = "   "
jogador_token = [" \033[33mX\033[m ", " \033[35mO\033[m "]  

def logo():
    f = open("logo.txt", "r")
    print("\033[33m",f.read(),"\033[m")

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função para iniciar o layout do jogo da velha
def iniciarLayout():
    layout = [
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
    ]
    return layout

#Função para printar o layout do jogo da velha
def printLayout(layout): 
    for i in range(3):
        print("\033[33m|\033[m".join(layout[i]))

# Função para receber o input do jogador de qual posição ele deseja marcar
def getJogada(jogada):
    n = int(input(jogada))
    if(n >= 1 and n <= 3):
        return n - 1
    else:
        print("\033[31mNumero invalido, digite um numero entre 1 e 3\033[m")
        return getJogada(jogada)

# Funçao que recebe a escolha do jogador de jogar com X ou O
def getOpJogo(msg):
    op = input(msg)
    if((op.lower() == "x" or op.lower() == "o")):
        return op
    else: 
        print("\033[31mOpcao invalida, escolha X ou O\033[m")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') 
        logo()
        return getOpJogo(msg)

# Funcao responsavel por manter o while do main.py em loop, caso o jogador desejar parar de jogar a variável reset altera para 1 e o while é interrompido
def getOpReset(msg):
    op = input(msg)
    if((op.lower() == "s" or op.lower() == "n")):
        return op
    else: 
        print("\033[31mOpcao invalida, escolha S ou N\033[m")
        return getOpJogo(msg)
    

# Função que verifica se o local onde o jogador escolheu para marcar está vazio
def verificaPosicao(layout, i, j):
    if(layout[i][j] == vazio):
        return True
    else:
        return False

# Função que marca X ou O na matriz
def marcaPosicao(layout, i, j, jogador):
    layout[i][j] = jogador_token[jogador]

# Função responsavel por verificar se algum dos jogadores ganhou ou se houve empate
def verificaVitoria(layout):
    # Verifica colunas
    for i in range(3):
        if(layout[0][i] == layout[1][i] and layout[1][i] == layout[2][i] and layout[0][i] != vazio):
            return layout[0][i]

    # Verifica linhas
    for i in range(3):
        if(layout[i][0] == layout[i][1] and layout[i][1] == layout[i][2] and layout[i][0] != vazio):
            return layout[i][0]
    
    # Verifica a diagonal principal
    if(layout[0][0] != vazio and layout[0][0] == layout[1][1] and layout[1][1] == layout[2][2]):
        return layout[0][0]

    # Verifica diagonal secundaria
    if(layout[0][2] != vazio and layout[0][2] == layout[1][1] and layout[1][1] == layout[2][0]):
        return layout[0][2]

    for i in range(3):
        for j in range(3):
            if(layout[i][j] == vazio):
                return False

    return "Empate"
