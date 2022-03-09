x = int(input("Qual o valor a ser sacado ?"))
total = x
ced = 50
totced = 0
while True:
    if x >= ced:
        totced += 1
        x -= ced
    else:
        if totced > 0:
            print(f'Total de {totced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if x == 0:
            break
print(f'Obrigado e volte sempre !!! \nValor total sacado: R${total},00')

