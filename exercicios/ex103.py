def jogador(jogadors='', gol=0):
    if jogadors:
        jogadors = jogadors
    else:
        jogadors = 'desconhecido'
    if gol == 0:
        gol = 'nenhum'
    print(f'O jogadors {jogadors} fez {gol} gols')


nome1 = str(input('Qual o nome ?'))
gol1 = str(input('Quantos gols ?'))
if gol1.isnumeric():
    gol1 = int(gol1)
else:
    gol1 = 0

jogador(nome1, gol1)
