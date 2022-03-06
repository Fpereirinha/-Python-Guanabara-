##x = 3 * 5 + 4 ** 2
##print('\033[0;33;44m {}\033[m'.format(x)
from time import sleep
x = int(input('Qual o seu salario ?'))
y = int(input('Qual o valor do imóvel a ser financiado ?'))
z = int(input('Em quantos anos deseja pagar ?'))
print('=-=-'*50)
print('Estamos calculando para ver se será possivel aprovar o emprestimo...')
print('=-=-'*50)
if y / (z*12) > (x*0.3):
    print('O emprestimo não pode ser aprovado, pois excede 30% do seu salário. O valor de cada prestação seria {}'
          ''.format(
        (y*0.3)
    ))
else:
    print('O emprestimo foi aprovado e o valor a ser pago mensal é de {}'.format(y / (z*12)))

