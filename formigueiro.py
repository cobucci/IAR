from random import *

def criarAmbiente(tamanho, quantidadeItens):

    # cria o ambiente e coloca todos os valores como sendo 0 (nao tem item)
    matriz = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(0)
        matriz.append(linha)


    #print(matriz)

    #dispor os itens (60%)
    porcentagem = tamanho*tamanho/100*quantidadeItens
    #print(tamanho*tamanho)
    #print(porcentagem)

    for i in range(int(porcentagem)):
        lin = randrange(0, tamanho)
        col = randrange(0, tamanho)
        while matriz[lin][col] == 1:
            lin = randrange(0, tamanho)
            col = randrange(0, tamanho)
        matriz[lin][col] = 1

    #print(matriz)
    return matriz

def criarFormigas(quantidadeFormigas, tamanho):

    #inicio as formigas na mesma posicao
    formigas = []
    for i in range(quantidadeFormigas):
        linha = []
        for j in range(2):
            linha.append(0)
        formigas.append(linha)

    for i in range(quantidadeFormigas):
        for j in range(2):
            if j == 0:
                lin = randrange(0, tamanho)
                formigas[i][j] = lin
            else:
                col = randrange(0, tamanho)
                formigas[i][j] = col

    #print(formigas)
    return formigas


def deslocamento(matriz, formigas, raioDeVisao, iteracoes):

    for i in range(iteracoes):
        for j in range(len(formigas)):
            #para cada formiga
                #se ela tiver numa celula com item, definir se pega ou nao o item
                    #se pegar, pra onde mover
                #se tiver numa celula sem item, movimentar

            #print("%d - %d" % (formigas[j][0], formigas[j][1]))
            if matriz[formigas[j][0]][formigas[j][1]] == 1:
                if pegarLargar(matriz, formigas[j][0], formigas[j][1], raioDeVisao):
                    #print("peguei item")
                    #mudarPosicaoItem(matriz, formigas[j][0], formigas[j][1], raioDeVisao)
                    matriz, novaLinFormiga, novaColFomiga = mudarPosicaoItem(matriz, formigas[j][0], formigas[j][1], raioDeVisao)
                    matriz[formigas[j][0]][formigas[j][1]] = 0
                    formigas[j][0] = novaLinFormiga
                    formigas[j][1] = novaColFomiga
                else:
                    #print("Nao peguei o item")
                    #se nao peguei, tenho que andar
                    formigas[j][0], formigas[j][1] = mudarPosicaoFormiga(matriz, formigas[j][0], formigas[j][1], raioDeVisao)
            else:
                formigas[j][0], formigas[j][1] = mudarPosicaoFormiga(matriz, formigas[j][0], formigas[j][1], raioDeVisao)

def mudarPosicaoFormiga(matriz, formigaLinha, formigaColuna, raioDeVisao):
    ondeNaoTemItem = []
    for i in range(1, raioDeVisao + 1):
        # cima
        if formigaLinha - (i) >= 0:
            posicao = []
            posicao.append(formigaLinha - i)
            posicao.append(formigaColuna)
            ondeNaoTemItem.append(posicao)
        # baixo
        if formigaLinha + (i) < len(matriz):
            posicao = []
            posicao.append(formigaLinha + i)
            posicao.append(formigaColuna)
            ondeNaoTemItem.append(posicao)
        # direita
        if formigaColuna + (i) < len(matriz):
            posicao = []
            posicao.append(formigaLinha)
            posicao.append(formigaColuna + i)
            ondeNaoTemItem.append(posicao)
        # esquerda
        if formigaColuna - (i) >= 0:
            posicao = []
            posicao.append(formigaLinha)
            posicao.append(formigaColuna - i)
            ondeNaoTemItem.append(posicao)

        # diagonal superior esquerda
        if formigaLinha - (i) >= 0 and formigaColuna - (i) >= 0:
            posicao = []
            posicao.append(formigaLinha - i)
            posicao.append(formigaColuna - i)
            ondeNaoTemItem.append(posicao)

        # diagonal superior direita
        if formigaLinha - (i) >= 0 and formigaColuna + (i) < len(matriz):
            posicao = []
            posicao.append(formigaLinha - i)
            posicao.append(formigaColuna + i)
            ondeNaoTemItem.append(posicao)

        # diagonal inferior esquerda
        if formigaLinha + (i) < len(matriz) and formigaColuna - (i) >= 0:
            posicao = []
            posicao.append(formigaLinha + i)
            posicao.append(formigaColuna - i)
            ondeNaoTemItem.append(posicao)

        # diagonal inferior direita
        if formigaLinha + (i) < len(matriz) and formigaColuna + (i) < len(matriz):
            posicao = []
            posicao.append(formigaLinha + i)
            posicao.append(formigaColuna + i)
            ondeNaoTemItem.append(posicao)

    celulaItem = randrange(0, len(ondeNaoTemItem))
    novaLinhaFormiga = ondeNaoTemItem[celulaItem][0]
    novaColunaFomiga = ondeNaoTemItem[celulaItem][1]
    return novaLinhaFormiga, novaColunaFomiga

def mudarPosicaoItem(matriz, formigaLinha, formigaColuna, raioDeVisao):

    ondeNaoTemItem = []
    for i in range(1, raioDeVisao+1):
        #cima
        if formigaLinha - (i) >= 0:
            if matriz[formigaLinha - i][formigaColuna] == 0:
                posicao = []
                posicao.append(formigaLinha - i)
                posicao.append(formigaColuna)
                ondeNaoTemItem.append(posicao)
        #baixo
        if formigaLinha + (i) < len(matriz):
            if matriz[formigaLinha + i][formigaColuna] == 0:
                posicao = []
                posicao.append(formigaLinha + i)
                posicao.append(formigaColuna)
                ondeNaoTemItem.append(posicao)
        #direita
        if formigaColuna + (i) < len(matriz):
            if matriz[formigaLinha][formigaColuna + i] == 0:
                posicao = []
                posicao.append(formigaLinha)
                posicao.append(formigaColuna + i)
                ondeNaoTemItem.append(posicao)
        #esquerda
        if formigaColuna - (i) >= 0:
            if matriz[formigaLinha][formigaColuna - i] == 0:
                posicao = []
                posicao.append(formigaLinha)
                posicao.append(formigaColuna - i)
                ondeNaoTemItem.append(posicao)

        #diagonal superior esquerda
        if formigaLinha - (i) >= 0 and formigaColuna - (i) >= 0:
            if matriz[formigaLinha - i][formigaColuna - i] == 0:
                posicao = []
                posicao.append(formigaLinha - i)
                posicao.append(formigaColuna - i)
                ondeNaoTemItem.append(posicao)

        #diagonal superior direita
        if formigaLinha - (i) >= 0 and formigaColuna + (i) < len(matriz):
            if matriz[formigaLinha - i][formigaColuna + i] == 0:
                posicao = []
                posicao.append(formigaLinha - i)
                posicao.append(formigaColuna + i)
                ondeNaoTemItem.append(posicao)

        # diagonal inferior esquerda
        if formigaLinha + (i) < len(matriz) and formigaColuna - (i) >= 0:
            if matriz[formigaLinha + i][formigaColuna - i] == 0:
                posicao = []
                posicao.append(formigaLinha + i)
                posicao.append(formigaColuna - i)
                ondeNaoTemItem.append(posicao)

        # diagonal inferior direita
        if formigaLinha + (i) < len(matriz) and formigaColuna + (i) < len(matriz):
            if matriz[formigaLinha + i][formigaColuna + i] == 0:
                posicao = []
                posicao.append(formigaLinha + i)
                posicao.append(formigaColuna + i)
                ondeNaoTemItem.append(posicao)


    #escolher um ponto de onde nao tem item, pra colocar o item la
    celulaItem = randrange(0, len(ondeNaoTemItem))
    matriz[ondeNaoTemItem[celulaItem][0]][ondeNaoTemItem[celulaItem][1]] = 1
    novaLinhaFormiga = ondeNaoTemItem[celulaItem][0]
    novaColunaFomiga = ondeNaoTemItem[celulaItem][1]
    return matriz, novaLinhaFormiga, novaColunaFomiga


def pegarLargar(matriz, formigaLinha, formigaColuna, raioDeVisao):

    #contabilizar quantos itens no total eu posso ver, quantos tem itens e tirar uma porcentagem
    quantidadeCelulasVistas = 0
    quantidadeCelulasComItem = 0
    #pra cima, baixo, esquerda, direita
    #cima
    for i in range(1, raioDeVisao+1):
        #cima
        if formigaLinha - (i) >= 0:
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha - i][formigaColuna] == 1:
                quantidadeCelulasComItem += 1
        #baixo
        if formigaLinha + (i) < len(matriz):
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha + i][formigaColuna] == 1:
                quantidadeCelulasComItem += 1
        #direita
        if formigaColuna + (i) < len(matriz):
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha][formigaColuna + i] == 1:
                quantidadeCelulasComItem += 1
        #esquerda
        if formigaColuna - (i) >= 0:
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha][formigaColuna - i] == 1:
                quantidadeCelulasComItem += 1

        #diagonal superior esquerda
        if formigaLinha - (i) >= 0 and formigaColuna - (i) >= 0:
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha - i][formigaColuna - i] == 1:
                quantidadeCelulasComItem += 1
        #diagonal superior direita
        if formigaLinha - (i) >= 0 and formigaColuna + (i) < len(matriz):
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha - i][formigaColuna + i] == 1:
                quantidadeCelulasComItem += 1
        # diagonal inferior esquerda
        if formigaLinha + (i) < len(matriz) and formigaColuna - (i) >= 0:
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha + i][formigaColuna - i] == 1:
                quantidadeCelulasComItem += 1
        # diagonal inferior direita
        if formigaLinha + (i) < len(matriz) and formigaColuna + (i) < len(matriz):
            quantidadeCelulasVistas += 1
            if matriz[formigaLinha + i][formigaColuna + i] == 1:
                quantidadeCelulasComItem += 1


    #print(quantidadeCelulasVistas)
    #print(quantidadeCelulasComItem)
    #porcentagem de chance de pegar ou largar
    porcentagemNaoPegarItem = (quantidadeCelulasComItem*100)/quantidadeCelulasVistas
    print(porcentagemNaoPegarItem)
    pegarItem = randint(0, 100)
    #nao pegar item vai de 0 ate porcentagemNaoPegarItem
    #pegar item vai de porcentagemNaoPegarItem + 1 ate 100
    if pegarItem > int(porcentagemNaoPegarItem):
        return 1
        #peguei o item
    else:
        return 0
        #nao peguei o item

def printarMatriz(matriz):

    #lembrando: 0 -> nao tem item | 1 -> tem item
    for i in range(len(matriz)):
        linha = "|"
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                linha += " "
            else:
                linha += "x"
        linha += "|"
        print(linha)
    print("-----------------")

def main():

    quantidadeLinhasColunas = 10
    porcentagemDeItensEmRelacaoAoTotalDeCelulas = 60
    quantidadeDeFormigas = 10
    raioDeVisao = 1
    iteracoes = 50000

    #criaAmbiente(quantidadeLinhasColunas, porcentagemDeItensEmRelacaoAoTotalDeCelulas)
    matriz = criarAmbiente(quantidadeLinhasColunas, porcentagemDeItensEmRelacaoAoTotalDeCelulas)
    printarMatriz(matriz)

    #criaFormigas(quantidadeDeFormigas, quantidadeLinhasColunas)
    formigas = criarFormigas(quantidadeDeFormigas, quantidadeLinhasColunas)

    #descamento(matriz, formigas, raioDeVisao, iteracoes)
    deslocamento(matriz, formigas, raioDeVisao, iteracoes)
    printarMatriz(matriz)


main()