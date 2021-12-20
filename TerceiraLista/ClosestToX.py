#Faça um programa que recebe um conjunto de inteiros e um valor n e indica qual o valor mais próximo de n no conjunto

conjunto = []

for n in range(0,5):
  elementos = int(input("Elementos do conjunto: "))
  conjunto.append(elementos)

n = int(input("Digite um valor para n: "))

cont = 1
closer = 0 

for numero in conjunto:
  if abs(numero - n) <= cont and numero != n:
    closer = numero
    break

  
    

print(f"O número mais próximo de {n} é {closer}")

