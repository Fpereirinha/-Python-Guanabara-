def fatorial(x):
    f = 1
    for c in range(x, 0, -1):
        f *= c
        if c == 1:
            print(c, end=f'={f}')
        else:
            print(c, end='!')
    return f


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
