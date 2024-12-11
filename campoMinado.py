import random

def criar_ampco(tamanho, minas):
    # Cria um campo vazio com zeros
    campo = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    # Coloca as minas aleatoriamente
    minas_posicionadas = 0
    while minas_posicionadas < minas:
        x = random.randint(0, tamanho - 1)
        y = random.randint(0, tamanho - 1)
        if campo[x][y] != -1:  # -1 representa uma mina
            campo[x][y] = -1
            minas_posicionadas += 1

            # Atualiza os números ao redor da mina
            for i in range(max(0, x - 1), min(tamanho, x + 2)):
                for j in range(max(0, y - 1), min(tamanho, y + 2)):
                    if campo[i][j] != -1:
                        campo[i][j] += 1
    return campo

def exibir_campo(campo, visivel):
    tamanho = len(campo)
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if visivel[i][j]:
                linha.append(str(campo[i][j]) if campo[i][j] != -1 else "*")
            else:
                linha.append(".")
        print(" ".join(linha))

def revelar_celulas(campo, visivel, x, y):
    # Revela células vazias adjacentes
    if campo[x][y] == 0:
        for i in range(max(0, x - 1), min(len(campo), x + 2)):
            for j in range(max(0, y - 1), min(len(campo), y + 2)):
                if not visivel[i][j]:
                    visivel[i][j] = True
                    if campo[i][j] == 0:
                        revelar_celulas(campo, visivel, i, j)

def jogar():
    tamanho = 5  # Tamanho do campo
    minas = 5    # Número de minas
    campo = criar_ampco(tamanho, minas)
    visivel = [[False for _ in range(tamanho)] for _ in range(tamanho)]

    print("Bem-vindo ao Campo Minado!")
    print("Digite as coordenadas (linha e coluna) para revelar uma posição.")

    while True:
        exibir_campo(campo, visivel)
        linha = int(input(f"Escolha a linha (0 a {tamanho - 1}): "))
        coluna = int(input(f"Escolha a coluna (0 a {tamanho - 1}): "))

        # Verifica se as coordenadas são válidas
        if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
            print("Coordenadas inválidas, tente novamente.")
            continue

        # Revela a posição escolhida
        visivel[linha][coluna] = True

        # Revela células vazias adjacentes
        revelar_celulas(campo, visivel, linha, coluna)

        # Verifica se o jogador acertou uma mina
        if campo[linha][coluna] == -1:
            print("BOOM! Você acertou uma mina. Game Over!")
            exibir_campo(campo, [[True] * tamanho for _ in range(tamanho)])
            break

        # Verifica se o jogador venceu
        if all(visivel[i][j] or campo[i][j] == -1 for i in range(tamanho) for j in range(tamanho)):
            print("Parabéns, você venceu!")
            exibir_campo(campo, [[True] * tamanho for _ in range(tamanho)])
            break

# Inicia o jogo
jogar()