def CriarMatriz(n):

    lista = []
    matriz = []
    for i in range(0, n):
        for j in range(0, n):
             lista.append(int(input(f"Digite um valor para [{i},{j}] da matriz A: ")))     
        matriz.append(lista)   
        lista = []

    for i in matriz:
          print(' '.join(str(i))) 
    
    return matriz

def MatrizTranspost(matriz, tr, n):
    for i in range(n):
        for j in range(n):
            tr[i][j] = matriz[j][i]


def MatrizSim(matriz, n):
    tr = [[ 0 for j in range(len(matriz[0]))] for i in range(len(matriz))]
    MatrizTranspost(matriz, tr, n)
    for i in range(n):            #Se não tiver mesma quantidade de linhas e colunas, vai ser falso
        for j in range(n):
           if tr[i][j] != matriz[i][j]:
                return False
    return True


n = int(input("Digite um número para definir a quantidade de linhas e colunas da matriz: "))
matriz = CriarMatriz(n)

if MatrizSim(matriz, n):
    print("É simétrica")
else:
    print("Não é simétrica")
