lista = []
soma = interrompe = 0
while True:
    temp = []
    temp.append(str(input('Qual o nome ?')))
    temp.append(int(input('Qual a 1° nota ?')))
    temp.append(int(input('Qual a 2° nota ?')))
    lista.append(temp[:])
    resp = str(input('Quer continuar ? S/N')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar ? S/N'))
    if resp == 'N':
        break
print(f'{"N.":<8} {"NOME":<8} {"Média":<8}')
for x, c in enumerate(lista):
    for posicao, valor in enumerate(c):
        if posicao == 0:
            print(f'{x:<8}', end='')
            print(f'{valor:<8}', end='')
        else:
            soma += valor
    print(f'{soma/2:<8}')
    soma = 0
while True:
    interrompe = int(input('Mostrar as notas de qual aluno ? 999 para interromper.'))
    if interrompe == 999:
        break
    else:
        print(f'Notas de {lista[interrompe][0]} são {lista[interrompe][1:]}')
