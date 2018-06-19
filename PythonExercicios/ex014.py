# 014 - Escreva um programa que converta uma temperatura digitada
# em ºC para ºF.

c = float(input('\033[4;34mInforme a temperatura em ºC:\033[m '))
f = 9 * c / 5 + 32
print('A temperatura de \033[1;36m{}ºC\033[m corresponde a \033[1;36m{}ºF\033[m!'
      .format(c, f))
