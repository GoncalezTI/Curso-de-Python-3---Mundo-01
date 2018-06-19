# 007 - Desenvolva um programa que leia duas notas de um aluno, calcule
# e mostre a sua média.

n1 = float(input('\033[1;33mPrimeira nota do aluno:\033[m '))
n2 = float(input('\033[1;33mSegunda nota do aluno:\033[m '))
média = (n1 + n2) / 2
print('A média entre \033[1;34m{:.1f}\033[m e \033[1;34m{:.1f}\033[m '
      'é igual a \033[1;33;46m{:.1f}\033[m'.format(n1, n2, média))
