#Faça um programa que recebe um conjunto de inteiros e um valor n e verifica se existe algum número com valor maior que n no conjunto

conjunto = []
num = 0

for k in range(0,5):
  elementos = int(input("Elementos do conjunto: "))
  conjunto.append(elementos)

n = int(input("Digite o valor de n: "))

for k in conjunto:
  if k > n:
    num += 1

print(f"Existe algum número maior que {n} nesse conjunto.")

