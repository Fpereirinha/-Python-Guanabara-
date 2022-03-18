lista = []
while True:
    n = int(input('Digite um valor:'))
    while n in lista:
        print('Valor já inserido, tente novamente.')
        n = int(input('Digite um valor:'))
    lista.append(n)
    s = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    while s not in 'SN':
        print('Digite sim ou não !!!')
        s = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if s == 'N':
        break
print(f'Você digitou {len(lista)} elementos.' if len(lista) > 1 else f'Você digitou {len(lista)} elemento.')
print(f'A lista em ordem decrescente é: ')
for c, x in enumerate(sorted(lista, reverse=True)):
    if c < len(lista)-1:
        print(x, end=',')
    else:
        print(x, end='.')
if 5 in lista:
    print(f'\nO valor 5 foi encontrado na lista, na posição {sorted(lista, reverse= True).index(5)+1}.')
else:
    print('\nO valor 5 não foi encontrado na lista.')
