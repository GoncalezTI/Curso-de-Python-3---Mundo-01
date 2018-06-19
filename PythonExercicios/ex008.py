# 008 - Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

medida = float(input('\033[1;32;46mUma distância em metros:\033[m '))
cm = medida * 100
mm = medida * 1000
print('A medida de \033[4;33m{}m\033[m corresponde a \033[4;33m{:.0f}cm\033[m e '
      '\033[4;33m{:.0f}mm\033[m'.format(medida, cm, mm))
