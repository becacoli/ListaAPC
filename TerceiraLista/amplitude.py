#Faça um programa que recebe um conjunto de inteiros e calcula a amplitude do conjunto

conjunto = []
maior = 0
menor = 0


for x in range(5):
    elementos = int(input("Digite os elementos do conjunto: "))
    conjunto.append(elementos)
    if x == 0:
      maior = menor = conjunto[x]
    else: 
        if conjunto[x] > maior:
          maior = conjunto[x]
        if conjunto[x] < menor:
          menor = conjunto[x]



amplitude = maior - menor

print(f"A amplitude do conjunto é: {amplitude}")


