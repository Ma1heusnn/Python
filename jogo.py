"""
Jogo da Velha em Python!
"""

#   Realiza a exibição do tabuleiro com "|" cortando entre os números
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | " .join(linha))

#   Checa se houve vencedor ou não
def verificar(tabuleiro, jogador):
    #checagem linhas
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        
    #checagem colunas
    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
        
    #checagem diagonais
    for i in range(3):
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            return True
        if tabuleiro[0][2] == jogador and tabuleiro[1][1]  == jogador and tabuleiro[2][0] == jogador:
            return True
        
    return False

tabuleiro = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
jogador_atual = "X"

#   Define o número de rodadas a serem jogadas e a posição escolhida pelo jogador
for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f"Jogador {jogador_atual}, digite a posição que deseja jogar (1-9): ")
    pos = int(escolha) - 1
    linha, coluna = pos // 3, pos % 3 

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posição já ocupada; tente outra.")
        continue

    tabuleiro[linha][coluna] = jogador_atual

 #   Verifica se houve vencedor ou não
    if verificar(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual} venceu!")
        break

    #   Realiza a troca entre os jogadores
    if jogador_atual == "O":
        jogador_atual = "X"
    else:
        jogador_atual = "O"

   

   