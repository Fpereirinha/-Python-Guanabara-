s = str(input('Qual o seu sexo ? F/M'))
while s not in'fFmM':
    s = str(input('Digite novamente, você digitou alguma coisa errada.'))
if s in 'Ff':
    print('O sexo Feminino foi registrado.')
else:
    print('O sexo Masculino foi registrado.')
