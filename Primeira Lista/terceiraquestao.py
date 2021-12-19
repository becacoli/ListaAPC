#Faça um algoritmo que calcule e apresente o valor do volume de um cilindro, utilizando a fórmula V = π * raio2 * altura

pi = 3.14;
raio = int(input('Digite o raio do cilindro: '));
altura = int(input('Digite a altura do cilindo: '));
volume = pi * (raio**2)* altura

print('O volume do cilindro é', volume)
