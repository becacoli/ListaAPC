#Escreva um algoritmo que recebe três valores para os lados de um triângulo (a,b e c) e decide se a forma geométrica é um triângulo ou não e em caso positivo, classifique em isósceles, escaleno ou equilátero.

a = float(input("Digite o lado 1:\n"))
b = float(input("Digite o lado 2:\n"))
c = float(input("Digite o lado 3:\n"))

tri = "É um triângulo"

if (b + c < a) and (a + c < b) and (a + b < c):
  print("Não é triângulo!!")
elif (a==b) and (b==c):
  print(f"{tri} e é equilátero")
elif (a == b) or (a == c) or (b == c):
  print(f"{tri} e é isósceles")
else:
    print(f"{tri} e é escaleno")
