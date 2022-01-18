#Verificando se tem número existe em uma lista
def CriarMatriz(n):

    lista = []
    matriz = []
    for i in range(0, n):
        for j in range(0, n):
             lista.append(int(input(f"Digite um valor para [{i},{j}] da matriz A: ")))     
        matriz.append(lista)   
        lista = []
    
    return matriz

def IsThereInM(matriz, x):
    existe = False
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == x:
                existe = True
    if existe:
        return "O número inteiro existe na matriz"
    else:
        return "O número inteiro não existe na matriz"

n = int(input("Digite um número para definir a quantidade de linhas e colunas da matriz: "))
matriz = CriarMatriz(n)
inteiro = int(input("Digite um número inteiro para verificar se ele existe na matriz: "))


print(IsThereInM(matriz, inteiro))
