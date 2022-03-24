from random import randint
def sortear(lista):
    for c in range(5):
        lista.append(randint(0,10))
def somp(x):
    soma = somai = 0

    for c in x:
        if c % 2 == 0:
            soma += c
            p.append(c)
        else:
            somai += c
            i.append(c)
    print(f'Somando os valores pares de {x} temos {p} = {soma}')
    print(f'Somando os valores impares de {x} temos {i} = {somai}')
i = []
p = []
n = []

sortear(n)
somp(n)



            
    
        