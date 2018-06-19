# 016 - Crie um programa que leia um número real qualquer pelo
# teclado e mostre na tela a sua porção inteira.

'''MODO 1
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira '
      'é {}'.format(num, math.trunc(num)))

MODO 2
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira '
      'é {}'.format(num, trunc(num)))'''

# MODO 3
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira '
      'é {}'.format(num, int(num)))
