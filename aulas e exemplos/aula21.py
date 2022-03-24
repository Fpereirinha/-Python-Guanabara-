def fatorial(n = 0):
    f = 1
    for c in range(n, 0, -1):
        if c == 1:
            print(c, end='=')
        else:
            print(c, end='!')
        f *= c
    print(f)


fatorial(5)

