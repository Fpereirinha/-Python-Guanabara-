def espacamento(x, y):
    print('=' * x)
    print(f'{y:^30}')
    print('=' * x)


def soma(*num):
    x = 0
    for cont, s in enumerate(num):
        print(f'O {cont + 1}° valor foi {s}.')
        x += s
    print(f'A soma é {x}')


def dobra(x):
    for y, item in enumerate(x):
        x[y] *= 2


numeros = [1, 2, 3, 4, 22]
dobra(numeros)
print(numeros)
soma(1, 2, 3)
