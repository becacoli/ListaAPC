def CriarMatriz(n):

    lista = []
    matriz = []
    for i in range(0, n):
        for j in range(0, n):
             lista.append(int(input(f"Digite um valor para [{i},{j}] da matriz A: ")))     
        matriz.append(lista)   
        lista = []
    
    return matriz
def dimensoes(matriz):
    linhas = len(matriz)
    colunas = 0

    if linhas != 0:
        colunas = len(matriz[0])
    return linhas, colunas

def MatrizQuadrada(matriz):
    l, c = dimensoes(matriz)
    if l == c:
        return True
    else: 
        return False
        
def QuadradoMagico(matriz):
    if MatrizQuadrada(matriz) == False:
        return False

    l, c = dimensoes(matriz)

    #somando as linhas
    SomaDasLinhas = []
    for i in range(l):
        soma = 0
        for j in range(c):
            soma += matriz[i][j]
        SomaDasLinhas.append(soma)

    #somando as colunas
    SomaDasColunas = []
    for j in range(l):
        soma = 0
        for i in range(c):
            soma += matriz[i][j]
        SomaDasColunas.append(soma)

    #soma das diagonais
    SomaDiagonal1 = 0 #Diagonal Principal
    for i in range(l):
        SomaDiagonal1 += matriz[i][i]

    SomaDiagonal2 = 0 #Diagonal Secundária
    for i in range(l):
        SomaDiagonal2 += matriz[i][c-i-1] #a posição da coluna vai ser baseado na subtação da coluna, linha e 1

    #Validação do Quadrado Mágico

    soma = SomaDiagonal2

    for item in SomaDasLinhas:
        if item != soma:
            return "Não é um quadrado mágico :("
    for item in SomaDasColunas:
        if item != soma:
            return "Não é um quadrado mágico :("
    if SomaDiagonal1 != soma: 
        return "Não é um quadrado mágico :("

    return "É um quadrado mágico!!"

n = int(input("Digite a quantidade de linhas/colunas da matriz: "))
MATRIZ = CriarMatriz(n)

print(QuadradoMagico(MATRIZ))
