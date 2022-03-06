from random import randint
x = randint(0,10)
print(x)
y = int(input('Qual o número eu pensei ?'))
palpite = 1
while y != x:
    palpite += 1
    if x > y:
        print('MAIS ALTO !!!')
    else:
        print('Mais baixo !!!')
    print('Resposta errada, tente novamente.')
    y = int(input('Digite o novo palpite'))
print(f'Resposta correta. Acertou com {palpite} palpites')