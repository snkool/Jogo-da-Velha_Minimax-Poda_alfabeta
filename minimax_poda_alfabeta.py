import time
from j_velha import vazio, jogador_token, verificaVitoria

# Função responsável por verificar todos os espaços que ainda estão vazios na matriz e adicionais na lista 'posicoes'
def getPosicao(layout):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(layout[i][j] == vazio):
                posicoes.append([i, j])
    
    return posicoes

# Função responsável por retornar as posicoes em que a IA decidiu marcar e realizar a Poda Alfa-Beta
def marcaPosicaoIA(layout, jogador):
    possibilidades = getPosicao(layout) # Variável recebe todas as posições da matriz do jogo da velha, para saber quais ainda estão disponíveis para jogar
    melhor_valor = None # Variável armazena o melhor valor de jogada retornado pela função do minimax 
    melhor_movimento = None # Variável armazena o melhor movimento vindo da comparação da lista de possibilidades
    alfa = 0.0
    beta = 0.0

    # Roda um for dentro da lista 'possibilidades', onde estao as posicoes da matriz do jogo
    for possibilidade in possibilidades:
        # Valores retornadados pelo Minimax que fazem a IA perder ou preferir 'garantir a vitoria'
        chance_x = 0.3333333333333333
        chance_x2 = -0.5
        chance_x3 = 0.5

        layout[possibilidade[0]][possibilidade[1]] = jogador_token[jogador] # Define o X ou O para marcar no layout do jogo
        valor = minimax(layout, jogador) # Recebe o valor de "chance de vitoria" retornado pela função de Minimax  
        layout[possibilidade[0]][possibilidade[1]] = vazio # Limpa o jogador que foi definido anteriormente
        
        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade    

            if(melhor_valor > alfa and valor != chance_x2):
               alfa = valor

            if(alfa >= beta and alfa != chance_x and alfa != chance_x2 and alfa > 0):
                if(valor != chance_x and valor != chance_x2):
                    return melhor_movimento[0], melhor_movimento[1]  

        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade  

            if(melhor_valor < beta and valor != chance_x3):
                beta = melhor_valor

            if(beta <= alfa and valor != chance_x3 and valor != chance_x2):
                return melhor_movimento[0], melhor_movimento[1] 
        #print(valor)
        #print(melhor_movimento[0], melhor_movimento[1])
    return melhor_movimento[0], melhor_movimento[1]

# 0 = Empate, 1 = Vitória X, -1 = Vitória O
resultado = {
    "Empate": 0,
    " \033[33mX\033[m ": 1,
    " \033[35mO\033[m ": -1
}

# Função Minimax
def minimax(layout, jogador, profundidade = 1):
    ganhador = verificaVitoria(layout)
    if(ganhador):
        #return resultado[ganhador] 
        return resultado[ganhador] / profundidade # A cada vez que  o minimax é chamado dentro do minimax é adicionado 1 na variavel profundidade, 
                                                  # assim quanto mais profundo for necessário para ganhar, mais próximo de 0 (Empate) será o resultado
    
    jogador = (jogador + 1) % 2 # Alterna o jogador entre X (0) ou O (1)
    
    possibilidades = getPosicao(layout)
    melhor_valor = None

    for possibilidade in possibilidades:
        layout[possibilidade[0]][possibilidade[1]] = jogador_token[jogador]
        valor = minimax(layout, jogador, profundidade + 1)
        layout[possibilidade[0]][possibilidade[1]] = vazio

        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor
  