import random
n1 = str(input('Digite o nome do primeiro a ser classificado:'))
n2 = str(input('Digite o nome do segundo a ser classificado:'))
n3 = str(input('Digite o nome do terceiro a ser classificado:'))
n4 = str(input('Digite o nome do quarto a ser classificado:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem a ser sorteada é {}:'.format(lista))
