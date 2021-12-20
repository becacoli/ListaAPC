#Faça um programa programa que recebe um conjunto de inteiros e conta quantos elementos maiores que n existem no conjunto

up = []
maiores_n = 0 

for x in range(0, 5):
  conjunto = int(input("Elementos do conjunto: "))
  up.append(conjunto)
n = int(input("Digite um valor para n: "))

for x in up:
  if (x > n):
    maiores_n += 1

print("Há",maiores_n,"elementos maiores que n.")
