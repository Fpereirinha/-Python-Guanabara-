from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento ?'))
idade = atual - nasc
if idade <= 9:
    print(''''O atleta tem {} anos.
    Classificação: MIRIM'''.format(idade))
elif 9 < idade <= 14:
    print('''O atleta tem {} anos.
    Classificação: INFANTIL'''.format(idade))
elif 14 < idade <= 19:
    print('''O atleta tem {} anos.
    Classificação: JUNIOR.'''.format(idade))
elif 19 < idade <= 25:
    print('''O atleta tem {} anos.
    Classificação: SENIOR.'''.format(idade))
elif idade > 25:
    print('''O atleta tem {} anos.
    Classificação: MASTER'''.format(idade))
    