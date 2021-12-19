#Faça um programa que leia a idade de uma pessoa e imprima sua categoria:
#– Criança, se menor de 14 anos
#– Adolescente, se entre 14 e 17 anos
#– Adulto, se entre 18 e 59 anos
#– Idoso, se maior que 60 anos

print("Descubra a sua categoria baseada na sua idade!")
idade = int(input("Qual é a sua idade?\n"))

if 0 < idade < 14:
  categoria = "criança"
if 14 <= idade <= 17:
  categoria = "adolescente"
if 18 <= idade <= 59:
  categoria = "adulto"
if idade >= 60:
  categoria = "idoso"
print("Parabéns, você é um(a):", categoria)
