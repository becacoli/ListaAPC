#Crie um programa que calcula o pagamento com atraso de um boleto bancário -- O valor final a ser pago é dado por: -- Total = valor + multa + (valor* juros * dias) -- Sabendo que a multa é de 2 e a taxa de juros é de 0,05

Valor_do_boleto = int(input('Digite o valor do boleto:'));
Dias_de_atraso = int(input('Quantos dias o boleto está atrasado?: '))

multa = 2;
juros = 0.05;

Total_a_pagar = Valor_do_boleto + multa + (Valor_do_boleto*juros*Dias_de_atraso);

print('O valor do boleto com atraso é de', Total_a_pagar, 'reais');
