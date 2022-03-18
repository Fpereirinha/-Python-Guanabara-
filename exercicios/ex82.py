completa = []
par = []
impar = []
soma = 0
while True:
    num = int(input('Digite o valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    completa.append(num)
    s = str(input('Quer continuar ?')).strip().upper()[0]
    while s not in 'SN':
        s = str(input('Quer continuar ?')).strip().upper()[0]
    if s == 'N':
        break
print(f'A lista completa é {sorted(completa)}.\nA lista com impares é {sorted(impar)}.'
      f'\nA lista com pares é {sorted(par)}.')
print(f'A soma das 3 listas é: ', end='')
for c in completa:
    print(c, end='+')
    soma += c
for c in par:
    print(c, end='+')
    soma += c
for x, c in enumerate(impar):
    if x < len(impar)-1:
        print(c, end='+')
    else:
        print(c, end='=')
    soma += c
print(soma)