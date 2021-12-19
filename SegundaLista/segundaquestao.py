#Escreva um programa que recebe o nome e o valor vendido por um corretor e indique qual será sua comissão


print("COMISSÃO")

Valor_de_Venda = int(input("Valor de venda:\n"))
Corretor = input("Corretor\n")

if Valor_de_Venda > 50000:
  comissao = Valor_de_Venda * 0.12
elif 30000 < Valor_de_Venda <= 50000:
  comissao = Valor_de_Venda * 0.095
else:
  comissao = Valor_de_Venda * 0.07

print(f"A comissão do(a) corretor(a) {Corretor} será de", "%.2f" % comissao
