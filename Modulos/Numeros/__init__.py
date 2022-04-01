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
