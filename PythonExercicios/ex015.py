# 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
# o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('\033[1;31mQuantos dias alugados?\033[m '))
km = float(input('\033[1;31mQuantos Km rodados?\033[m '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago é de \033[4;31mR${:.2f}\033[m'.format(pago))
