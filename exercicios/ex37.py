n = int(input('Digite um número a ser convertido:'))
print('''Digite para qual medida quer que converta:
[1] BINARIO
[2] HEXADECIMAL
[3] OCTAL''')
x = int(input(''))
if x == 1:
    print('{} convertido para bínario é {}.'.format(n, bin(n)[2:]))
elif x == 2:
    print('{} convertido para hexadecimal é {}'.format(n, hex(n)[2:]))
elif x == 3:
    print('{} convertido em octal é {}.'.format(n, oct(n)[2:]))
else:
    print('Opção inválida, revise os dados.')

