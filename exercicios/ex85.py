c = 0
lista = [[], []]
while c < 7:
    x = int(input(f'Digite o {c+1}° valor:'))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
    c += 1
if len(lista[1]) == 0:
    print('Não houve valores impares.')
else:
    print(f'Os valores impares digitados foram {sorted(lista[1])}' if len(lista[1]) > 1 else
          f'O valor impar digitado foi {lista[1]}')
if len(lista[0]) == 0:
    print('Não houve valores pares.')
else:
    print(f'Os valores pares digitados foram {sorted(lista[0])}'
          if len(lista[0]) > 1 else f'O valor par digitado foi'
         f'{lista[0]}.')
