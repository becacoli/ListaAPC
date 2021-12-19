#Faça um algoritmo que leia dois valores para as variáveis A e B e efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresente os valores trocados.

A = int(input('Digite um valor: '))
B = int(input('Digite um valor: '))

A, B = B, A

print(f"Variável 1: {A} e Variável 2: {B}")
