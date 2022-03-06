dia = int(input('Quantos dias o carro foi alugado ?'))
km = int(input('Quantos kms foram rodados ?'))
print('O valor total a ser pago é de R${:.2f}'.format((dia*60) + (km*0.15)))

