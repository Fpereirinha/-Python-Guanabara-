def fatorial(x):
    f = 1
    for c in range(x, 0, -1):
        f *= c
        if c == 1:
            print(c, end=f'={f}')
        else:
            print(c, end='!')
    return f
