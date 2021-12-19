#Faça um programa que receba três números e ordene eles em ordem crescente.

a = int(input("Digite um número:\n"))
b = int(input("Digite um número:\n"))
c = int(input("Digite um número:\n"))

if a > c:
    a, c = c, a

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

print(f"A ordem crescente é {a}, {b} e {c}")
