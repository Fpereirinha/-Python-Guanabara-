num = tuple(int(input(f'Digite o {f1} valor'))for f1 in range(1,5))
print('A lista digitada é: ', end= '')
for c in num:
       print(c, end= ' ')
print(f'\nO número 9 aparece {num.count(9)}x' if 9 in num else '\nNão há valores 9 na lista.')
print(f'O número 3 aparece na {num.index(3)+1}° posição' if 3 in num else 'Não há números 3.')
print(f'Os números pares digitados foram: ', end='')
#print({n for n in num if n % 2 == 0}, end=' ') não pega valores repetidos !!! optei pela de baixo.
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')