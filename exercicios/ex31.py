n = int(input('Qual a distância de sua viagem ?'))
if n <=150:
    print('O preço da viagem será de R${},00'.format(n*2))
if n > 150:
    print('O preço da viagem será de R${}'.format(n*1.5))