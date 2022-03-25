def fatorial(x, show=False):
    """
    -> Calcula o fatorial
    :param x: Número a ser calculado o fatorial
    :param show: mostrar ou não sequencia
    :return: fatorial calculado.
    """
    fat = 1
    for c in range(x, 0, -1):
        fat *= c
        if show:
            if c > 1:
                print(f'{c}! ', end='')
            else:
                print(f'{c}', end=' = ')
    print(fat)


fatorial(5, True)

