n1 = float(input('Qual a primeira nota ?'))
n2 = float(input('Qual a segunda nota ?'))
media = (n1 + n2) / 2
if media > 7:
    print('Você está aprovado, sua média foi {}'.format(media))
elif media < 5:
    print('Você está reprovado, sua média foi {}.'.format(media))
elif media >=5 and media < 7:
    print('Você está de recuperação. Sua média é {}'.format(media))