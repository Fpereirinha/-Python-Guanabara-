partidas = []
geral = []
jogador = {}
while True:
    partidas.clear()
    jogador['Nome'] = str(input('Qual o nome do jogador ?'))
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou ?'))
    for c in range(total):
        n = int(input(f'Quantos gols ele marcou no {c + 1}° jogo ?'))
        partidas.append(n)
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    geral.append(jogador.copy())
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"JOGADOR"} {"Gols":>13} {"Total":>15}')
for contador, valor in enumerate(geral):
    print(f'{contador}', end=' ')
    for item in valor.values():
        print(f'{str(item):<15}', end='')
    print()
while True:
    n1 = str(input('Deseja saber os dados ? [S/N]')).strip().upper()[0]
    while n1 not in 'NS':
        n1 = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if n1 == 'N':
        break
    n = int(input('Qual o jogador deseja saber os dados ? [N] para encerrar'))
    if n > len(geral):
        print('Não existe esse jogador.')
        n = int(input('Qual o jogador deseja saber os dados ? [N] para encerrar'))
    else:
        for contador, dados in enumerate(geral[n]["Gols"]):
            print(f'No jogo {contador + 1} ele fez {dados} gols')
