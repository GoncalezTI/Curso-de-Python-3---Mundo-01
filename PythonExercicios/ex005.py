# 005 - Faça um programa que leia um número inteiro e mostre
# na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print('Analisando o valor \033[7;30m{}\033[m, seu antecessor é \033[7;30m{}\033[m '
      'e seu sucessor é \033[7;30m{}\033[m.'.format(n, (n-1), (n+1)))
