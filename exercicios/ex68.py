from random import randint
vitoria = 0
while True:
    n = int(input('Digite um valor'))
    s = str(input('Par ou impar ? P/I')).upper().strip()[0]
    computador = randint(0,100)
    print(f'O computador jogou {computador}')
    total = n + computador
    if s == 'P':
        print('Você escolheu par !')
        if (n + computador) % 2 == 0:
            print(f'Parabéns, a soma de {n} + {computador} é {total} que é par, você ganhou.')
        else:
            print(f'Que pena, a soma de {n} + {computador} é {total} que é impar, você perdeu.')
            break
    elif s not in 'IP':
        print('Comando inválido !')
        break
    elif s == 'I':
        print('Você escolheu impar !')
        if (n + computador) % 2 != 0:
            print(f'Parabéns, a soma de {n} + {computador} é {total} que é impar, você ganhou.')
        else:
            print(f'Que pena, a soma de {n} + {computador} é {total} que é par, você perdeu.')
            break
    vitoria += 1
if vitoria > 1:
    print(f'GAME OVER, VOCÊ GANHOU {vitoria} vezes')
elif vitoria == 0:
    print('GAME OVER, VOCÊ NÃO GANHOU NENHUMA')
else:
    print(f'GAME OVER, VOCÊ GANHOU {vitoria} VEZ')
