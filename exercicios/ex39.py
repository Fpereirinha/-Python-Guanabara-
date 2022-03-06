import datetime
atual = datetime.date.today().year
nasc = int(input('Qual ano de nascimento ?'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você precisa se alistar esse ano !')
elif idade < 18:
    print('Você ainda não precisa se alistar, faltam ainda {} anos e seu alistamento será em {}.'
          .format(18 - idade, atual + ( 18 - idade)))
elif idade > 18:
    print('Passou da data de alistamento, corre lá !')