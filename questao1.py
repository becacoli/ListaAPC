with open("ex_q1.txt") as arquivo:

    maiores_valores = []
    maior = 0

    for i, numero in enumerate(arquivo):
        if int(numero) > maior:
            maior = int(numero)

        if (i+1) % 5 == 0:
            maiores_valores.append(int(maior))
            maior = 0

print(maiores_valores)