#Algoritmo que recebe um conjunto de inteiros e dois números e verifica se estes dois numeros ocorrem em sequência no conjunto

conjunto = []
numbers = []


for x in range(3):
  elementos = int(input("Digite os elementos do conjunto: "))
  conjunto.append(elementos)

for x in range(2):
  num = int(input("Digite os números do conjunto: "))
  numbers.append(num)

for x in range(len(conjunto)):
   if len(conjunto) > x+1:
    if numbers[0] == conjunto[x]:
      if numbers[1] == conjunto[x+1]: 
        print("Ocorre em sequência! :)")
    else: 
      print("Não ocorre em sequência :( ")
