#Faça um algoritmo que leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius

f = int(input('Digite temperatura em Fahrenheit: '));
c = ( f - 32) * 5/9;
print('A temperatura é', "%.2f" % c ,'°C')
