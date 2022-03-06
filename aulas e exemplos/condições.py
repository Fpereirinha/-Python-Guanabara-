##tempo = int(input("Quantos anos tem seu carro ?"))
#if tempo >=3:
#    print("Ta no osso pedrão")
#else:
#    print('Ta suave mens')
#print('carro novo' if tempo >=3 else 'carro velho')##
n1 = float(input('Nota 1 :'))
n2 = float(input('Nota 2'))
n3 = float(input('Nota 3'))
print('Sua média é {:.2}'.format((n1+n2+n3)/3))
if ((n1+n2+n3) / 3) < 6:
    print('Você não passou.')
else:
    print('Você passou !')

