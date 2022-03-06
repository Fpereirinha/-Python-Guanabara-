peso = float(input('Qual seu peso ?'))
altura = float(input('Qual sua altura ?'))
imc = peso / (altura ** 2)
clas = 0
if imc < 18.5:
    clas = 'Abaixo do peso'
elif 18.5 < imc <= 25:
    clas = 'Peso ideal'
elif 25 < imc <=30:
    clas = 'Sobrepeso'
elif 30 < imc <=40:
    clas = 'Obesidade'
elif 40 < imc:
    clas = 'Obesidade Morbida'
print('Você está com o imc em {:.1f} e a classificação é {}.'.format(imc, clas))
