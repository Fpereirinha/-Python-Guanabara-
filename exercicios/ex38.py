x = int(input('Qual o primeiro número ?'))
y = int(input('Qual o segundo número :'))
if x > y:
    print('O primeiro número é maior.')
elif x < y:
    print('O segundo número é maior.')
elif x == y:
    print('Os 2 números são iguais.')
else:
    print('Opção invalida, revise os dados.')