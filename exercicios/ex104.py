def leiaInt(x):
    while True:
        n = str(input(x))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('Digite um número inteiro verdadeiro.')
    print(f'Você digitou {n}', end='')

leiaInt('Digite um número ')
