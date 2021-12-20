#Faça um programa que recebe um conjunto de inteiros e imprime os valores que estão abaixo da média do conjunto

conjunto = []
valoresunder = []
under = 0

for n in range(0,5):
  elementos = int(input("Elementos do conjunto: "))
  conjunto.append(elementos)

mean = sum(conjunto)/len(conjunto)

for n in conjunto:
  if (n < mean):
      valoresunder.append(n)
      under += 1
print("Os valores abaixo da média são:", valoresunder)
