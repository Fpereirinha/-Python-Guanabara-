i = c = soma = media = 0
while i != 999:
    i = int(input('Digite um numero, 999 para parar / caso queira saber a média e parar agora 998:'))
    if i == 998:
        media = soma / c
        break
    if i == 999:
        break
    else:
        soma += i
        c += 1
if i != 998:
    print(f'A soma de {c} numeros é {soma}')
else:
    print(f'A soma de {c} numeros é {soma} e a média é {media}')
