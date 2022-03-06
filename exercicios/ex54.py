from datetime import date
y = 0
f = 0
data = date.today().year
quantidade = int(input('Qual a quantidade de pessoas que deseja consultar ?'))
for c in range (1, quantidade + 1):
    x = int(input(f'Qual o ano de nascença da {c}° pessoa ?'))
    if data - x < 18:
        y += 1
    elif data - x >= 18:
        f += 1
print(f'Temos {f} maiores de idades. \n E temos {y} menores de idade.')

