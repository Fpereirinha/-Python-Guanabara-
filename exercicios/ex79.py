num = []
soma = 0
while True:
    z = int(input('Digite um valor: '))
    if z in num:
        print('Valor não será adicionado pois está duplicado.')
    else:
        print('Valor adicionado com sucesso.')
        num.append(z)
    x = str(input('Quer continuar ? S/N')).upper().strip()[0]
    while x not in 'SN':
        print('opção inválida.')
        x = str(input('Quer continuar ? S/N')).upper().strip()[0]
    if x == 'N':
        break
print(f'Os números em ordem crescente são: ', end='')
for x, c in enumerate(sorted(num)):
    if x < len(num) - 1:
        print(c, end=', ')
    else:
        print(c, end='.')
print('\nA soma é: ', end='')
for x, c in enumerate(sorted(num)):
    if x < len(num)-1:
        print(f'{c}+', end='')
        soma += c
    else:
        print(f'{c}', end='')
        soma += c
print(f'={soma}.')
