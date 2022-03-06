print(f'{"Lojas Pedrocas":=^45}')
x = int(input('Qual o preço total ?'))
print('''FORMAR DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista no cartão
[3] 2x no cartão
[4] 3x+ no cartão
Qual é a opção ?''')
y = int(input(''))
if y == 1:
    print('O pagamento a vista tem um desconto de R${:.2f} e o  tota'
          'l a ser pago é de R${:.2f}.'.format((x * .1), (x * .9)))
elif y == 2:
    print('O pagamento a vista com cartão tem um desconto de R${:.2f} '
          'e o total a ser pago é de {:.2f}'.format((x * .05), (x * .95)))
elif y == 3:
    print('O valor total é de R${:.2f}. E cada parcela terá o valor de {:.2f}'.format(x, (x / 2)))
elif y == 4:
    x = x * 1.2
    z = int(input('Em quantas parcelas será feito o pagamento ?'))
    print('O valor total será de R${:.2f}.'
          ' E cada parcela terá o valor de R${:.2f}'.format(x, (x / z)))
else:
    print('Opção inválida.')
