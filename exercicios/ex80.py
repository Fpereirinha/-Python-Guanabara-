números = []
quantidade = int(input('Qual a quantidade de números que deseja ordenar ?'))
for c in range(quantidade):
    n = int(input(f'Qual o {c+1}° Número ?'))
    while n in números:
        print('Número duplicado, tente novamente.')
        n = int(input(f'Qual o {c + 1}° Número ?'))
    if c == 0 or n > max(números):
        if c == 0:
            print('Adicionado na primeira posição')
        else:
            print('Adicionado na ultima posição')
        números.append(n)
    else:
        '''pos = 0
        while pos < len(números):
            if n <= números[pos]:
                números.insert(pos,n)
                print(f'Adicionado na posição {pos+1}')
                break
            pos += 1'''
        for t,x in enumerate(números):
            if n <= números[t]:
                números.insert(t,n)
                print(f'Adicionado na posição {t + 1}')
                break
for c,x in enumerate(números):
    print(f'{c+1}°: {x}')




