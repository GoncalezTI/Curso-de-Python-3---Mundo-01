# 006 - Crie um algoritmo que leia um número e
# mostre o seu dobro, triplo e raiz quadrada.

n = int(input('\033[1;32mDigite um número:\033[m '))
print('O dobro de \033[1;33m{}\033[m vale \033[1;33m{}\033[m.'.format(n, (n*2)))
print('O triplo de \033[1;33m{}\033[m vale \033[1;33m{}\033[m. \nA raiz'
      ' quadrada de \033[1;33m{}\033[m é igual a \033[1;33m{:.2f}\033[m.'
      .format(n, (n*3), n, pow(n, (1/2))))
