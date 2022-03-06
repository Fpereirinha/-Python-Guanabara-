from random import randint
## jogar = int(input())
empate = str('Empate')
vc = str('Vitória do computador.')
nome = str(input('Qual o seu nome Jogador ?'))
vj = str('Vitória do {}'.format(nome))
print('''Qual é sua opção {}?
[0] PEDRA
[1] PAPEL
[2] TESOURA'''.format(nome))
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input(''))
computador = randint(0,2)
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA ')
else:
    print('O jogador jogou {} e o computador jogou {}'.format(itens[jogador], itens[computador]))
if jogador == 0: ## pedra
    if computador == 0:
        print(empate)
    elif computador == 1:
        print(vc)
    elif computador == 2:
        print(f'\n\033[34m{vj}')
if jogador == 1: ## papel
    if computador == 0:
        print(f'\n\033[34m{vj}')
    elif computador == 1:
        print(empate)
    elif computador == 2:
        print(vc)
if jogador == 2: ## tesoura
    if computador == 0:
        print(vc)
    elif computador == 1:
        print(f'\n\033[34m{vj}')
    elif computador == 2:
        print(empate)
