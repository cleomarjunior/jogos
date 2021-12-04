import random
import sys
import os


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
0

tab = [0, 1, 2,
       3, 4, 5,
       6, 7, 8]


def desenhar():
    print(tab[0], '|', tab[1], '|', tab[2])
    print('-' * 9)
    print(tab[3], '|', tab[4], '|', tab[5])
    print('-' * 9)
    print(tab[6], '|', tab[7], '|', tab[8])


def jogadaHumano():
    while True:
        posicao = input('Escolha a posição:')
        n = int(posicao)

        if (tab[n] == 'X' or tab[n] == 'O'):
            print('Posiçao inválida')
            continue
        else:
            break

    tab[n] = 'O'


def jogadaAI():
    print('Jogada da AI')
    opcoesValidas = []

    for i in range(0, 8):
        if (tab[i] != 'X' and tab[i] != 'O'):
            opcoesValidas.append(i)

    opcao = random.choice(opcoesValidas)
    tab[opcao] = 'X'


def ganhou(turno):
    if (
            # Avaliando as linhas
            (tab[0] == turno and tab[1] == turno and tab[2] == turno) or
            (tab[3] == turno and tab[4] == turno and tab[5] == turno) or
            (tab[6] == turno and tab[7] == turno and tab[8] == turno) or

            # Avaliando as colunas
            (tab[0] == turno and tab[3] == turno and tab[6] == turno) or
            (tab[1] == turno and tab[4] == turno and tab[7] == turno) or
            (tab[2] == turno and tab[5] == turno and tab[8] == turno) or

            # Avaliando as diagonais
            (tab[0] == turno and tab[4] == turno and tab[8] == turno) or
            (tab[2] == turno and tab[4] == turno and tab[6] == turno)
    ):
        return True
    else:
        return False


desenhar()

turnoHumano = True

for i in range(0, 9):
    if turnoHumano:
        jogadaHumano()

        if (ganhou('O')):
            desenhar()
            print('Jogador Humano ganhou')
            jogardnv = input("Deseja jogar novamente? Se sim responda 's' ou nao responda 'n'")
            if jogardnv == "s":
                restart_program()
            else:
                break
    else:
        jogadaAI()

        if (ganhou('X')):
            desenhar()
            print('AI ganhou')
            jogardnv = input("Deseja jogar novamente? Se sim responda 's' ou nao responda 'n'")
            if jogardnv == "s":
                restart_program()
            else:
                break

    desenhar()
    turnoHumano = not turnoHumano

    if (i == 8):
        print('Deu velha')
        print('Fim do jogo.')
        jogardnv = input("Deseja jogar novamente? Se sim responda 's' ou nao responda 'n'")
        if jogardnv == "s":
            print("carregando jogo...")
            restart_program()
        else:
            break