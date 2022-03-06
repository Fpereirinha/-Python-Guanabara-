numero = int(input('Qual número deseja separar ?'))
#n = str(numero)
u = numero % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}...'.format(numero))
print('Unidade {} \n Dezenas {} \n Centena {} \n Milhar {} '.format(u, d, c, m))

