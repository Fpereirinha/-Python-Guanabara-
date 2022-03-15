listagem = ('Lápis', 1.88,
            'Caneta', 5.00,
            'Estojo', 8.00,
            'Lapiseira', 10.00,
            'Caderno', 15.00,
            'Bic 4 cores', 120.00)
print(f'{"Listagem de Preços":-^40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print(f'{"FIM":-^40}')

'''lista = ()
soma = cont = 0
while True:
    produto = str(input('Digite o nome do produto: ')).upper().strip()
    valor = float(input('Digite o preço: '))
    lista += produto, valor
    continuar = str(input('Quer continuar? [S/N]')).strip()
    while continuar not in 'SsNn':
        continuar = str(input('Tente novamente. Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-=' * 18)
print(f'{"LISTA DE PRODUTOS":^36}\n')
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<25} R$ {lista[c + 1]:.2f}')
    cont += 1
for c in range(1, len(lista), 2):
    soma += lista[c]
print()
print(f'Você comprou {cont} produtos e a soma')
print(f'deles foi de R$ {soma:.2f}')
print('-=' * 18)'''