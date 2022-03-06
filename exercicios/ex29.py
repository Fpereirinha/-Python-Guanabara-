n = int(input('Qual a velocidade atual do veiculo ?'))
if n <= 60:
    print('Tenha um bom dia e dirija com cuidado.')
else:
    n = n-60
    print('A velocidade é superior ao máximo e você foi multado ! O Valor da multa é R${}'.format(n*2))