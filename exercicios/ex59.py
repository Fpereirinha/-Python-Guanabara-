n1 = int(input('Digite o primeiro valor'))
n2 = int(input('Digite o segundo valor'))
opção = 0
while opção != 5:
    opção = int(input('''Oque deseja fazer com os 2 valores ?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números 
    [5] sair'''))
    if opção == 1:
        print(f'O resultado da soma de {n1} + {n2} é {n1+n2}')

    elif opção == 2:
        print(f'O resultado da multiplicação de {n1} x {n2} é {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor'))
        n2 = int(input('Digite o segundo valor'))
    else:
        print('opção invalida')
print('Obrigado por ultizar o programa.')


