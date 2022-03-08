x = c = maior = menor = soma = 0
y = 'S'
while y == 'S':
    x = int(input('Digite um número para verificarmos o maior e menor.'))
    y = str(input("Quer continuar ? S / N")).upper().strip()[0]
    c += 1
    soma += x
    if c == 1:
        maior = menor = x
    if x > maior:
        maior = x
    elif x < menor:
        menor = x

print(f'{maior} e {menor} e foram digitados {c} numeros media é {soma/c:.2f}')