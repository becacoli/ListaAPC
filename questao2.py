def LetraComMaisFrequencia(frequencia):
    maior = 0
    chave_maior = ""
    for chave, valor in frequencia.items():
        if valor > maior:
            maior = valor
            chave_maior = chave
    return chave_maior, maior
        

alfabeto = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

frequencia = {}

with open("ex_q2.txt") as arquivo:
    numero_de_letras = 0
    for caractere in arquivo.read():
        caractere_minusculo = caractere.lower()
        if caractere_minusculo in alfabeto:
            if not caractere_minusculo in frequencia:
                frequencia[caractere_minusculo] = 1
            else:
                frequencia[caractere_minusculo] += 1
            numero_de_letras += 1

    chave, maior = LetraComMaisFrequencia(frequencia)
    porcentagem = round((maior/numero_de_letras) * 100, 2)

    print(f"O caractere '{chave}' esteve frequente em {porcentagem}% do texto")

        


