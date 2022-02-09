def ReceberDados(n):
    agenda_telefonica = {}
    for i in range(n):
        chave, nome = input("Digite o número e o contato: ").split(":")
        agenda_telefonica[chave] = nome
    return agenda_telefonica


arquivo = open("agenda.txt", "w")

n = int(input("Quantas pessoas serão adicionadas? "))
agenda = ReceberDados(n)

for chave, nome in agenda.items():
    arquivo.write(f"{chave}: {nome}\n")
    

print(agenda)

arquivo.close()
