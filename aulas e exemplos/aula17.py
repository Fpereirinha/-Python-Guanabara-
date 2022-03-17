from random import randint
n = []
'''n2 = len(n)
n1 = n[2] - n2
print(n1)'''
y = 0
p = [1,2]
while True:
    x = randint(1,100)
    if x not in n:
        n.append(x)
    while 5 in n:
        n.remove(5)
    if len(n) > 5:
        if 2 in n:
            n = []
            n.append(2)
        elif 1 in n:
            n = []
            n.append(1)
        else:
            n = []
        y += 1
        print(y)
    if 1 in n:
        if 2 in n:
            break
    if y >= 10:
        break
if 1 in n:
    print('1 está na lista')
    if 2 in n:
        print('2 Está na lista')
        print(f'acabou com {y} listas geradas')
    else:
        print('2 Não está na lista')
        print('fim')
else:
    print('Não foi dessa vez.')

print(n)