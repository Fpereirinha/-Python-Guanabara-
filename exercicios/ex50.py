q = int(input('Qual a quantidade de numeros pares que deseja somar ?'))
soma = 0
contador = 0
for c in range(1,q+1):
    n = int(input('Digite o {}° número (esse programa aceita 6 numeros e somará os pares.'.format(c)))
    if n % 2 == 0:
        soma += n
        contador += +1
print('A soma de {} numeros pares é {}'.format(contador,soma))