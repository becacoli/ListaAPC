#Algoritmo que recebe uma palavra e um caractere e conta as ocorrências do caractere na palavra

word = input("Digite uma palavra: ").upper()
letter = input("Digite uma letra: ").upper()

ocurrences = 0

for letra in range(len(word)):
  if word[letra] == letter:
    ocurrences += 1

   
    
   


print(ocurrences)
