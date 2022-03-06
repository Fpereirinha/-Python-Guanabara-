fr = str(input('Digite uma frase para avaliarmos.')).strip().lower()
print('A quantidade de As é {}.'.format(fr.count('a')))
print('A primeira letra A aparece na {} posição.'.format(fr.find('a')+1))
print('A última letra A aparece na posição {}.'.format(fr.rfind('a')+1))
