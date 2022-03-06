salario = int(input('Qual seu salario ?'))
if salario <= 1250:
    print('Seu aumento foi de 15% e seu novo salário é R${}'.format(salario*1.15))
if salario >1250:
    print('Seu aumento foi de 10% e seu novo salário é {}'.format(salario*1.1))
