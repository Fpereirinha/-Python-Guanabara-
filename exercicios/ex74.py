from random import randint
numero = [randint(0,999),randint(0,999),randint(0,999),randint(0,999),randint(0,999)]
print(f'Os números sorteados são: ', end= '')
for c in numero:
    print(f'{c}', end=' ')
print(f'\nO maior número é o {max(numero)}\n'
      f'O menor é o {min(numero)}')
print('Os números parés são: ', end= '')
for c in numero:
    if c % 2 == 0:
        print(c, end= ' ')
print('\nOs números impares são: ', end='')
for c in numero:
    if c % 2 == 1:
        print(c, end=' ')

