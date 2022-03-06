x = int(input('Digite o número a ser verificado.'))
div = 0
for c in range(1,x+1):
    if x % c == 0:
        print('\033[34m', end= ' ')
        div += 1
    else:
        print('\033[33m', end=' ')
    print(c, end= ' ')
print(f'\n\033[m O número {x} foi divisivel {div}vezes.')
if div == 2:
    print('\n\033[34m é primo')
else:
    print('\n\033[33m Não é primo')




'''
x = int(input('Digite o número a ser verificado:'))
div = 0
for c in range(1, x+1):
    if x % c == 0:
        div +=1
    print(c)
if div == 2:
    print('é PRIMO.')
else:
    print('Não é primo.')
print(f'O número foi dividido {div} vezes.')'''