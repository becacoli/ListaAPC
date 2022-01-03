#Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada

def ContadorDeVogais(palavra):
    vogais = "aeiou"

    contarvogais = {}.fromkeys(vogais, 0)

    for caracteres in palavra:
        if caracteres in contarvogais:
            contarvogais[caracteres] += 1

    return contarvogais


p = input("Digite uma palavra: ").lower()
quantidade = ContadorDeVogais(p) 
print(quantidade)
