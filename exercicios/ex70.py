menor = maior = meno = total = cont = 0
while True:
    prod = str(input("Nome do produto:"))
    preço = int(input("Preço: R$"))
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        meno = prod
    if preço > 1000:
        maior += 1
    total += preço
    prox = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
    while prox not in 'SN':
        prox = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
    if prox == 'N':
        break
print(f'O preço total dos items foi: R${total} \n'
      f'Temos {maior} items custando mais de R$1000,00\n'
      f'O produto mais barato foi {meno}, custando R${menor}')



