maior = 0
menor = 0



for c in range(1,6):
    x = float(input(f'Qual o peso da {c}° pessoa ?'))
    if c == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        elif  x < menor:
            menor = x
print(f'O maior peso foi {maior}.\nE o menor peso foi {menor}')
