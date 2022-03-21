partidas = []
jogador = {}
jogador['Nome'] = str(input('Qual o nome do jogador ?'))
total = int(input('Quantas partidas foram jogadas ?'))
for c in range(total):
    n = int(input(f'Quantos gols ele marcou no {c+1}° jogo ?'))
    partidas.append(n)
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
for k, v in jogador.items():
    print(k,v)
print(f'O jogador {jogador["Nome"]} fez {total} partidas')
for contador, valor in enumerate(jogador['Gols']):
    print(f'No {contador+1}° jogo foram feitos {valor} gols')
print(f'O total de gols marcados foi {jogador["Total"]}')