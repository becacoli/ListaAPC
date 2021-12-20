#Faça um programa que recebe um conjunto de inteiros e verifica se existe algum número negativo no conjunto

conjunto = []
num = 0

for n in range(0, 5):
  elementos = int(input("Elementos do conjunto: "))
  conjunto.append(elementos)

for n in conjunto:
  if (n < 0):
    num += 1
print(f"Existe {num} números negativos no conjunto.")
