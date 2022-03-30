from Modulos.Numeros import metade, dobro, aumento, diminui
x = int(input('Digite o preço:'))
print(f'A metade de {x} é {metade(x)}'
      f'\nO dobro de {x} é {dobro(x)}'
      f'\nAumentando 10% temos {aumento(x,10)}'
      f'\nDiminuindo 10% temos {diminui(x,10)}')
