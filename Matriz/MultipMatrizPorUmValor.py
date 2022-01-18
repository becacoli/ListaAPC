#Multiplicando uma matriz por um inteiro
def CriarMatriz(n):

    lista = []
    matriz = []
    for i in range(0, n):
        for j in range(0, n):
             lista.append(int(input(f"Digite um valor para [{i},{j}] da matriz A: ")))     
        matriz.append(lista)   
        lista = []
    
    return matriz

def MultiInteiro(matriz, inteiro):
    for i in range(len(matriz)):
      for j in range(len(matriz[0])):
        matriz[i][j] = matriz[i][j] * inteiro
    return matriz

n = int(input("Digite um número para definir a quantidade de linhas e colunas da matriz: "))
inteiro = int(input("Digite um número inteiro para ser o multiplicador: "))
Matriz = CriarMatriz(n)
matriz = MultiInteiro(Matriz, inteiro)

for i in matriz:
          print(' '.join(str(i))) 
