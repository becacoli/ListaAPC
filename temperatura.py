arquivo = open("temperaturamedia.txt")

def MediaAnual(lista):
    return sum(lista)/len(lista)

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperatura_media = []

for temperatura in arquivo:
    temperatura_media.append(float(temperatura.rstrip()))

print(temperatura_media)

acima_media = {}
media = MediaAnual(temperatura_media)

for i in range(len(meses)):
    if temperatura_media[i] > media:
        acima_media.update({meses[i] : temperatura_media[i]})

print(f"Média anual das temperaturas {round(media)}\nMeses com temperatura acima da média {acima_media}")


arquivo.close()