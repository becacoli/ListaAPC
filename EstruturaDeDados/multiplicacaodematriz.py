#Escreva um programa que possua uma função que recebe duas matrizes e retorna a multiplicação destas matrizes
matrizA = [[0,0], [0,0]]

for l in range(0, 2):
    for c in range(0, 2):
        matrizA[l][c] = int(input(f"Digite um valor para [{l},{c}] da matriz A: "))

matrizB = [[0,0], [0,0]]

for l in range(0, 2):
    for c in range(0, 2):
        matrizB[l][c] = int(input(f"Digite um valor para [{l},{c}] da matriz B: "))

def MatrizMult(A, B):
    resp = [[0,0], [0,0]]
    for i in range(len(A)): #loops para interar linhas com colunas
        for j in range(len(B[0])):
             for m in range(len(B)):
                resp[i][j] += A[i][m] * B[m][j]
    return resp

print(MatrizMult(matrizA, matrizB))
