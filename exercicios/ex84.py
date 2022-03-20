dados = []
pessoas = []
c = 0
mai = menor = tempme = tempm = 0
while True:
    dados.append(str(input(f'Digita o nome da {c+1}° Pessoa: ')).strip())
    dados.append(int(input(f'Digita o peso da {c+1}° Pessoa: ')))
    if c == 0:
        mai = menor = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    c += 1
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(pessoas)
print(f'O total de pessoas cadastradas foi {c}.')
for p in pessoas:
    if p[1] == menor:
        tempme += 1
print(f'O menor peso foi {menor:.2f}kg. ', end='')
print(f'Das seguintes pessoas: ' if tempme > 1 else 'Da pessoa:')
for p in pessoas:
    if p[1] == menor:
        print(p[0])
print(f'O maior peso foi {mai:.2f}kg. ', end='')
for p in pessoas:
    if p[1] == mai:
        tempm += 1
print(f'Das seguintes pessoas: ' if tempm > 1 else 'Da pessoa:')
for p in pessoas:
    if p[1] == mai:
        print(p[0])
