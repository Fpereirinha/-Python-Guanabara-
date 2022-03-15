from random import randint
numero = [randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
print(f'Os números sorteados são: ', end= '')
for c in numero:
    print(f'{c}', end=' ')
print(f'\nO maior número é o {max(numero)}\n'
      f'O menor é o {min(numero)}')

