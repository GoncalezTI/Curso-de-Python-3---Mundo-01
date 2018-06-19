# 003 - Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre \033[1;31m{}\033[m e \033[1;31m{}\033[m é '
      'igual a \033[1;31m{}\033[m!'.format(n1, n2, s))
