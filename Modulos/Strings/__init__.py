def titulo(x=''):
    tot = len(x) + 30
    print(f'-' * tot)
    print(f' {x.center(tot)}')
    print(f'-' * tot)


def Leiadin(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '' or not entrada.replace('.', '').isdigit():
            print(f'\"{entrada}\"é um preço inválido.')
        else:
            break
    return float(entrada)
