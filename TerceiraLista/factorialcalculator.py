numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

while (numero > 1):
  fatorial = fatorial * numero
  numero = numero - 1
print(f"O fatorial é {fatorial}")
