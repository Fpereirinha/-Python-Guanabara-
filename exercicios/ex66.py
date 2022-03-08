x = soma = 0
while True:
    n = int(input('Digite um número a ser somado: [999 para parar]'))
    if n == 999:
        break
    x += 1
    soma += n
print(f'A soma de {x} numeros foi {soma}')

