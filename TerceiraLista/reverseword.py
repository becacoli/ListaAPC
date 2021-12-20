#Algoritmo que recebe uma palavra e imprime o reverso dessa palavra

word = input("Digite uma palavra: ") 
reversed_word = ""

for x in word:
  reversed_word = x + reversed_word

print(f"O reverso de {word} é {reversed_word}")

