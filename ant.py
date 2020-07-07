from random import *

def criarAmbiente(tamanho, quantidadeItens):

    # cria o ambiente e coloca todos os valores como sendo 0 (nao tem item)
    matriz = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(0)
        matriz.append(linha)


    print(matriz)

    #dispor os itens (60%)
    porcentagem =  ((tamanho*tamanho) * 60) / 100
    print(porcentagem)
    random.seed()
    for i in range(porcentagem):
        lin = randrange(0, tamanho)
        col = randrange(0, tamanho)
        while matriz[lin][col] == 1:
            lin = randrange(0, tamanho)
            col = randrange(0, tamanho)
        matriz[lin][col] == 1

    print(matriz)


criarAmbiente(10, 5)
