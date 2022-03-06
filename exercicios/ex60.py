n = int(input('Digite um numero para ser fatorado.'))
c = n
f = 1
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f)