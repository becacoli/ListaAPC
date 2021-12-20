#Algoritmo que recebe uma palavra e conta quantas vogais há na palavra

word = input("Digite uma palavra: ").lower()

def vowels_counter(word):
  ocurrences = 0
  vowels = "aeiou"

  for x in vowels:
        if x in word:
            ocurrences += word.count(x)
  return ocurrences

print(vowels_counter(word))
