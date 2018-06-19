# 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

real = float(input('\033[1;33mQuanto dinheiro você tem na carteira? R$\033[m'))
dolar = real / 3.27
print('Com \033[1;31mR${:.2f}\033[m você pode comprar \033[1;31mUS${:.2f}\033[m'
      .format(real, dolar))
