from sys import float_repr_style


arquivo = open("notas.txt")

notas = []

for nota in arquivo:
    notas.append(float(nota.rstrip()))

quantidade_notas = len(notas)

soma = 0
for nota in notas:
    soma = soma + nota

acima_media = []
media = soma/quantidade_notas

for i in range(len(notas)):
    if notas[i] > media:
        acima_media.append(notas[i])

print(f"Notas recebidas:{notas}\nQuantidade de notas recebidas: {quantidade_notas}\nSomas das notas: {soma}\nMédia das notas: {media}\nNotas acima da média: {acima_media}")













arquivo.close()