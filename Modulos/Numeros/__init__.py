from Modulos.Strings import titulo


def fatorial(x):
    f = 1
    for c in range(x, 0, -1):
        f *= c
        if c == 1:
            print(c, end=f'={f}')
        else:
            print(c, end='!')
    return f


def moedares(x, y=0, z=0):
    titulo('RESUMO DO VALOR')
    print(f'O dobro do valor é: \t{moeda(dobro(x))}'
          f'\nA metade do valor é: \t{moeda(metade(x))}'
          f'\n{y}% de aumento é: \t\t{moeda(aumento(x,y))}'
          f'\n{z}% de redução é: \t\t{moeda(diminui(x,z))}')
    print('-'*45)


def aumento(x, y):
    r = x + (x * y/100)
    return r


def diminui(x, y):
    r = x - (x * y/100)
    return r


def dobro(x):
    r = x * 2
    return r


def metade(x):
    r = x / 2
    return r


def moeda(preco=0, simb='R$'):
    return f'{simb}{preco:.2f}'.replace('.', ',')


def leiaInt(x):
    while True:
        try:
            n = int(input(x).strip())
        except(ValueError, TypeError):
            print(f'Digite um número válido !')
        else:
            return n


def leiaFloat(x):
    while True:
        try:
            n = float(input(x).strip().replace(',','.'))
        except(ValueError, TypeError):
            print(f'Digite um número válido !')
        except(KeyboardInterrupt):
            print('Entrada interrompida pelo usúario.', end='')
            exit()
        else:
            return n


def menu(x):
    titulo('Menu Principal !')
    for c,i in enumerate(x):
        print(f'{c+1} {i}')
    opc = leiaInt('Opção: ')
    return opc
