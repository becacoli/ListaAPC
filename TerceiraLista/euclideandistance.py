#Faça um algoritmo que recebe dois conjuntos de inteiros A e B e calcula a distância euclidiana entre estes dois conjuntos

ConjuntoA = []
ConjuntoB = []

for x in range(0, 3):
  elementos = int(input("Elementos do conjunto A: "))
  ConjuntoA.append(elementos)

for x in range(0, 3):
  elementos = int(input("Elementos do conjunto B: "));
  ConjuntoB.append(elementos)

distance = ((ConjuntoA[0]-ConjuntoB[0])**2 + (ConjuntoA[1]-ConjuntoB[1])**2 + (ConjuntoA[2]-ConjuntoB[2]**2))**1/2


print(f"A distância euclidiana entre estes dois conjuntos é {distance}")
