palavra = list(input("Digite uma palavra: "))

with open("questao3.txt", "w") as arquivo:
    for _ in palavra: 
        ultima_letra = palavra.pop() #Removendo a última letra
        palavra.insert(0, ultima_letra) #Colocando o último caractere no início
        print("".join(palavra))
        arquivo.write("".join(palavra) + "\n")

