def maior(*num):
    maior = 0
    for contador, value in enumerate(num):
        if contador == 0:
            maior = value
        else:
            if value > maior:
                maior = value
        print(f'O {contador+1}° número digitado foi {value}.')
    print(f'Foram digitados no total {len(num)} números' f'\nO maior valor informado foi {maior}')


def maiors(*num):
    for value in num:
        print(f'{value}', end=' ')
    print(f'O maior valor digitado foi {max(num)}, e a quantidade foi {len(num)}.')


maiors(1,3,5,111,2)