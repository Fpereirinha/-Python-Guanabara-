c = 101010010101
soma = 0
impares = 0
pares = 0
total = 0
while c != 0:
    c = int(input('Digite um valor '))
    if c !=0 :
        soma += c
        total += 1
        if c % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'A soma de todos os números é {soma}. \n A quantidade total de números digita'
      f'dos é {total} sendo eles: \n impares : {impares} \n pares: {pares}')